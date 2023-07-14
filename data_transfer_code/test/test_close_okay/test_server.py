import sys
import os
sys.path.append(os.getcwd())

import threading
from channel.channel_server_api import ServerArmor
import socket

if __name__=="__main__":
    # create server's socket
    hostname = socket.gethostname()
    print(socket.gethostbyname(hostname))
    server = ServerArmor(socket.gethostbyname(hostname), 8888)

    # accept the client's shooting
    while True:
        client, client_addr = server.accept()
        print("the accepted client %s:%d" % (client_addr[0], client_addr[1]))

        t = threading.Thread(target=server.defend, args=(client, client_addr))
        t.start()