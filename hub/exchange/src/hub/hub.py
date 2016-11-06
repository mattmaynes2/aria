import json
import logging
from .hub_mode  import HubMode

log=logging.getLogger(__name__)

class Hub:
    VERSION = '0.0.2'

    def __init__ (self, args = {}, exit = None):
        self.version = Hub.VERSION
        self._devices = []
        self.name    = 'My Hub'
        self.mode    = HubMode.Normal
        self.exit    = exit if exit else lambda: None

    def command (self, action):
        if action == 'status':
            return self.status()
        if action == 'list_devices':
            log.debug('sending device list '+json.dumps(self._devices))
            return json.dumps(self._devices)

    def status (self):
        return {
            'version'   : self.version,
            'mode'      : str(self.mode),
            'devices'   : len(self._devices)
        }
    
    def addDevice(self,device):
        log.debug('adding device '+str(device))
        self._devices.append(device)



