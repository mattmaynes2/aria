class packet:

    def __init__ (self, category):
        self.category   = category
        self.size       = 0
        self.sender     = '\0\0\0\0\0\0\0\0\0\0\0\0'

    def encode (self, payload = ''):
        self.size = len(payload)
        return chr(self.category) + chr(self.size) + self.sender + payload

    def decode (self, msg):
        self.category = ord(msg[:1])
