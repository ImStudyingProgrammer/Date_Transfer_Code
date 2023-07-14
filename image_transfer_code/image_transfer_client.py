from channel.channel_client_api import ClientHandgun
import os
import time

""" For Debug """
import cv2

if __name__=="__main__":
    # load images
    dirpath = "resources/images/angry/"
    files = os.listdir(dirpath)
    images = []
    for f in files:
        img = cv2.imread(dirpath+f)
        images.append(img)

    # create client's socket
    client = ClientHandgun("127.0.0.1", 8888)
    # client = ClientHandgun(os.getenv("IP"), int(os.getenv("PORT")))

    for img in images:
        # load the set of data (e.g., images)
        client.load_bullet(img)
        client.shoot()
        time.sleep(0.5)
    client.drop_gun()
