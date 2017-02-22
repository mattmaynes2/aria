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
        if message.type == Message.Request:
            if message.receiver in self.__devices:
                device =self.__devices[message.receiver]
                if 'set' in message.data:
                    self.notify('received', Message( 
                            Message.Response,
                            data=self.setDeviceValue(message.data,device),
                            sender=device.address,
                            receiver=message.sender
                        ))
                    return True
            else:
                raise ValueError('Invalid receiver {}'.format(message.receiver))

    def receive (self):
        return None
    
    def received (self,message):
        self.notify('received',message)

    def setDeviceValue(self, request, device):
        attributeName = request["set"]
        value = request["value"]
        paramChanges =  []
        for param in value:
            change = device.handleRequest(param["name"], param["value"])  
            paramChanges.append(change)
        response = {
	    "device" : device.name,
	    "deviceType" : device.deviceType.name,
	    "attribute" : {
	        "name" : attributeName,
	        "parameters" : paramChanges
            }
        }
        return response