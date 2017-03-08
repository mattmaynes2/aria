import json
import struct
from enum import Enum
from uuid import UUID
from device import Device,DeviceType,Attribute, Parameter
import threading
import logging

logger = logging.getLogger(__name__)

class Message:
    Error               = 0
    Discover            = 1
    Request             = 2
    Event               = 3
    Ack                 = 4
    Response            = 5
    OFFSET_TYPE         = 1
    OFFSET_SIZE         = 5
    OFFSET_SENDER       = 21
    OFFSET_RECEIVER     = 37
    ENCODING            = 'utf-8'
    DEFAULT_ADDRESS     = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

    def __init__(self,
                 type_= Request,
                 data = {},
                 sender = DEFAULT_ADDRESS,
                 receiver = DEFAULT_ADDRESS
                 ):

        self.type       = type_
        self.data       = data
        self.sender     = sender
        self.receiver   = receiver

    def encode(self):
        data    = json.dumps(self.data,default=Message.json_encode,sort_keys=True).encode(Message.ENCODING)
        type_   = struct.pack('B', self.type)
        length  = struct.pack('I', len(data))

        return type_ + length + self.sender + self.receiver + data

    def __eq__ (self, other):
        return Message      == type(other)      and \
            self.type       == other.type       and \
            self.sender     == other.sender     and \
            self.receiver   == other.receiver

    @staticmethod
    def decode (msg):
        msg = msg.encode(Message.ENCODING) if str == type(msg) else msg
        message             = Message()
        message.type        = struct.unpack('B',msg[0 : Message.OFFSET_TYPE])[0]
        message.length      = struct.unpack('I', msg[Message.OFFSET_TYPE:Message.OFFSET_SIZE])[0]
        message.sender      = msg[Message.OFFSET_SIZE:Message.OFFSET_SENDER]
        message.receiver    = msg[Message.OFFSET_SENDER:Message.OFFSET_RECEIVER]
        message.data        = json.loads(msg[Message.OFFSET_RECEIVER:].decode(Message.ENCODING))

        return message

    @staticmethod
    def encode_to_json(self):
        return '{"type":"'+str(self.type)+'", "data":'+str(json.dumps(self.data,default=Message.json_encode,sort_keys=True))+', "sender":"'+\
        str(UUID(bytes=self.sender))+ '", "receiver": "'+str(UUID(bytes=self.receiver))+'"}'

    @staticmethod
    def decode_from_json(string):
        dictionary = json.loads(string)
        message = Message()
        message.type = dictionary["type"]
        message.sender = dictionary["sender"]
        message.receiver = dictionary["receiver"]
        message.data = dictionary["data"]
        return message

    def __str__(self):
        return 'Message [ type:'+str(self.type)+', data:'+str(json.dumps(self.data,default=Message.json_encode,sort_keys=True).encode(Message.ENCODING))+', sender:'+\
        str(UUID(bytes=self.sender))+ ', receiver: '+str(UUID(bytes=self.receiver))+']'
    
    @staticmethod
    def json_encode(obj):
        if( isinstance(obj,(Device,DeviceType,Attribute,Parameter))):
            return {key.lstrip('_'): value for key, value in obj.__dict__.items()}
        if(isinstance(obj,Enum)):
            return str(obj.value)
        if( isinstance(obj,bytes)):
            return str(UUID(bytes=obj))
        if( isinstance(obj,UUID)):
            return str(obj)
        if (isinstance(obj, type(threading.Lock()))):
            return str(obj)
        if (isinstance(obj, threading.Condition)):
            return str(obj)
        if (isinstance(obj, threading.Thread)):
            return str(obj)
        else:
            return