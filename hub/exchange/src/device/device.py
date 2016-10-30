import uuid

class Device:

    def __init__ (self, type_, name = '', address = None):
        self.type    = type_
        self.name    = name
        self.address = address if address else uuid.uuid4().bytes

    def __str__(self):
        return 'Device [type: '+str(self.type)+', name: '+self.name+', address: '+str(self.address)+']'
