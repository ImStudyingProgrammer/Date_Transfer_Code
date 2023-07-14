import sys
import os
sys.path.append(os.getcwd())

from channel.channel_client_api import ClientHandgun
import pickle
import time

def gun_shooting(shooter, bullet):
    shooter.load_bullet(bullet)
    shooter.shoot()

if __name__=="__main__":
    # load the test data
    file = open("test/test_data/test.p", "rb",)
    data = pickle.load(file)
    data = data['Y_test']
    print("Shape of array: ",data.shape)

    # create client's socket
    client = ClientHandgun("127.0.1.1", 8888)
    # client = ClientHandgun(os.getenv("ip"), 8888)

    # send the data from dataset one by one
    for d in data[:3]:
        bullet = d
        gun_shooting(client, bullet)
        # Ok means the sent data is successful
        if client.blocking() != "OK":
            gun_shooting(client, bullet)
        time.sleep(0.5)

    client.drop_gun()