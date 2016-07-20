from packet import Packet
from data   import Data

class Event (Data):

    def __init__ (self, route = '', content = '',
                  format_ = '', sender = Packet.default):
        super().__init__(route, content, format_, 6, sender)

    @staticmethod
    def decode (msg):
        return Data.decode(msg, Event)
