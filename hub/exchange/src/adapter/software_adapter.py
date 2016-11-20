from .message import Message
from .adapter import Adapter

class SoftwareAdapter(Adapter):
    """
    SoftwareAdapter allows the exchange to receive messages 
    from a software device (within the same process)
    """

    def __init__(self):
        super().__init__()

    def event(self, deviceUuid, deviceData): 
        message = Message()
        message.type = Message.Event
        message.sender = deviceUuid
        message.received = Message.DEFAULT_ADDRESS
        message.data = deviceData
        self.notify('received', message)

    def add_device(self, device):
        device.registerEventCallback(self.event)
        
