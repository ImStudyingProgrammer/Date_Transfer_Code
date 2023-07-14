import cv2
import pickle
import socket
import struct
import os

class ServerArmor():
    def __init__(self, ip, port):
        """ Initialize server socket and start running """
        self.__serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.__serverSocket.bind((ip, port))
        self.__serverSocket.listen()
        print("server is running")

    def accept(self):
        """ server wait to accept the client socket """
        return self.__serverSocket.accept()

    def defend(self, client, client_addr, want_write=False):
        """ process the data sent from client """
        payload_size = struct.calcsize('L')
        # debug: count the number of images
        count = 0

        try:
            while True:
                data = b''
                # the size of data
                while len(data) < payload_size:
                    data += client.recv(4096)

                if data == b'': continue

                packed_msg_size = data[:payload_size]
                # it is possible that has remaining data content
                data = data[payload_size:]
                msg_size = struct.unpack('L',packed_msg_size)[0]

                # Retrieve all data based on message
                while len(data) < msg_size:
                    data += client.recv(1024)

                # convert byte stream to original data struct 
                msg_data = data[:msg_size]
                data = data[msg_size:]
                msg = pickle.loads(msg_data)
                
                # check the message is image data or checking channel message
                if type(msg) == str:
                    # if data is received, response Ok to client
                    client.sendall("OK".encode())
                    continue

                image = cv2.imdecode(msg, cv2.IMREAD_GRAYSCALE)

                # debug: counter for receiving the number of data
                count += 1
                print("client %s:%d, the count: %d" % (client_addr[0], client_addr[1], count))

                 # debug: write image info files for checking there is no missing data
                if want_write:
                    self.__write_file("{}_{}_{}.jpg".format(client_addr[0], client_addr[1], count), image) 
        except Exception as err:
            print(err)
        finally:
            # close the client socket
            print("client %s:%d is closed" % (client_addr[0], client_addr[1]))
            client.close()

    # debug: test to write data into file for checking there is no missing data 
    def __write_file(self, img_name, data):
        current_dir = os.getcwd()
        if cv2.imwrite(current_dir+"/written_img/"+img_name, data):
            print("write successfully")


