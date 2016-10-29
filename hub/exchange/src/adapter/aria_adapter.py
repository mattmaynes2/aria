import socket

from .message import Message
from .adapter import Adapter

from device import Device

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
            self.socket.bind(('localhost', self.port))
        except socket.error as msg:
            print('Socket failed to connect to port ' + str(self.port) + ' with: ' + str(msg));
            return False
        return True

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

        print('Sending')
        sock.sendto(msg.encode(), receiver)
        print('Sent')
        sock.close()

    def receive (self):
        print('Listening')
        data, address = self.socket.recvfrom(AriaAdapter.BUFFER_SIZE)
        print('Received')
        msg = Message.decode(data)
        self._ip_map[msg.sender] = address

        if (msg.type == Message.Discover):
            self.delegate.discovered(Device('aria', '', msg.sender))
            self.delegate.received(Message(Message.Ack, '', msg.receiver, msg.sender))
        else:
            self.delegate.received(msg)

