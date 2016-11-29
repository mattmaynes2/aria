import uuid
import json
from device import Attribute, DeviceType
from enum import Enum
class Device:

    def __init__ (self, deviceType, name = '', address = None,version=''):
        self.name    = name
        self.address = address if address else uuid.uuid4().bytes
        self.version =version
        if isinstance(deviceType, DeviceType):
            self.deviceType = deviceType
        else:
            raise TypeError('type must be a DeviceType')

        if (not isinstance(self.address,bytes)):
            raise TypeError("address needs to be of type bytes")

    def __str__(self):
        return 'Device [name: '+self.name+', DeviceType: <'+self.deviceType.name+'>, address: '\
        +str(uuid.UUID(bytes=self.address))+', version: '+self.version+']'

    def getAttribute(self, attributeName):
        return self.deviceType.getAttribute(attributeName)
