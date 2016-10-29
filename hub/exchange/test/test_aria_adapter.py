from unittest   import TestCase

from device     import Device
from adapter    import AriaAdapter, Message, Delegate

class AriaAdapterTest (TestCase):

    def setUp (self):
        self.adapter = AriaAdapter()
        self.adapter.setup(self)

    def tearDown (self):
        self.adapter.teardown()

    def test_send (self):
        data    = { 'action' : 'status' }
        sender  = Device('')
        mock    = Delegate()

        message = Message(Message.Request, data, sender.address, Message.default)
        mock.received = lambda msg: self.assertEqual(msg.data, data)

        self.adapter.send(message, ('localhost', self.adapter.port))
        self.adapter.start()
        self.adapter.teardown()
