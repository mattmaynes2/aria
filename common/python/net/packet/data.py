from packet import Packet

class Data (Packet):

    def __init__ (self, route = '', content = '',
                  format_ = 'binary', type_ = 0, sender = Packet.default):
        super().__init__(type_, sender)
        self.route      = route
        self.content    = content
        self.format     = format_

    def encode (self):
        if str == type(self.content):
            content = self.content.encode(Packet.encoding)
        else:
            content = self.content

        return super().encode(
            self.route.encode(Packet.encoding)
            + b'\x00'
            + self.format.encode(Packet.encoding)
            + b'\x00'
            + content
        )

    @staticmethod
    def decode (msg, constructor = None):
        data = Packet.decode(msg, Data if constructor == None else constructor)

        parts = data.payload.split(b'\x00')
        data.route      = parts[0]
        data.format     = parts[1]
        data.content    = parts[2]
        return data
