from unittest import TestCase
from hub import Hub

class HubTest (TestCase):

    def setUp (self):
        self.hub = Hub()

    def test_status (self):
        status = self.hub.status()
        self.assertEqual(status['version']  , self.hub.version)
        self.assertEqual(status['mode']     , str(self.hub.mode))

    def test_command (self):
        self.assertEqual(self.hub.command('status'), self.hub.status())
