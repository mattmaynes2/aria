import uuid
from unittest import TestCase
from hub import Hub,HubMode
from device import Device, DeviceType, Attribute, DataType


class HubTest (TestCase):

    def setUp (self):
        self.hub = Hub()

    def test_status (self):
        status = self.hub.status()
        self.assertEqual(status['version']  , self.hub.version)
        self.assertEqual(status['mode']     , self.hub.mode.value)

    def test_command (self):
        self.assertEqual(self.hub.getCommand('status'), self.hub.status())
    
    def test_get_device(self):
        id=uuid.uuid4()        
        dev=Device(DeviceType('WeMo Switch','wemo', maker='WeMo', \
        attributes=[Attribute('state',DataType.Binary)]), name= 'Lamp Switch', address= id.bytes,\
         version='0.1.0')
        self.hub.addDevice(dev)
        expected='['+dev.to_json()+']'
        self.assertEqual(self.hub.getCommand('devices'), expected)
    
    def test_set_name(self):
        self.hub.setCommand('name','Test')
        self.assertEqual(self.hub.name,'Test')

    def test_set_mode(self):
        self.assertRaises(ValueError,self.hub.setCommand,'mode',3)
        self.hub.setCommand('mode',1)
        self.assertEqual(HubMode(1),self.hub.mode)