from unittest   import TestCase

from device     import Device
from adapter    import AriaAdapter, Message, Delegate

class AriaAdapterTest (TestCase):

    def setUp (self):
        self.adapter = AriaAdapter()

    def tearDown (self):
        self.adapter.teardown()

    def test_send (self):
        data    = { 'action' : 'status' }
        sender  = Device('')
        mock    = Delegate()

        self.adapter.add_delegate(mock)
        message = Message(Message.Request, data, sender.address, Message.DEFAULT_ADDRESS)
        mock.received = lambda msg: self.assertEqual(msg.data, data)

        self.adapter.send(message, ('localhost', self.adapter.port))
        self.adapter.start()
        self.adapter.teardown()
