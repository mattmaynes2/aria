import json
import logging
import uuid
from .hub_mode  import HubMode
from device import Device
from database import DatabaseTranslator
from adapter import Message


log=logging.getLogger(__name__)

class Hub(Device):
    VERSION = '0.0.2'
    
    def __init__ (self, args = {}, exit = None):
        super().__init__('hub','Smart Hub',Message.DEFAULT_ADDRESS )
        self.version = Hub.VERSION
        self._devices = []
        self.mode    = HubMode.Normal
        self.exit    = exit if exit else lambda: None

    def getCommand (self, attribute):
        if attribute == 'status':
            return self.status()
        if attribute == 'devices':
            return self.getDevicesJson()
        if attribute == 'name':
            return self.name
        if attribute == 'mode':
            return self.mode.value

    def setCommand (self, attribute,value):
        if attribute == 'name':
            self.name=value
            return self.name
        if attribute == 'mode':
            self.setMode(value)
            return self.mode.value

    def status (self):
        return {
            'version'   : self.version,
            'mode'      : self.mode.value,
            'devices'   : len(self._devices)
        }
    
    def addDevice (self,device):
        log.debug('adding device '+str(device))
        self._devices.append(device)

    def getDevicesJson (self):
        data=json.dumps(self._devices,default=Device.json_encode, sort_keys=True)
        log.debug('sending device list '+ data)
        return data

<<<<<<< HEAD
=======
    def setMode(self,mode):
        self.mode=HubMode(mode)
>>>>>>> origin/sprint-3

