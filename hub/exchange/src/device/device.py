import uuid
import json
from device import Attribute
class Device:

    def __init__ (self, device_type, name = '', address = None,version=''):
        self.name    = name
        self.address = address if address else uuid.uuid4().bytes
        self.version =version
        if isinstance(device_type, DeviceType):
            self.type = device_type
        else:
            raise TypeError('type must be a DeviceType')

        if (not isinstance(self.address,bytes)):
            raise TypeError("address needs to be of type bytes")

    def __str__(self):
        return 'Device [name: '+self.name+', DeviceType: <'+self.device_type.name+'>, address: '\
        +str(uuid.UUID(bytes=self.address))+', version:'+self.version+']'
    


    
    def to_json(self):
        return json.dumps(self,default=Device.json_encode,sort_keys=True)
    
    @staticmethod
    def json_encode(obj):
        if( isinstance(obj,(Device,DeviceType,Attribute))):
            return obj.__dict__
        if( isinstance(obj,bytes)):
            return str(uuid.UUID(bytes=obj))
        if( isinstance(obj,uuid.UUID)):
            return str(obj)
        raise TypeError("Unserializable object {} of type {}".format(obj, type(obj)))