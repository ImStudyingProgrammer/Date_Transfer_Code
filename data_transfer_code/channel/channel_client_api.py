import pickle
import socket
import struct
import time

class ClientHandgun():
    def __init__(self, ip:str, port:int):
        self.__socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        # connect to server and check the channel is okay
        self.__connect(ip, port)
        # wait the interval time of connection setup
        time.sleep(2)
        self.__checkchannel()
        # the data that would like to send
        self.__bullets = []
        # wrapped functions
        self.__wrapped = []
    
    def load_bullet(self, data):
        """ load the data for sending to server """
        self.__bullets.append(data)

    # @Ignore
    def refit_gun(self, func):
        """ add the wrapped function for preprocessing """
        self.__wrapped.append(func)
    
    def shoot(self):
        """ send the data controled by myselimg_size = struct.pack("L", len(img)) """
        
        # if the bullet is no less than 0, then it enable to shoot
        if len(self.__bullets) > 0:
            data = self.__bullets.pop(0)
            b_data = pickle.dumps(data)
            b_data_size = struct.pack("L", len(b_data))
            self.__socket.sendall(b_data_size+b_data)

    # @Ignore
    def round_shoot(self):
        """ send the all data to server continuously """
        for data in self.__bullets:
            b_data = pickle.dumps(data)
            b_data_size = struct.pack("L", len(b_data))
            self.__socket.sendall(b_data_size+b_data)
            time.sleep(2)
        print("no bullets")

    def blocking(self):
        """ wait and receive the message from server """
        msg = b''
        msg = self.__socket.recv(16)
        return msg.decode()
        
        
    def drop_gun(self):
        """ close the socket """
        try:
            self.__socket.close()
            print("succeed to close socket")
        except socket.error as err:
            print("the connection is closed", err)

    # @Private
    def __connect(self, ip, port):
        """ client connects to server """
        try:
            self.__socket.connect((ip, port))
            print("the connection is success")
            # test message to check the channel is okay
        except socket.error as err:
            print("the connection is failed", err)

    # @Private
    def __checkchannel(self):
        """ check the channel is okay """
        b_data = pickle.dumps("test")
        b_data_size = struct.pack("L", len(b_data))
        self.__socket.sendall(b_data_size+b_data)
