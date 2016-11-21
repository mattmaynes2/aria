import uuid
import json
from unittest import TestCase
from device import Device, DeviceType,Attribute,DataType


class DeviceTest(TestCase):
    
    def setUp (self):
        self.id=uuid.uuid4()        
        self.dev=Device(DeviceType('WeMo Switch','wemo', maker='WeMo', \
        attributes=[Attribute('state',DataType.Binary)]), name= 'Lamp Switch', address=self.id.bytes,\
         version='0.1.0')
    
    def test_str(self):
        self.assertEqual('Device [name: Lamp Switch, DeviceType: <WeMo Switch>, address: '\
        +str(self.id)+', version: 0.1.0]',str(self.dev))
    
    def test_encode(self):
        expected='{"address": "'+str(self.id)+'", "name": "Lamp Switch", "type": {"attributes":\
        [{"dataType":}]}}'
        self.assertEqual(self.dev.to_json(), expected)