import socket

from .message import Message
from .adapter import Adapter

from device import Device

class AriaAdapter (Adapter):
    BUFFER_SIZE = 4096
    PORT        = 7600
    HOST_NAME   = 'localhost'

    def __init__ (self):
        super().__init__()
        self.socket     = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.port       = AriaAdapter.PORT
        self._ip_map    = {}

    def setup (self ):
        super().setup()

        try:
            self.socket.bind((AriaAdapter.HOST_NAME, self.port))
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

        sock.sendto(msg.encode(), receiver)
        sock.close()

    def receive (self):
        data = []
        print('Listening')
        chunk, address = self.socket.recvfrom(AriaAdapter.BUFFER_SIZE)
        #while chunk:
        #   data.append(chunk)
        #   chunk = self.socket.recv(AriaAdapter.BUFFER_SIZE)
        #payload = ''.join(data)
        payload = chunk

        print('Received all data')
        msg = Message.decode(payload)
        self._ip_map[msg.sender] = address

        if (msg.type == Message.Discover):
            self.delegate.discovered(Device('aria', '', msg.sender))
            self.delegate.received(Message(Message.Ack, '', msg.receiver, msg.sender))
        else:
            self.delegate.received(msg)

