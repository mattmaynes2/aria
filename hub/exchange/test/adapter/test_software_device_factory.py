import unittest
from unittest   import TestCase
from adapter import SoftwareDeviceFactory
from device import TimerDevice

class SoftwareDeviceFactoryTest(TestCase):

    def test_create_timer_device(self):
        factory = SoftwareDeviceFactory()
        deviceConfig = {"type": "timer", "period" : 1}

        device = factory.createDevice(deviceConfig)
        self.assertTrue(isinstance(device,TimerDevice))
        self.assertEqual(device.period, 1)

