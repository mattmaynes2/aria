import socket
import comm
import message

class NativeComm (comm.Comm):
    PORT = 7600 # Default system port

    def __init__ (self):
        super().__init__()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.port = NativeComm.PORT
        self._addresses={}

    def setup (self, listener):
        self.listener = listener
        try:
            self.socket.bind(('localhost', self.port))
            print('Socket opened to port ' + str(self.port))
        except socket.error as msg:
            print('Socket failed to connect to port ' + str(self.port) + ' with: ' + msg);

    def teardown (self):
        super().teardown()
        self.socket.close()
        return True


    """
    scan network for any new devices
    """
    def discover(): pass

    """
    send a message to a device
    """
    def send(self, msg, address = None):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        if (address):
            receiver = address
        elif (msg.receiver in self._addresses):
            receiver = self._addresses[msg.receiver]
        else:
            raise NameError('Unknown receiver')

        sock.sendto(msg.encode(), receiver)

    """
    listen for messages from devices
    """
    def receive(self):
        data,address = self.socket.recvfrom(1024)
        msg = message.Message.decode(data)
        self._addresses[msg.sender]=address
        print ('Got Message')
        self.listener.message(msg)

