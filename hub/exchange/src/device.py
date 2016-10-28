class Device:

    default         = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

    def __init__ (self, type, name, address= default ):
        self.type=type
        self.name=name
        self.address=address
