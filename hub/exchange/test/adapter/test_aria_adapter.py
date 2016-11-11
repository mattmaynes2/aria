from unittest   import TestCase
from unittest import mock
from unittest.mock import Mock
from unittest.mock import patch

from device     import Device
from adapter    import AriaAdapter, Message, Delegate

# Dependencies to mock: Thread, Socket

class AriaAdapterTest (TestCase):

    ## Mocks socket functions: socket, socket.sendto, socket.close
    @mock.patch('socket.socket')
    def test_send (self, mock_sockets):
        adapter = AriaAdapter()
        data    = { 'action' : 'status' }
        sender = Device('');
        mockSocket = Mock()
        mock_sockets.return_value = mockSocket

        message = Message(Message.Request, data, sender.address, Message.DEFAULT_ADDRESS)
        adapter.send(message, ('localhost', adapter.port))
        mockSocket.sendto.assert_called_with(message.encode(), ('localhost', adapter.port))
        mockSocket.close.assert_called_with()

    @mock.patch('socket.socket')
    def test_receive_request(self, mock_sockets):
        mockSocket = Mock()
        mock_sockets.return_value = mockSocket
        mockDelegate = Mock()

        adapter = AriaAdapter()

        adapter.add_delegate(mockDelegate)

        data    = {}
        sender = Device(''); 
        responseData = Message(Message.Request, data, sender.address, Message.DEFAULT_ADDRESS).encode()
        responseHost = ("127.0.0.1", "7000")
        mockSocket.recvfrom.return_value = (responseData, responseHost)

        adapter.receive()
        mockDelegate.received.assert_called_with(Message(Message.Request, data, sender.address, Message.DEFAULT_ADDRESS))

    @mock.patch('socket.socket')
    def test_receive_discover(self, mock_sockets):
        mockSocket = Mock()
        mock_sockets.return_value = mockSocket
        mockDelegate = Mock()

        adapter = AriaAdapter()

        adapter.add_delegate(mockDelegate)

        data    = {}
        sender = Device(''); 
        responseData = Message(Message.Discover, data, sender.address, Message.DEFAULT_ADDRESS).encode()
        responseHost = ("127.0.0.1", "7000")
        mockSocket.recvfrom.return_value = (responseData, responseHost)

        adapter.receive()
        self.assertEqual(True, mockDelegate.discovered.called)
        self.assertEqual(True, mockDelegate.received.called)
        
    @mock.patch('socket.socket')
    def test_setup(self, mock_sockets):
        mockSocket = Mock()
        mock_sockets.return_value = mockSocket
        adapter = AriaAdapter()
        adapter.setup()
        mockSocket.bind.assert_called_with(("localhost", 7600))

    @mock.patch('socket.socket')
    def test_teardown(self, mock_sockets):
        mockSocket = Mock()
        mock_sockets.return_value = mockSocket
        adapter = AriaAdapter()
        adapter.teardown()
        mockSocket.close.assert_called_with()
