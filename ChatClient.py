import pickle, socket, struct, sys, threading
import traceback

class Chat ():
    def __init__(self , host = socket.gethostname(),port =4848, nickname = "NoBody") :
        s = socket.socket()
        s.settimeout(0.5)
        s.bind((host,port))
        self.__s = s
        self.__nickname = nickname

        print('Listening on {}:{}'.format(host, port))

    def run(self):
        handlers = {
            '/exit ': self._exit,
            '/quit' : self._quit,
            '/join' : self._join,
            '/send': self._send
        }
        self.__running = True
        self.__address = None
        threading.Thread(target = self._receive ).start()
        while self.__running :
            line = sys.stdin.readline().rstrip()+ ' '
            command = line[:line.index(' ')]
            param = line[line.index(' ')+1:].rstrip()
            if command in handlers :
                try :
                    handlers[command]() if param == '' else handlers [command](param)
                except RunError :
                    print("RunningError")
            else :
                print ('Unknown command :', command )

    def _exit(self):
        self.__running = False
        self.__address = None
        self.__s.close()

    def _quit(self):
        self.__address = None

    def _join(self, param):
        if self.__nickname = "NoBody" :
            self.__nickname = str(input("Please choose a nickname : "))
        nickname = str(self.__nickname+" : ").encode()

        tokens = param.split(' ')
        if len(tokens) == 2:
            try :
                self.__address = (tokens[0], int(tokens[1]))
                self.__socket.connect(self.__address)
                threading.Thread(target=self._receive).start()
                print('Connected to {}:{}'.format(*self.__address))
            except JoinError :
                print("Join Error.")


    def _send(self, param):
        if self.__address is not None :
            try :
                message = param.encode()
                totalsent = 0
                while totalsent < len ( message ):
                    sent = self.__s.sendto(message[totalsent:], self.__address)
                    totalsent += sent
                print(self.__socket.recv(2048).decode())
            except OSError :
                print("Send error")

    def _receive(self):
        while self.__running :
            try :
               data, address = self.__s.recvfrom(2048)
               print(data.decode())
            except socket.timeout :
               pass

if __name__ == '__main__':

    if len(sys.argv) == 3:
        Chat(sys.argv[1], int(sys.argv[2])).run()
    else:
        Chat().run()
