from unittest   import TestCase
from unittest import mock
from unittest.mock import Mock
from unittest.mock import patch

from device     import Device
from adapter    import Message, Delegate
from adapter.software_adapter import SoftwareAdapter
from device.timer_device import TimerDevice
import uuid
import time
from datetime import timedelta

class TestSoftwareAdapterIntegrations (TestCase):

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