from unittest   import TestCase
from unittest import mock
from unittest.mock import Mock
from unittest.mock import patch

from device     import Device
from delegate    import  Delegate
from ipc import Message
from adapter.software_adapter import SoftwareAdapter
from device.timer_device import TimerDevice

import uuid
import time
from datetime import timedelta

class TestSoftwareDevices (TestCase):

    def test_timer_should_fire_events(self):
        timer = TimerDevice(timedelta(seconds=2))
        adapter = SoftwareAdapter()

        mockDelegate = Mock()
        adapter.add_delegate(mockDelegate)
        adapter.add_device(timer)

        timer.start()
        time.sleep(7)
        timer.stop()
        self.assertEqual(mockDelegate.received.call_count, 3)

    def test_software_device_controller_should_list_devices(self):
        mockListener = Mock()
        message = Message()
        message.type = Message.Request
        message.data = { 'get' : 'deviceList' }

        controller = SoftwareDeviceController()
        controller.registerEventCallback(mockListener)
        controller.send(message)
        self.assertTrue(mockListener.called)
