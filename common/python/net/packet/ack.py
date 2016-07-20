from packet import Packet

class Ack (Packet):
    def __init__ (self, sender = Packet.default):
        super().__init__(1, sender)

