import unittest
from unittest   import TestCase
from unittest.mock import patch
from unittest.mock   import Mock
from device import SoftwareDeviceFactory
from device import TimerDevice

class SoftwareDeviceFactoryTest(TestCase):

    @patch("device.timer_device.threading")
    def test_create_timer_device(self, mockThreading):
        SoftwareDeviceFactory.setDeviceListener(Mock())
        deviceConfig = {"name": "timer", "config" : {"period" : 1}}

        device = SoftwareDeviceFactory.create(deviceConfig)
        self.assertTrue(isinstance(device,TimerDevice))
        self.assertEqual(device.period, 1)

