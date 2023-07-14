"""
=============================================
Writer: MaskerTim

README:
This is the server program for data transfer.
You could customize the code to satisfy your requirements.
The following code is just an example for your reference.
=============================================
""" 

import threading
from channel.channel_server_api import ServerArmor
import socket
import os

if __name__=="__main__":
    # create server's socket
    hostname = socket.gethostname()
    print(socket.gethostbyname(hostname))
    # create server's socket. Port configured in Dockerfile
    server = ServerArmor(socket.gethostbyname(hostname), int(os.getenv("PORT")))

    # accept the client's socket which request to connect
    while True:
        client, client_addr = server.accept()
        print("the accepted client %s:%d" % (client_addr[0], client_addr[1]))
        # if accept the client, start the services for client
        t = threading.Thread(target=server.defend, args=(client, client_addr))
        t.start()
