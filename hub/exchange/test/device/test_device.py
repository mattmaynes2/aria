import uuid
import json
from unittest import TestCase
from device import Device, DeviceType,Attribute,DataType,Parameter
from ipc import Message


class DeviceTest(TestCase):
    
    def setUp (self):
        self.maxDiff=None
        self.id=uuid.uuid4()        
        self.dev=Device(DeviceType('WeMo Switch','wemo', maker='WeMo', \
        attributes=[Attribute('state',[Parameter('state',DataType.Binary)])]), name= 'Lamp Switch',\
        address=self.id.bytes,version='0.1.0')
    
    def test_str(self):
        self.assertEqual('Device [name: Lamp Switch, DeviceType: <WeMo Switch>, address: '\
        +str(self.id)+', version: 0.1.0]',str(self.dev))
    
    def test_encode(self):
        expected='{"address": "'+str(self.id)+'", "deviceType": {"attributes":'\
        +' [{"isControllable": true, "name": "state", "parameters": [{"dataType": "binary",' \
        +' "max": null, "min": null, "name": "state", "step": null, "value": null}]}]'\
        +', "maker": "WeMo", "name": "WeMo Switch", "protocol": "wemo"},'\
        +' "icon": null, "name": "Lamp Switch", "version": "0.1.0"}'
        self.assertEqual(json.dumps(self.dev,default=Message.json_encode,sort_keys=True), expected)