from unittest   import TestCase
from unittest import mock
from unittest.mock import Mock
from unittest.mock import patch

from device     import Device
from delegate    import  Delegate
from adapter.software_adapter import SoftwareAdapter
from ipc import Message
import uuid

class SoftwareAdapterTest (TestCase):

    def test_software_adapter_should_forward_message_from_device (self):
        mockDelegate = Mock()
        adapter = SoftwareAdapter()
        adapter.add_delegate(mockDelegate)
        uid = uuid.uuid4().bytes
        adapter.event(uid, {"value" : 12})
        message = mockDelegate.received.call_args[0][0]
        self.assertEqual(message.type, Message.Event)
        self.assertEqual(message.sender, uid)
        self.assertEqual(message.received, Message.DEFAULT_ADDRESS)
        self.assertEqual(message.data["value"], 12)

    def test_software_adapter_should_register_for_device_events (self):
        mockDevice = Mock()
        adapter = SoftwareAdapter()
        adapter.add_device(mockDevice)
        mockDevice.registerEventCallback.assert_called_with(adapter.event)