import json
import struct

from unittest import TestCase
from adapter import Message

class MessageTest (TestCase):

    def setUp (self):
        self.data = {
            'abc' : 123,
            'foo' : 'bar',
            'baz' : {
                'name' : 'tom',
                'game' : 'risk'
            }
        }

    def test_encode (self):
        m = Message(Message.Request, self.data)

        payload     = json.dumps(self.data).encode(Message.ENCODING)
        type_       = struct.pack('B', Message.Request)
        length      = struct.pack('I', len(payload))
        sender      = Message.DEFAULT_ADDRESS
        receiver    = Message.DEFAULT_ADDRESS
        
        expected = type_ + length + sender + receiver + payload
        print("EXPETED")
        self.assertEqual(m.encode(), expected)

    def test_decode (self):
        m = Message(Message.Request, self.data)

        self.assertEqual(Message.decode(m.encode()), m)



