import IO
import sys
import os
import subprocess
from socket import socket

__workingdir = os.path.dirname(os.path.abspath(__file__))

def startserver(address, port, startshell):
    """Starts a simulator instance at the given address and port.
    If startshell is True, a seperate python instance will be created
    that is connected to the server"""
    sock = socket()
    sock.bind((address, port))
    sock.listen(2)

    if startshell:
        subprocess.Popen([sys.executable, __workingdir + '/Shell.py', address, str(port)])

    while True:
        conn, addr = sock.accept()
        print('Connected to client at ', addr)
        while True:
            response = IO.readinputbytes(getCmd(conn))
            if response == '':
                conn.close()
                break

            else:
                print ('response:', response)
                try:
                    conn.send(str.encode(response.getresponse()))
                except:
                    conn.close()
                    break


def getCmd(c):   
    """
        reads the next cr delimited command from the socket
        filters out linefeeds
        returns a normalized string command
        or empty string if read fails
    """
    cmd=''
    while True:
        try:
            data = c.recv(1).decode('utf-8')
        except:
            return ''

        if not data:
            return ''

        if data == '\n':
            continue    # ignore linefeed 

        if data == '\r': # cr is terminator, but ignore it
            break

        cmd += data.upper()

    print ('received:', cmd)
    return cmd  
