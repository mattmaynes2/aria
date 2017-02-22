import uuid
import logging
import soco
from adapter import Adapter
from device.sonos_device import SonosDevice
from ipc import Message

import sys

log=logging.getLogger(__name__)

class SonosAdapter (Adapter):
    def __init__(self):
        super().__init__()
        self.__devices={}

    def discover(self):
        devices=soco.discover()
        for device in devices:
            device=SonosDevice(device,self)
            self.__devices[device.address]=device
            self.notify('discovered',device)

    def send (self, message):
        pass

    def receive (self):
        return None
    
    def received (self,message):
        self.notify('received',message)