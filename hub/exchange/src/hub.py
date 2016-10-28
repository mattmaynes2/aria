import thread
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

        thread.start_new_thread(cli.CLI, (self))

    def start (self):
        self.exchange.bind()

    def stop (self):
        self.exchange.release()

    def command (self, action):
        pass

    def status (self):
        return {
            'version'   : self.version,
            'mode'      : self.mode
        }


