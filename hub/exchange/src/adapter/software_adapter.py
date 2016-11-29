from ipc import Message
from .adapter import Adapter

class SoftwareAdapter(Adapter):

    """
    SoftwareAdapter allows the exchange to receive messages 
    from a software device (within the same process)
    """
    def __init__(self):
        super().__init__()
        self.devices = {}

    def event(self, deviceUuid, deviceData): 
        message = Message()
        message.type = Message.Event
        message.sender = deviceUuid
        message.received = Message.DEFAULT_ADDRESS
        message.data = deviceData
        self.notify('received', message)

    def add_device(self, device):
        device.registerEventCallback(self.event)
        self.notify('discovered', device)
        self.devices[device.address] = device

    def send(self, message):
        if (message.sender in self.devices):
            raise KeyError("No software device exists at address: " + message.receiver)
        
        self.devices[message.sender].send(message)

    def teardown(self):
        super().teardown()
        for key, device in self.devices.items():
            device.stop()
            


