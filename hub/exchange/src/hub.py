from hubmode import HubMode

class Hub:
    VERSION = '0.0.2'

    def __init__ (self):
        self.version = Hub.VERSION
        self.name = 'My Hub'
        self.mode = HubMode.Normal


    def status (self):
        return {
            'version'   : self.version,
            'mode'      : self.mode
        }
