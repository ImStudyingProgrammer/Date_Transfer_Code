import pickle
import socket
import struct

class ServerArmor():
    def __init__(self, ip, port):
        """ Initialize server socket and start running """
        self.__serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.__serverSocket.bind((ip, port))
        self.__serverSocket.listen()
        print("server is running")

        # debug: the received data is complete
        self.__debug_stored = []

    def accept(self):
        """ server wait to accept the client socket """
        return self.__serverSocket.accept()

    def defend(self, client, client_addr, want_write=False):
        """ process the data sent from client """
        payload_size = struct.calcsize('L')
        count = -1
        
        try:
            while True:
                data = b''
                # the size of data
                while len(data) < payload_size:
                    data += client.recv(1024)

                if data == b'': continue
                
                packed_msg_size = data[:payload_size]
                # it is possible that has remaining data content
                data = data[payload_size:]
                msg_size = struct.unpack('L',packed_msg_size)[0]

                # Retrieve all data based on message
                while len(data) < msg_size:
                    data += client.recv(1024)

                # convert byte stream to original data struct 
                nd_data = data[:msg_size]
                _ = data[msg_size:]
                data = pickle.loads(nd_data)
                
                # Debug
                self.__debug_stored.append(data)
                print("the client's data:", data)

                # if data is received, response Ok to client
                client.sendall("OK".encode())

                # debug: counter for receiving the number of data
                count += 1
                print("client %s:%d, the count: %d" % (client_addr[0], client_addr[1], count))
        except Exception as err:
            print(err)
        finally:
            if want_write:
                self.__write_file()
            # close the client socket
            print("client %s:%d is closed" % (client_addr[0], client_addr[1]))
            client.close()

    """ For debug: save the after-transfer data in files for checking """
    def __write_file(self):
        # debug: the received data is complete
        fw = open("after.p", "wb")
        pickle.dump(self.__debug_stored, fw)
        fw.close()


        


