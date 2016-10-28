class Exchange ():

    def __init__ (self):
        self.comms = {}
        self.devices = {}

    def register (self, device_type, comm):
        self.comms[device_type] = comm
        comm.setup(self)
        comm.start()

    def send (self, device, message):
        # TODO Log sending a message here
        if (device.type in self.comms):
            self.comms[device.type](message)

    def teardown (self):
        for comm in self.comms:
            self.comms[comm].teardown()

    def message (self, msg):
        # TODO Add thread synchronization
        # TODO Log a received message here
        if (msg.target in self.devices):
            self.send(msg)

    def discovered (self, device):
        # TODO Add thread synchronization
        self.devices[device.address] = device
