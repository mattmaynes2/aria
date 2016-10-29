class Exchange ():

    def __init__ (self, hub):
        self._hub       = hub
        self._adapters  = {}
        self._devices   = {}

    def setup (self):
        for _, adapter in self._adapters.items():
            adapter.setup(self)

    def start (self):
        for _, adapter in self._adapters.items():
            adapter.start()

    def register (self, device_type, adapter):
        self._adapters[device_type] = adapter

    def send (self, device, message):
        # TODO Log sending a message here
        if (device.type in self._adapters):
            self._adapters[device.type](message)

    def teardown (self):
        for adapter in self._adapters:
            self._adapters[adapter].teardown()

    def received (self, message):
        # TODO Add thread synchronization
        # TODO Log a received message here
        if (message in self.devices):
            self.send(message)

    def discovered (self, device):
        # TODO Add thread synchronization
        self.devices[device.address] = device
        self._hub.append(device)
