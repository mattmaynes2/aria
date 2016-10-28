import uuid
import struct

class Packet:
    header          = 0
    HEADEROFFSET    = 38
    TYPEOFFSET      = 2
    SIZEOFFSET      = 6
    SENDEROFFSET    = 22
    encoding        = 'utf-8'
    default         = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

    def __init__ (self, type_ = 0, sender = default, receiver=default):
        self.type       = type_
        self.length     = 0
        self.sender     = sender
        self.receiver   = receiver
        self.payload    = ''

    def size (self):
        return len(self.payload)

    def encode (self, payload = ''):
        if Packet.default == self.receiver:
            self.receiver = uuid.uuid1().bytes

        self.payload    = payload
        self.length     = self.size()
        return struct.pack('H', self.type)
        + struct.pack('I', self.length)
        + self.sender
        + self.receiver
        + payload

    @staticmethod
    def decode (msg, constructor = None):
        packet = Packet() if not constructor else constructor()

        packet.type     = struct.unpack('H', msg[0: Packet.TYPEOFFSET])[0]
        packet.length   = struct.unpack('I', msg[Packet.TYPEOFFSET:Packet.SIZEOFFSET])[0]
        packet.receiver    = msg[Packet.SIZEOFFSET:Packet.SENDEROFFSET]
        packet.sender   = msg[Packet.SENDEROFFSET:Packet.HEADEROFFSET]
        packet.payload  = msg[Packet.HEADEROFFSET:packet.length]
        return packet


