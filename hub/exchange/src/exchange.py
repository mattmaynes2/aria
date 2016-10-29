from cli import CLI

class Exchange ():

    def __init__ (self, hub, cli):
        self._hub       = hub
        self._cli       = cli
        self._adapters  = {}
        self._devices   = {}

    def setup (self):
        for _, adapter in self._adapters.items():
            self._cli.log('Setting up adapter: ' + str(adapter), CLI.LEVEL_DEBUG)
            adapter.setup(self)

    def start (self):
        for _, adapter in self._adapters.items():
            self._cli.log('Starting adapter: ' + str(adapter), CLI.LEVEL_DEBUG)
            adapter.start()

    def register (self, device_type, adapter):
        self._cli.log('Registered adapter: ' + str(adapter), CLI.LEVEL_INFO)
        self._adapters[device_type] = adapter

    def send (self, device, message):
        # TODO Log sending a message here
        if (device.type in self._adapters):
            self._cli.log('Sending ' + str(message) + ' to device ' + str(device), CLI.LEVEL_INFO)
            self._adapters[device.type](message)

    def teardown (self):
        for _, adapter in self._adapters.items():
            self._cli.log('Tearing down adapter: ' + str(adapter), CLI.LEVEL_DEBUG)
            adapter.teardown()

    def received (self, message):
        # TODO Add thread synchronization
        # TODO Log a received message here
        if (message in self.devices):
            self._cli.log('Received ' + str(message), CLI.LEVEL_INFO)
            self.send(message)

    def discovered (self, device):
        # TODO Add thread synchronization
        self._cli.log('Discovered device: ' + str(device), CLI.LEVEL_INFO)
        self.devices[device.address] = device
        self._hub.append(device)
