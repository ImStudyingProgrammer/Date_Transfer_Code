import threading
from channel.channel_server_api import ServerArmor
import socket
import os

if __name__=="__main__":
    # create server's socket
    server = ServerArmor("127.0.0.1", 8888)
    # hostname = socket.gethostname()
    # print(socket.gethostbyname(hostname))
    # server = ServerArmor(socket.gethostbyname(hostname), int(os.getenv("PORT")))

    # accept the client's shooting
    while True:
        client, client_addr = server.accept()
        print("the accepted client %s:%d" % (client_addr[0], client_addr[1]))
        # start the processing thread for client
        t = threading.Thread(target=server.defend, args=(client, client_addr, True))
        t.start()
