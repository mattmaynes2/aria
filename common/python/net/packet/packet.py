import uuid
import struct

class Packet:
    header      = 0
    body        = 38
    encoding    = 'utf-8'
    default     = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

    def __init__ (self, type_ = 0, sender = default):
        self.type       = type_
        self.length     = 0
        self.sender     = sender
        self.token      = Packet.default
        self.payload    = ''

    def size (self):
        return len(self.payload)

    def encode (self, payload = ''):
        if Packet.default == self.token:
            self.token = uuid.uuid1().bytes

        self.payload    = payload
        self.length     = self.size()
        return struct.pack('H', self.type)
        + struct.pack('I', self.length)
        + self.sender
        + self.token
        + payload

    @staticmethod
    def decode (msg, constructor = None):
        packet = Packet() if not constructor else constructor()

        packet.type     = struct.unpack('H', msg[0:2])[0]
        packet.length   = struct.unpack('I', msg[2:6])[0]
        packet.token    = msg[6:22]
        packet.sender   = msg[22:38]
        packet.payload  = msg[38:packet.length]
        return packet


