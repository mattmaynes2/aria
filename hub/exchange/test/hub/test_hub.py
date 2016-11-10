import uuid
from unittest import TestCase
from hub import Hub
from device import Device


class HubTest (TestCase):

    def setUp (self):
        self.hub = Hub()

    def test_status (self):
        status = self.hub.status()
        self.assertEqual(status['version']  , self.hub.version)
        self.assertEqual(status['mode']     , str(self.hub.mode))

    def test_command (self):
        self.assertEqual(self.hub.command('status'), self.hub.status())
    
    def test_list_device(self):
        id=uuid.uuid4()        
        dev=Device(type_='wemo', name= 'Switch', address=id.bytes)
        self.hub.addDevice(dev)
        expected='[{"address": "'+str(id)+'", "name": "Switch", "type": "wemo"}]'
        self.assertEqual(self.hub.command('list_devices'), expected)