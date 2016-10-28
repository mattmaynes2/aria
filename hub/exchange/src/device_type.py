from protocol import Protocol

class DeviceType:
    def __init__(self, name, protocol = Protocol.WIFI,input = False, maker = '', version = '0.0.0'):
        self.name     = name
        self.protocol = protocol
        self.input    = input
        self.maker    = maker
        self.version  = version
