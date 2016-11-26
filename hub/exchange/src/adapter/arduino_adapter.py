import socket
import logging
import uuid

from device import Device

from ipc import Message
from .adapter import Adapter

logging.basicConfig(level=logging.DEBUG)
log=logging.getLogger(__name__)

class ArduinoAdapter (Adapter):
    BUFFER_SIZE = 1024

    def __init__ (self):
        super().__init__()
        self._socket    = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._ip_map    = {}

    def discover (self):
        uid = uuid.uuid4().bytes
        self.__ip_map[('192.168.1.50', 1260)] = uid

        dev = Device('arduino', 'light-sensor', uid)
        log.debug('Discovered ' + str(dev))
        self.notify('discovered', dev)

    def send (self, msg, address = None):
        if (address):
            receiver = address
        elif (msg.receiver in self._ip_map):
            receiver = self._ip_map[msg.receiver]
        else:
            raise NameError('Unknown receiver')

        log.debug('Sending ' + str(msg.data['data']) + ' to ' + str(receiver))
        self._socket.sendto(msg.data['data'], receiver)


        log.debug('Waiting for reply')
        data, address = self._socket.recvfrom(ArduinoAdapter.BUFFER_SIZE);

        log.debug('Got reply from socket')
        self.notify('received', Message(
            type_   = Message.Event,
            data    = { 'data' : data },
            sender  = self._ip_map[address]
        ));
