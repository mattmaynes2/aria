import exchange
import cli

from hubmode import HubMode

class Hub:
    PORT = 7600
    VERSION = '0.0.2'

    def __init__ (self, args = {}):
        self.exchange = exchange.Exchange()
        self.version = Hub.VERSION
        self.name = 'My Hub'
        self.mode = HubMode.Normal

        self.exchange.port = args.port if args.port else Hub.PORT

        cli.CLI(self).start()

    def start (self):
        self.exchange.bind()

    def stop (self):
        self.exchange.release()

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


