import uuid
import logging
from adapter import Adapter
from netdisco.ssdp import scan,ST_ROOTDEVICE
from device import Device, DeviceType
from adapter import Message
from pywemo.discovery import device_from_description
from pywemo.subscribe import SubscriptionRegistry
import threading
import sys

log=logging.getLogger(__name__)

class WemoAdapter (Adapter):

    def __init__(self):
        super().__init__()
        self._deviceUids={}
        self._deviceMac={}
        self._registry=SubscriptionRegistry()
        # setup call back when device is discovered
        # TODO move to Adapter
        self.shutdownCondition = threading.Condition()

    def setup(self):
        super().setup()
        self._registry.start()


    def discover(self):
        self._discovered(scan(ST_ROOTDEVICE))
        return True

    def _discovered(self,devices):
        for discovered in devices:
            dev=device_from_description(discovered.location,None)
            if(dev):
                self.processWeMo(dev)

    def processWeMo(self,dev):
        # add new device if we haven't discovered it before
        deviceMac = dev.basicevent.GetMacAddr()['MacAddr']
        if( not deviceMac in self._deviceMac):
            self._registry.register(dev)
            uid = uuid.uuid4().bytes
            # need to track associate mac with uid and uid with device 
            self._deviceMac[deviceMac]=uid
            self._deviceUids[uid]=dev
            # TODO change to be upnp or devicetype
            device=Device('wemo',dev.name,uid)
            self._registry.on(dev,None,self.subscribe)
            log.debug('discovered '+ str(device))
            self.notify('discovered',device) 
            
    def send (self, message):
        log.debug('looking for '+str(message.receiver))
        device = self._deviceUids[message.receiver]
        log.debug('found device with name '+device.name)
        # TODO need to add mapping for label:value pairs
        if(message.type == Message.Request):
            return self.handleRequest(message,device)
        log.warn("Don't know what to do with "+message)
        return False

    def handleRequest(self,message,device):
        if('set' in message.data):
            attribute=message.data['set']
            # TODO need a list of possible actions
            if('state' == attribute and 'value' in message.data):
                device.set_state(message.data['value'])
                return True
        elif('get' in message.data):
                self.notify('received',Message(
                    type_ = Message.Response, 
                    data = { 'response':'state' , 'value':device.get_state()}, 
                    sender = message.receiver))
                return True
        log.warn("Don't know what to do with "+str(message.data))
        return False

    def receive (self):
        return None
    def run(self):
        self.setup()


    def teardown(self):
        self._registry.stop()
        return True

    def subscribe(self,device,value):
        log.debug('got device status '+str(value) )
        mac=device.basicevent.GetMacAddr()['MacAddr']
        uid=self._deviceMac[mac]
        self.notify('received',Message(
            type_ = Message.Event, 
            data = { 'response':'state' , 'value':value }, 
            sender = uid)
            )
