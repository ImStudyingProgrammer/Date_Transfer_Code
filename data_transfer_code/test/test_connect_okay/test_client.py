import sys
import os
sys.path.append(os.getcwd())

from channel.channel_client_api import ClientHandgun
import time

if __name__=="__main__":
    client = ClientHandgun("127.0.1.1", 8888)
    
    while True:
        if client.blocking() == "OK":
            print("the connection channel is okay!")
            break
        print("the channel has some problem, so just reconnect.")
        time.sleep(2)
        client.drop_gun()
        client = ClientHandgun("127.0.1.1", 8888)
    # close the connection
    client.drop_gun()