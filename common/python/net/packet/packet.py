
class Packet:

    def __init__ (self, category, sender = '\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0'):
        self.category   = category
        self.size       = 0
        self.sender     = sender

    def encode (self, payload = ''):
        self.size = len(payload)
        size = ''.join(map(chr, to_vector(self.size)))
        return chr(self.category) + size + self.sender + payload

    @staticmethod
    def decode (msg):
        packet = Packet(ord(msg[:1]))
        packet.size     = to_scalar(list(map(ord, msg[1:5])))
        packet.sender   = msg[5:21]
        return packet

def to_vector (n, base = 16):
    if n >= base and 1 < base:
        return to_vector(n // base, base) + [n % base]
    return [n]

def to_scalar (v, base = 16):
    return sum([base ** i * v[len(v) - 1 - i] for i in range(len(v))])

