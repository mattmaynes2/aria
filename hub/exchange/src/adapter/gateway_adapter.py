import socket
import os
import select
import logging

from .message import Message
from .adapter import Adapter

from device import Device, DeviceType

log = logging.getLogger(__name__)

class AriaAdapter (Adapter):
    BUFFER_SIZE = 4096
    PORT        = 7600
    HOST_NAME   = 'localhost'

    def __init__ (self):
        super().__init__()
        self.socket     = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.port       = AriaAdapter.PORT
        self._ip_map    = {}
        try:
            self.self_rd, self.self_wd = os.pipe()
        except OSError:
            log.warn("Unable to open self pipe, the server may not shut down properly")

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
        try:
            os.write(self.self_wd, bytes('x', 'utf-8'))
        except OSError:
            log.warn("Failed to write to self pipe, the server may not shut down properly")

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
        log.info('Aria adapter is listening')

        readables, writeables, exceptions = select.select([self.self_rd, self.socket.fileno()], [], [])
        if (self.socket.fileno() in readables):
            chunk, address = self.socket.recvfrom(AriaAdapter.BUFFER_SIZE)
            #while chunk:
            #   data.append(chunk)
            #   chunk = self.socket.recv(AriaAdapter.BUFFER_SIZE)
            #payload = ''.join(data)
            payload = chunk

            log.debug('Aria adapter received data on UDP socket')
            msg = Message.decode(payload)
            self._ip_map[msg.sender] = address

            if (msg.type == Message.Discover):
                # TODO need to find way to discover attributes of devices
                self.notify('discovered', Device(DeviceType('Default Aria Device','aria'), '', msg.sender))
                self.notify('received', Message(Message.Ack, '', msg.receiver, msg.sender))
            else:
                self.notify('received', msg)
        else:
            try:
                os.close(self.self_rd)
                os.close(self.self_wd)
                self.socket.close()
            except OSError:
                log.warn("Failed to close self-pipe")


        return True
