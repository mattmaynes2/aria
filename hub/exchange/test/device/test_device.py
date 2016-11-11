import uuid
import json
from unittest import TestCase
from device import Device


class DeviceTest(TestCase):
    
    def setUp (self):
        self.id=uuid.uuid4()        
        self.dev=Device(type_='wemo', name= 'Switch', address=self.id.bytes)
    
    def test_str(self):
        self.assertEqual('Device [type: wemo, name: Switch, address: '+str(self.id)+']',str(self.dev))
    
    def test_encode(self):
        expected='{"address": "'+str(self.id)+'", "name": "Switch", "type": "wemo"}'
        self.assertEqual(self.dev.toJson(), expected)