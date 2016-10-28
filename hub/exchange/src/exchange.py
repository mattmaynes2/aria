import socket

class Exchange ():
    PORT = 7600 # Default system port

    def __init__ (self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.port = Exchange.PORT

    def bind (self):
        try:
            self.socket.bind(('localhost', self.port))
            print('Socket opened to port ' + str(self.port))
        except socket.error as msg:
            print('Socket failed to connect to port ' + str(self.port) + ' with: ' + msg);



if (__name__ == '__main__'):
    exc = Exchange()
    exc.bind()
    print('Success!')


