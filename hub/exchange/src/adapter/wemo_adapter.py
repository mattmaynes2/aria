import uuid
import logging
from adapter import Adapter

from device import Device, DeviceType
from adapter import Message
import threading
import sys

logging.basicConfig(level=logging.DEBUG)


class WemoAdapter (Adapter):

    OFF = 0
    ON  = 1

    def __init__(self):
        super().__init__()
        self._deviceUids={}
        self._deviceNames={}
        # setup call back when device is discovered
        # TODO move to Adapter
        self.shutdownCondition = threading.Condition()

    def setup(self):
        super().setup()
        

    def discover(self):
        return True

    def _discovered(self,sender, **kwargs):
        uid = uuid.uuid4().bytes

        self._deviceNames[uid] = sender.name
        self._deviceUids[sender.name]=uid
        print(sender)
        #deviceType = DeviceType(sender.name, False, 'WeMo')
        #hostname=sender.services['basicevent'].hostname.split(':')
        #address= (hostname[0],hostname[1])
        device=Device('wemo',sender.name,uid)
        self.notify('discovered',device)

    def send (self, message):
        print('looking for '+str(message.receiver))
        deviceName = self._deviceNames[message.receiver]
        print('found device with name '+deviceName)
        

        response = device.get_state()
        print('got device status '+str(response) )
        if device.get_state == WemoAdapter.OFF:
            response = 'OFF'
        elif device.get_state == WemoAdapter.ON:
            response == 'ON'
        else:
            response == 'ERROR'
            self.notify('received',Message(type_ = 3, data = { 'status' : response }, sender = message.receiver, receiver=message.sender))


    def receive(self,sender,**kwargs):
        print(sender.name+' has changed states new state is  :'+kwargs['state'])

    def subscibe(self, sender, **kwargs):
        print('subscription received ')
        print(sender.name)
        print(kwargs)

    def run(self):
        self.setup()


    def teardown(self):
        sys.exit(0)
        return True