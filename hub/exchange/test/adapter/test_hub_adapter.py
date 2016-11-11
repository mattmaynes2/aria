from unittest   import TestCase
from unittest import mock
from unittest.mock import Mock
from unittest.mock import patch

from device     import Device
from adapter    import HubAdapter, Message, Delegate

# Dependencies to mock: Thread, Socket

class HubAdapterTest (TestCase):

    def test_send_with_action(self):
        mockHub = Mock()
        adapter = HubAdapter(mockHub)
        data    = { 'action' : 'status' }
        sender = Device('')
        mockDelegate = Mock()

        callBackMsg = None
        def callBack(msg):
            callBackMsg = True
        mockDelegate.received.side_effect = callBack

        adapter.add_delegate(mockDelegate)
        mockHub.command.return_value = "testValue"

        message = Message(Message.Request, data, sender.address, Message.DEFAULT_ADDRESS)

        adapter.send(message)
        mockHub.command.assert_called_with(mock.ANY)
        mockDelegate.received.assert_called_with(mock.ANY)
