from .hub_mode  import HubMode
import json

class Hub:
    VERSION = '0.0.2'

    def __init__ (self, args = {}, exit = None):
        self.version = Hub.VERSION
        self.devices = []
        self.name    = 'My Hub'
        self.mode    = HubMode.Normal
        self.exit    = exit if exit else lambda: None

    def command (self, action):
        if action == 'status':
            return self.status()
        if action == 'list_devices':
            return json.dumps(self.devices)

    def status (self):
        return {
            'version'   : self.version,
            'mode'      : str(self.mode),
            'devices'   : len(self.devices)
        }


