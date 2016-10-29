import socket

from .message import Message
from .adapter import Adapter

class AriaAdapter (Adapter):
    BUFFER_SIZE = 4096
    PORT        = 7600

    def __init__ (self):
        super().__init__()
        self.socket     = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.port       = AriaAdapter.PORT
        self._ip_map    = {}

    def setup (self, delegate):
        super().setup(delegate)

        try:
            self.socket.bind((socket.gethostname(), self.port))
        except socket.error as msg:
            print('Socket failed to connect to port ' + str(self.port) + ' with: ' + msg);

    def teardown (self):
        super().teardown()
        self.socket.close()
        return True

    def send (self, msg, address = None):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        if (address):
            receiver = address
        elif (msg.receiver in self._ip_map):
            receiver = self._ip_map[msg.receiver]
        else:
            raise NameError('Unknown receiver')

        sock.sendto(msg.encode(), receiver)

    def receive (self):
        data, address = self.socket.recvfrom(AriaAdapter.BUFFER_SIZE)
        msg = Message.decode(data)
        self._ip_map[msg.sender] = address
        self.delegate.received(msg)

