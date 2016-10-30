import uuid
from adapter import Adapter
from ouimeaux.environment import Environment
from ouimeaux.signals import discovered, receiver
from device import Device, DeviceType

class WemoAdapter (Adapter):

    def __init__(self):
        super().__init__()
        self.env=Environment()
        self.deviceUIds={}

    def setup(self,delegate):
        super().setup()
        self.env.start()
        self.env.wait()

    def discover(self):
        self.env.discover(2)
        return True

    @receiver(discovered)
    def discovered(self,sender, **kwargs):
        uid = uuid.uuid4()

        self.deviceNames[uid] = sender.name
        self.deviceUids[sender.name]=uid

        deviceType = DeviceType(sender.name, False, 'WeMo')
        device=Device(deviceType,sender.name,kwargs['address'])
        self.notify('discovered',device)

