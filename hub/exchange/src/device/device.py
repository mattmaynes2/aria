import uuid
import json

class Device:

    def __init__ (self, type_, name = '', address = None):
        self.type    = type_
        self.name    = name
        self.address = address if address else uuid.uuid4().bytes
        if( not isinstance(self.address,bytes)):
            raise TypeError("address needs to be of type bytes")

    def __str__(self):
        return 'Device [type: '+str(self.type)+', name: '+self.name+', address: '+str(uuid.UUID(bytes=self.address))+']'
    


    
    def toJson(self):
        return json.dumps(self,default=json_encode,sort_keys=True)
    
    @staticmethod
    def json_encode(obj):
        if( isinstance(obj,Device)):
            return obj.__dict__
        if( isinstance(obj,bytes)):
            return str(uuid.UUID(bytes=obj))
        if( isinstance(obj,uuid.UUID)):
            return str(obj)
        raise TypeError("Unserializable object {} of type {}".format(obj, type(obj)))