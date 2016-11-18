import json
import logging
import uuid
from .hub_mode  import HubMode
from device import Device
from database import DatabaseTranslator

log=logging.getLogger(__name__)

class Hub:
    VERSION = '0.0.2'

    def __init__ (self, args = {}, exit = None):
        self.version = Hub.VERSION
        self._devices = []
        self.name    = 'My Hub'
        self.mode    = HubMode.Normal
        self.exit    = exit if exit else lambda: None
        self.dbTranslator = DatabaseTranslator()

    def command (self, action):
        if action == 'status':
            return self.status()
        if action == 'list_devices':
            return self.getDevicesJson()

    def status (self):
        return {
            'version'   : self.version,
            'mode'      : str(self.mode),
            'devices'   : len(self._devices)
        }
    
    def addDevice (self,device):
        log.debug('adding device '+str(device))
        self._devices.append(device)

    def getDevicesJson (self):
        data=json.dumps(self._devices,default=Device.json_encode, sort_keys=True)
        log.debug('sending device list '+ data)
        return data

    def processEvent (self, message):
        self.dbTranslator.processEvent(message)

