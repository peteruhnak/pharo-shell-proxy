# -*- coding: utf-8 -*-
# socket proxy to run shell commands from Pharo
# mainly for Windows, because ProcessWrapper is just broken and I am tired

import os
import sys
import socket
import tempfile

PORT_FILE = tempfile.gettempdir() + '\pharo-shell-proxy-port.txt'

def stop_server():
    if not os.path.isfile(PORT_FILE):
        print 'Server is not running.'
        return
    #/if

    with open(PORT_FILE, 'r') as f:
        port = int(f.read())
    #/with

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', port,))
    sock.sendall('terminate')
    sock.close()
    print 'Server stopped.'
#/def

if __name__ == '__main__':
    stop_server()
#/if
