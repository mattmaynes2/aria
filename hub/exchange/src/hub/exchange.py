from .cli import CLI
from adapter import Message

class Exchange ():

    def __init__ (self, hub, cli):
        self._hub       = hub
        self._cli       = cli
        self._adapters  = {}
        self._devices   = {}

    def start (self):
        for _, adapter in self._adapters.items():
            self._cli.log('Starting adapter: ' + str(adapter), CLI.LEVEL_DEBUG)
            adapter.start()

    def register (self, device_type, adapter):
        self._cli.log('Registered adapter: ' + str(adapter), CLI.LEVEL_INFO)
        adapter.add_delegate(self)
        self._adapters[device_type] = adapter

    def send (self, device, message):
        # TODO Log sending a message here
        if (device.type in self._adapters):
            self._cli.log('Sending ' + str(message) + ' to device ' + str(device), CLI.LEVEL_INFO)
            self._adapters[device.type].send(message)

    def teardown (self):
        for _, adapter in self._adapters.items():
            self._cli.log('Tearing down adapter: ' + str(adapter), CLI.LEVEL_DEBUG)
            adapter.teardown()

    def received (self, message):
        # TODO Add thread synchronization
        self._cli.log('Received ' + str(message) + ' from ' + str(message.sender), CLI.LEVEL_INFO)
        if( 'action' in message.data and message.data['action'] == 'discover'):
            self.send(self._devices[message.sender],Message(
                type_=Message.Ack,
                data={'success':'True'},
                receiver=message.sender))
            self.discoverDevices()
        elif (message.receiver in self._devices):
            self._cli.log('Routing message to ' + str(message.receiver), CLI.LEVEL_DEBUG)
            self.send(self._devices[message.receiver], message)

    def discoverDevices(self):
        for _, adapter in self._adapters.items():
            adapter.discover()

    def discovered (self, device):
        # TODO Add thread synchronization
        self._cli.log('Discovered device: ' + str(device.address), CLI.LEVEL_INFO)
        self._devices[device.address] = device
        # add device to hub
        self._hub.addDevice(device) 
