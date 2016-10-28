import json

class Message:
    SENDEROFFSET    = 16
    RECEIVEROFFSET  = 32
    default         = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

    def __init__(self, data = {}, sender=default, receiver=default):
        self.data       = data
        self.sender     = sender
        self.receiver   = receiver

    def encode(self):
        return self.sender
        + self.receiver
        + json.dumps(self.data)

    @staticmethod
    def decode (msg):
        message             = Message()
        message.sender      = msg[0:Message.SENDEROFFSET]
        message.receiver    = msg[Message.SENDEROFFSET:Message.RECEIVEROFFSET]
        message.data        = json.loads(msg[Message.RECEIVEROFFSETL:])
        return message
