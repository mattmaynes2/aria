import json
import struct

class Message:
    TYPEOFFSET      = 1
    SIZEOFFSET      = 4
    SENDEROFFSET    = 20
    RECEIVEROFFSET  = 36

    default         = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

    def __init__(self, type_=0,data = {}, sender=default, receiver=default):
        self.type_      =type_
        self.data       = data
        self.sender     = sender
        self.receiver   = receiver

    def encode(self):
        data =json.dumps(self.data)

        return self.type_
        + len(data)
        + self.sender
        + self.receiver
        + json.dumps(self.data)


    @staticmethod
    def decode (msg):
        message             = Message()
        message.type_       = struct.unpack('B',msg[0 : Message.TYPEOFFSET])[0]
        message.length      = struct.unpack('I', msg[Message.TYPEOFFSET:Message.SIZEOFFSET])[0]
        message.sender      = msg[Message.SIZEOFFSET:Message.SENDEROFFSET]
        message.receiver    = msg[Message.SENDEROFFSET:Message.RECEIVEROFFSET]
        message.data        = json.loads(msg[Message.RECEIVEROFFSETL:])
        return message
