from packet import Packet

class Ack (Packet):
    def __init__ (self, sender = '\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0'):
        super().__init__(1, sender)

