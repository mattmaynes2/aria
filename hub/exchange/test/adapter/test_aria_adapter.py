from unittest   import TestCase
from unittest import mock
from unittest.mock import Mock
from unittest.mock import patch

from device     import Device
from adapter    import AriaAdapter, Message, Delegate

# Dependencies to mock: Thread, Socket

class AriaAdapterTest (TestCase):

    def setUp (self):
        self.adapter = AriaAdapter()

    def tearDown (self):
        self.adapter.teardown()

    ## Mocks socket functions: socket, socket.sendto, socket.close
    @mock.patch('socket.socket')
    def test_send (self, mock_sockets):
        data    = { 'action' : 'status' }
        sender = Device('');
        mockSocket = Mock()
        mock_sockets.return_value = mockSocket

        message = Message(Message.Request, data, sender.address, Message.DEFAULT_ADDRESS)
        self.adapter.send(message, ('localhost', self.adapter.port))
        mockSocket.sendto.assert_called_with(message.encode(), ('localhost', self.adapter.port))
        mockSocket.close.assert_called_with()

