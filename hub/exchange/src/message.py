import json

class Message:
    OFFSET_SENDER       = 16
    OFFSET_RECEIVER     = 32
    default             = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

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
        message.sender      = msg[0:Message.OFFSET_SENDER]
        message.receiver    = msg[Message.OFFSET_SENDER:Message.OFFSET_RECEIVER]
        message.data        = json.loads(msg[Message.OFFSET_RECEIVERL:])
        return message
