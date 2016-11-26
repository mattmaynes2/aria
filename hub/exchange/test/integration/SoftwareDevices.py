from unittest   import TestCase
from unittest import mock
from unittest.mock import Mock
from unittest.mock import patch
import unittest

from device     import Device
from delegate    import  Delegate
from ipc import Message
from adapter.software_adapter import SoftwareAdapter
from device.timer_device import TimerDevice
from hub import SoftwareDeviceFactory

import uuid
import time
from datetime import timedelta

class TestSoftwareDevices (TestCase):

    @unittest.skip("Slow test")    
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

    def test_software_device_controller_should_list_available_devices(self):
        # The device list should contain at least one device type with a name of "timer"
        self.assertTrue(SoftwareDeviceFactory.getAvailableDevices()[0].name == "timer")
