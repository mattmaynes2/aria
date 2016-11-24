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
        self._push_back_ports= {}
        self.name = 'aria'
        self.pushBackAddress = None

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
            payload = chunk

            log.debug('Aria adapter received data on UDP socket')
            msg = Message.decode(payload)
            self._ip_map[msg.sender] = address

            if (msg.type == Message.Discover):
                device=self.buildDevice(msg.data,msg.sender) 
                # add the port to push back messages to
                if('port' in msg.data):
                    self.pushBackAddress=(address[0],msg.data['port'])
                   
                self.notify('discovered', device)
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
    
    def buildDevice(self,deviceData,deviceAddress):
        name='Default Aria Device'
        if('name' in deviceData):
            name=deviceData['name']
        return Device(DeviceType(name,self.name),name,deviceAddress)
    
    def pushBack(self,message):
        if(self.pushBackAddress):
            log.debug('Pushing '+str(message)+' to '+ pushBackAddress)
            self.send(message,self.pushBackAddress)
        else:
            log.warn("I don't Have an address to push messages to")


    def discovered(self, device):
        data={'event':'device.discovered', 'data':device.to_json()}
        msg = Message(Message.Event,data)
        self.adapter.pushBack(msg)


        

