import uuid

from unittest   import TestCase
from unittest import mock
from unittest.mock import Mock
from unittest.mock import patch
from adapter    import HubAdapter
from delegate import Delegate
from ipc import Message

# Dependencies to mock: Thread, Socket

class HubAdapterTest (TestCase):

    def test_send_with_action(self):
        mockHub = Mock()
        adapter = HubAdapter(mockHub)
        data    = { 'action' : 'status' }
        mockDelegate = Mock()
        id= uuid.uuid4()
        adapter.add_delegate(mockDelegate)
        mockHub.command.return_value = "testValue"

        message = Message(Message.Request, data, id, Message.DEFAULT_ADDRESS)

        adapter.send(message)
        self.assertEqual(True, mockDelegate.received.called)

    def test_send_with_action(self):
        mockHub = Mock()
        adapter = HubAdapter(mockHub)
        data    = { }
        mockDelegate = Mock()
        id= uuid.uuid4()

        adapter.add_delegate(mockDelegate)
        message = Message(Message.Request, data, id, Message.DEFAULT_ADDRESS)

        adapter.send(message)
        self.assertEqual(False, mockDelegate.received.called)