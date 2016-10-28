import socket
import comm
import message

class NativeComm (comm.Comm):
    PORT = 7600 # Default system port

    def __init__ (self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.port = NativeComm.PORT
        self.addressCache={}

    def setup (self, listener):
        self.listener=listener
        try:
            self.socket.bind(('localhost', self.port))
            print('Socket opened to port ' + str(self.port))
        except socket.error as msg:
            print('Socket failed to connect to port ' + str(self.port) + ' with: ' + msg);
        self.receive()

    def teardown (self):
        self.socket.close()
        return True


    """
    scan network for any new devices
    """
    def discover(): pass

    """
    send a message to a device
    """
    def send(self,msg):
        sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        if(msg.receiver in self.addressCache ):
            sock.sendto(msg.encode(),self.addressCache[msg.receiver])
        else:
            raise NameError('Unknown receiver')

    """
    listen for messages from devices
    """
    def receive(self):
        data,address = self.socket.recvfrom(1024)
        msg = message.Message.decode(data)
        self.addressCache[msg.sender]=address
        self.listener.message(msg)

