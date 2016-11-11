import uuid
import logging
from adapter import Adapter
from netdisco.ssdpd import scan,RT_ROOTDEVICE
from device import Device, DeviceType
from adapter import Message
from pywemo.discovey import device_from_description
import threading
import sys

logging.basicConfig(level=logging.DEBUG)
log=logging.getLogger(__name__)

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
        devices=scan(RT_ROOTDEVICE)
        self._discovered(devices)
        return True

    def _discovered(self,devices):
        for discovered in devices:
            dev=device_from_description(discovered.location,None)
            uid = uuid.uuid4().bytes
            # TODO change to be upnp or devtype
            device=Device('wemo',dev.name,uid)
            log.debug('dicovered '+ str(device))
            self.notify('discovered',device)

    def send (self, message):
        log.debug('looking for '+str(message.receiver))
        deviceName = self._deviceNames[message.receiver]
        log.debug('found device with name '+deviceName)


        response = device.get_state()
        log.debug('got device status '+str(response) )
        if device.get_state == WemoAdapter.OFF:
            response = 'OFF'
        elif device.get_state == WemoAdapter.ON:
            response == 'ON'
        else:
            response == 'ERROR'
            self.notify('received',Message(type_ = 3, data = { 'status' : response }, sender = message.receiver, receiver=message.sender))


    def receive(self,sender,**kwargs):
        log.debug(sender.name+' has changed states new state is  :'+kwargs['state'])
        return True

    def subscibe(self, sender, **kwargs):
        log.debug('subscription received ')
        log.debug(sender.name)
        log.debug(kwargs)

    def run(self):
        self.setup()


    def teardown(self):
        self.netdisco.stop()
        return True
