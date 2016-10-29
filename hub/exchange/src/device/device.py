class Device:
    default = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

    def __init__ (self, type_, name = '', address = default ):
        self.type    = type_
        self.name    = name
        self.address = address
