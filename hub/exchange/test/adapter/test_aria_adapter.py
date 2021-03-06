import uuid
from unittest   import TestCase
from unittest import mock
from unittest.mock import Mock
from unittest.mock import patch

from adapter    import AriaAdapter
from delegate import Delegate
from ipc import Message
import sys

# Dependencies to mock: Thread, Socket

class AriaAdapterTest (TestCase):

    ## Mocks socket functions: socket, socket.sendto, socket.close
    @mock.patch('socket.socket')
    def test_send (self, mock_sockets):
        adapter = AriaAdapter()
        data    = { 'action' : 'status' }
        id=uuid.uuid4().bytes
        mockSocket = Mock()
        mock_sockets.return_value = mockSocket

        message = Message(Message.Request, data, id, Message.DEFAULT_ADDRESS)
        adapter.send(message, ('localhost', adapter.port))
        mockSocket.sendto.assert_called_with(message.encode(), ('localhost', adapter.port))
        mockSocket.close.assert_called_with()

    @mock.patch('socket.socket')
    @mock.patch('select.select')
    def test_receive_request(self, mock_select, mock_sockets):
        mockSocket = Mock()
        mock_sockets.return_value = mockSocket
        mockSocket.fileno.return_value = 1
        mock_select.return_value = ([1],[],[])
        mockDelegate = Mock()
        id=uuid.uuid4().bytes
        adapter = AriaAdapter()

        adapter.add_delegate(mockDelegate)

        data    = {}
        
        responseData = Message(Message.Request, data, id, Message.DEFAULT_ADDRESS).encode()
        responseHost = ("127.0.0.1", "7000")
        mockSocket.recvfrom.return_value = (responseData, responseHost)

        adapter.receive()
        mockDelegate.received.assert_called_with(Message(Message.Request, data, id, Message.DEFAULT_ADDRESS))

    @mock.patch('socket.socket')
    @mock.patch('select.select')
    def test_receive_discover(self, mock_select, mock_sockets):
        mockSocket = Mock()
        mock_sockets.return_value = mockSocket
        mockSocket.fileno.return_value = 1
        mock_select.return_value = ([1],[],[])
        mockDelegate = Mock()

        adapter = AriaAdapter()

        adapter.add_delegate(mockDelegate)

        data    = {}
        id=uuid.uuid4().bytes
        responseData = Message(Message.Discover, data, id, Message.DEFAULT_ADDRESS).encode()
        responseHost = ("127.0.0.1", "7000")
        mockSocket.recvfrom.return_value = (responseData, responseHost)

        adapter.receive()
        discoveredDevice = mockDelegate.discovered.call_args
        discoveredMessage = mockDelegate.received.call_args
        self.assertEqual("aria", discoveredDevice[0][0].deviceType.protocol)
        self.assertEqual(Message.Ack, discoveredMessage[0][0].type)
        self.assertEqual(Message.DEFAULT_ADDRESS, discoveredMessage[0][0].sender)
        self.assertEqual(id, discoveredMessage[0][0].receiver)

    @mock.patch('socket.socket')
    def test_setup(self, mock_sockets):
        mockSocket = Mock()
        mock_sockets.return_value = mockSocket
        adapter = AriaAdapter()
        adapter.setup()
        mockSocket.bind.assert_called_with(("localhost", 7600))

    @mock.patch('socket.socket')
    @mock.patch('os.write')
    @mock.patch('os.pipe')
    def test_teardown(self, os_pipe, os_write, mock_sockets):
        os_pipe.return_value = (1,2)
        adapter = AriaAdapter()
        adapter.teardown()
        if not sys.platform.startswith('win32') :
            os_write.assert_called_with(2, bytes('x', 'utf-8'))

