import cv2
import pickle
import socket
import struct
import os
import time

class ClientHandgun():
    def __init__(self, ip:str, port:int):
        self.__socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        # connect to server
        self.__connect(ip, port)
        # the data that would like to send
        self.__bullets = []
        # wrapped functions
        self.__wrapped = []
    
    # load the data for sending to server
    def load_bullets(self, dirpath:str):
        files = os.listdir(dirpath)
        for f in files:
            img = cv2.imread(dirpath+f)
            self.__bullets.append(img)

    # add the wrapped function for preprocessing
    def refit_gun(self, func):
        self.__wrapped.append(func)
    
    # send the data controled by myself
    def shoot(self): 
        for img in self.__bullets:
            result, img = cv2.imencode("'.jpg", img, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
            img = pickle.dumps(img)
            img_size = struct.pack("L", len(img))
            self.__socket.sendall(img_size+img)
            yield "success" # use generator to control the time of sending by myself

    # send the all data to server continuously
    def round_shoot(self):
        for img in self.__bullets:
            result, img = cv2.imencode("'.jpg", img, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
            img = pickle.dumps(img)
            img_size = struct.pack("L", len(img))
            self.__socket.sendall(img_size+img)
            time.sleep(2)
        print("no bullets")

    # close the socket
    def drop_gun(self):
        try:
            self.__socket.close()
            print("succeed to close socket")
        except socket.error as err:
            print("the connection is closed", err)

    """ Private: client connects to server"""
    def __connect(self, ip, port):
        try:
            self.__socket.connect((ip, port))
            print("the connection is success")
        except socket.error as err:
            print("the connection is failed", err)
