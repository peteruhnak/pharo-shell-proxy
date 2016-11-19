# -*- coding: utf-8 -*-
# socket proxy to run shell commands from Pharo
# mainly for Windows, because ProcessWrapper is just broken and I am tired

from subprocess import Popen,PIPE
import os
import sys
import json
import socket
from base64 import b64encode, b64decode
import threading

PORT_FILE = sys.path[0] + '\port.txt'

class ShellServer(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.create_socket()
    #/def

    def create_socket(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.host, self.port))
        if self.port == 0:
            self.port = self.socket.getsockname()[1]
        #/if
        with open(PORT_FILE, 'w') as f:
            f.write(str(self.port))
        #/with
    #/def

    def run(self):
        print 'Listening on ', (self.host, self.port,)
        self.socket.listen(1)
        self.running = True
        while self.running:
            print 'waiting for accept'
            client, address = self.socket.accept()
            print 'Connected client on ', address
            clientThread = threading.Thread(target=self.processClient,args=(client,))
            clientThread.start()
        #/while
        self.socket.close()
        print 'Server terminated.'
    #/def

    def processClient(self, client):
        print 'Processing client', client
        data = client.recv(1024).strip()
        print 'Received:', data
        if data == 'terminate':
            client.close()
            self.terminate()
            return
        if data == '':
            print 'No data'
            client.close()
            return
        #/if
        response = self.processCommand(data)
        client.sendall(response)
        client.close()
        print 'Client processed', client
    #/def

    def terminate(self):
        self.running = False
        # Create an artificial connection to stop accept() from inside
        terminatingSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        terminatingSocket.connect((self.host, self.port,))
        os.remove(PORT_FILE)
    #/def

    def processCommand(self, data):
        # data is B64(JSON(command))
        command = json.loads(b64decode(data))
        print 'Received command:', command
        response = self.runCommand(command)
        response['stdout'] = b64encode(response['stdout'])
        response['stderr'] = b64encode(response['stderr'])
        print 'Sending:', response
        return json.dumps(response)
    #/def

    def runCommand(self, args):
        p = Popen(args, stdout=PIPE, stderr=PIPE)
        out, err = p.communicate()
        code = p.returncode
        return {'exitCode':code, 'stdout':out, 'stderr':err}
    #/def

#/class


if __name__ == '__main__':
    server = ShellServer('localhost', 0)
    server.run()
#/if
