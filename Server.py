import pickle, socket, struct, sys, threading

SERVERADDRESS = ("localhost", 5000)
users_list = {}

class Server():
    def __init__(self):
        self.__server = socket.socket()
        self.__server.bind(SERVERADDRESS)


    def run(self) :
        self.__server.listen(4)
        print("Server adress is {}".format(SERVERADRESS))
        while True :
            client ,addr = self.__s.accept()
            print (self. _receive(client).decode ())

    def exit(self) :
        self.__server.close()


if __name__ == '__main__':
    Server().run()
