import sys
import os
sys.path.append(os.getcwd())

from channel.channel_server_api import ServerArmor
import socket
import threading

if __name__=="__main__":
    hostname = socket.gethostname()
    print(socket.gethostbyname(hostname))
    server = ServerArmor(socket.gethostbyname(hostname), 8888)

    # accept the client's shooting
    while True:
        client, client_addr = server.accept()
        print("the accepted client %s:%d" % (client_addr[0], client_addr[1]))
        # start the client thread
        t = threading.Thread(target=server.defend, args=(client, client_addr))
        t.start()