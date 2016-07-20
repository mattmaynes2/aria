import struct

from enum   import Enum
from packet import Packet

class LogLevel (Enum):
    emergency   = 0x00
    fatal       = 0x01
    critical    = 0x02
    normal      = 0x03
    warning     = 0x04
    notice      = 0x05
    info        = 0x06
    debug       = 0x07
    unknown     = 0xff

class Log (Packet):

    def __init__ (self, level = LogLevel.unknown, message = '', sender = Packet.default):
        super().__init__(2, sender)
        self.level      = level
        self.message    = message

    def encode (self):
        return super().encode(
            struct.pack('H', self.level)
            + self.message.encode(Packet.encoding)
        )

    @staticmethod
    def decode (msg):
        log         = Packet.decode(msg, Log)
        log.level   = struct.unpack('H', log.payload[0:2])
        log.msg     = log.payload[2::].deocde(Packet.encoding)
        return log

