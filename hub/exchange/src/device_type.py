from protocol import Protocol

class DeviceType:
    def __init__(self, name, communication= Protocol.WiFi ,input = False, maker= '', version='0.0'):
        self.name-name
        self.communication=communication
        self.input=input # is this device a sensor or controller
        self.maker=maker #who made the device
        self.version=version
