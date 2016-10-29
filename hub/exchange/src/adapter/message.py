import json
import struct

class Message:
    Error               = 0
    Discover            = 1
    Request             = 2
    Event               = 3
    Ack                 = 4
    OFFSET_TYPE         = 1
    OFFSET_SIZE         = 5
    OFFSET_SENDER       = 21
    OFFSET_RECEIVER     = 37
    encoding            = 'utf-8'
    default             = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

    def __init__(self, type_= 0, data = {}, sender = default, receiver = default):
        self.type       = type_
        self.data       = data
        self.sender     = sender
        self.receiver   = receiver

    def encode(self):
        data = json.dumps(self.data).encode(Message.encoding)

        return struct.pack('B', self.type) + struct.pack('I', len(data)) + self.sender + self.receiver + data


    @staticmethod
    def decode (msg):
        msg = msg.encode(Message.encoding) if str == type(msg) else msg
        message             = Message()
        message.type        = struct.unpack('B',msg[0 : Message.OFFSET_TYPE])[0]
        message.length      = struct.unpack('I', msg[Message.OFFSET_TYPE:Message.OFFSET_SIZE])[0]
        message.sender      = msg[Message.OFFSET_SIZE:Message.OFFSET_SENDER]
        message.receiver    = msg[Message.OFFSET_SENDER:Message.OFFSET_RECEIVER]
        message.data        = json.loads(msg[Message.OFFSET_RECEIVER:].decode(Message.encoding))

        return message
