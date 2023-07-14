"""
=============================================
Writer: MaskerTim

README:
This is the client program for data transfer.
You could customize the code to satisfy your requirements.
The following code is just an example for your reference.
=============================================
""" 

from channel.channel_client_api import ClientHandgun
import time
import os
import pickle

""" For Debug """
import numpy as np

# send the data to server
def gun_shooting(shooter, bullet):
    shooter.load_bullet(bullet)
    shooter.shoot()

if __name__=="__main__":

    # create client's socket
    # client = ClientHandgun("127.0.1.1", 8888)
    # create client's socket. IP, Port configured in Dockerfile
    client = ClientHandgun(os.getenv("IP"), int(os.getenv("PORT")))

    # mock ndarray struct of data
    t1 = np.array([1.0,2.,0,3.0])
    t2 = np.array([[1.0,1.0,2.0],[2.0,2.0,2.0]])
    t3 = np.array([[1.0,2.0],[2.0,3.0],[3.0,4.0]])
    mock_data = [t1, t2, t3]

    # load the mock dataset
    # file = open("test/test_data/test.p", "rb",)
    # data = pickle.load(file)
    # mock_data = data['Y_test']
    # print("Shape of array: ",data.shape)

    # send the data from dataset one by one
    for d in mock_data[:100]:
        bullet = d
        gun_shooting(client, bullet)
        # received the server response message
        # if okay, the message is received; Otherwise, resend the data
        if client.blocking() != "OK":
            gun_shooting(client, bullet)
        # wait the transmission time
        time.sleep(0.5)

    # close the client
    client.drop_gun()
    
