class Exchange ():

    def __init__ (self):
        self.comms = {}


    def register (self, device_type, comm):
        self.comms[device_type] = comm
        comm.setup(self)

    def message (device, message): pass
