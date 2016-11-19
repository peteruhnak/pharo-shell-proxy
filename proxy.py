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
import logging
from datetime import datetime

def configure_logging():
    logDir = sys.path[0] + '\logs'
    if not os.path.isdir(logDir):
        os.mkdir(logDir)
    #/if
    logging.basicConfig(
        filename=logDir + '\\' + datetime.now().strftime('%Y-%m-%d.log'),
        format='[%(asctime)s] %(message)s',
        level=logging.DEBUG
    )
#/def

configure_logging()


PORT_FILE = sys.path[0] + '\port.txt'

class ShellServer(object):
    def __init__(self, host, port):
        logging.info('Starting new server...')
        self.host = host
        self.port = port
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
        logging.info('Started on %s', self.socket.getsockname())
    #/def

    def run(self):
        self.create_socket()
        logging.info('Listening...')
        self.socket.listen(1)
        self.running = True
        while self.running:
            client, address = self.socket.accept()
            logging.info('Accepted client on %s', address)
            clientThread = threading.Thread(target=self.processClient,args=(client,address))
            clientThread.start()
        #/while
        self.socket.close()
        logging.info('Stopping server...')
    #/def

    def processClient(self, client, address):
        logging.info('%s Processing client...', address)
        data = client.recv(1024).strip()
        logging.info('%s Received: %s', address, data)
        if data == 'terminate':
            logging.info('%s Received \'terminate\' command, closing.', address)
            client.close()
            self.terminate()
            return
        #/if
        if data == '':
            logging.info('%s Received no data, closing.', address)
            client.close()
            return
        #/if
        try:
            response = self.processCommand(data)
            client.sendall(response)
        except Exception:
            logging.exception('Client exception')
        #/try
        client.close()
        logging.info('%s Client processed.', address)
    #/def

    def terminate(self):
        self.running = False
        # Create an artificial connection to stop accept() from inside
        logging.info('Executing termination connection.')
        terminatingSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        terminatingSocket.connect((self.host, self.port,))
        os.remove(PORT_FILE)
    #/def

    def processCommand(self, data):
        # data is B64(JSON(command))
        logging.info('Processing command...')
        logging.debug('base64: %s', data)
        jsonString = b64decode(data+'213')
        logging.debug('json: %s', jsonString)
        command = json.loads(jsonString)
        response = self.runCommand(command)
        response['stdout'] = b64encode(response['stdout'])
        response['stderr'] = b64encode(response['stderr'])
        logging.debug('Truncated response: %s', (response['exitCode'], response['stdout'][:100], response['stderr'][:100],))
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
    logging.info('Bye.')
#/if
