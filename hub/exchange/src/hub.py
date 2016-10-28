import exchange
import cli
import hub_comm
import native_comm

from hubmode import HubMode

class Hub:
    VERSION = '0.0.2'

    def __init__ (self, args = {}):
        self.exchange = exchange.Exchange()
        self.version = Hub.VERSION
        self.name = 'My Hub'
        self.mode = HubMode.Normal

        self.hub_comm = hub_comm.HubComm(self)

        cli.CLI(self).start()

    def start (self):
        # TODO change device type
        self.exchange.register('hub', self.hub_comm)
        self.exchange.register('native', native_comm.NativeComm())


    def stop (self):
        self.exchange.teardown()

    def command (self, action):
        if action == 'status':
            return self.status()

    def exit (self):
        print('Tearing down connections')
        # TODO teardown all connections
        self.stop()
        print('Complete')

    def status (self):
        return {
            'version'   : self.version,
            'mode'      : self.mode
        }


