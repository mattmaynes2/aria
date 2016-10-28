class Device:

    default = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

    def __init__ (self, name = '', address = default ):
        self.name    = name
        self.address = address
