from packet import Packet
from data   import Data

class Request (Data):

    def __init__ (self, route = '', content = '',
                  format_ = '', sender = Packet.default):
        super().__init__(route, content, format_, 4, sender)

    @staticmethod
    def decode (msg):
        return Data.decode(msg, Request)
