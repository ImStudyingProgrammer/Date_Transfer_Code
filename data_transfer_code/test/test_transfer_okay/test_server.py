"""
=============================================
Writer: MaskerTim

README:
This is the server test program for transferring data.
You can try it to test whether the program is okay or not.
=============================================
""" 

import sys
import os
sys.path.append(os.getcwd())

import threading
from channel.channel_server_api import ServerArmor
import socket

if __name__=="__main__":
    # create server's socket
    # for local test
    # server = ServerArmor("127.0.0.1", 8888)
    # for remote test
    # server = ServerArmor("192.168.98.226", 8888)
    hostname = socket.gethostname()
    print(socket.gethostbyname(hostname))
    server = ServerArmor(socket.gethostbyname(hostname), 8888)

    # accept the client's shooting
    while True:
        client, client_addr = server.accept()
        print("the accepted client %s:%d" % (client_addr[0], client_addr[1]))

        t = threading.Thread(target=server.defend, args=(client, client_addr, True))
        t.start()