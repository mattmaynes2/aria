import uuid
from unittest.mock import Mock,patch
from unittest import TestCase
from hub import Hub,HubMode
from hub.commands import CommandType
from device import Device, DeviceType, Attribute, DataType, Parameter
from database import Database


class HubTest (TestCase):

    def setUp (self):
        self.hub = Hub()

    def test_status (self):
        status = self.hub.status
        self.assertEqual(status['version']  , self.hub.version)
        self.assertEqual(status['mode']     , self.hub.mode.value)

    def test_command (self):
        self.assertEqual(self.hub.executeCommand(CommandType.GET,{'get':'status'}), self.hub.status)
    
    def test_get_device(self):
        id=uuid.uuid4()        
        dev=Device(DeviceType('WeMo Switch','wemo', maker='WeMo', \
        attributes=[Attribute('state',parameters=[Parameter('state',DataType.Binary)])]), \
        name = 'Lamp Switch', address= id.bytes,version='0.1.0')
        self.hub.addDevice(dev)
        expected=[dev]
        self.assertEqual(self.hub.executeCommand(CommandType.GET,{'get':'devices'}), expected)
    
    def test_set_name(self):
        self.hub.executeCommand(CommandType.SET,{'set':'name','value':'Test'})
        self.assertEqual(self.hub.name,'Test')

    def test_set_mode(self):
        self.assertRaises(ValueError,self.hub.executeCommand,\
        CommandType.SET,{'set':'mode', 'value':3})
        self.assertEqual(1,self.hub.executeCommand( CommandType.SET,{'set':'mode', 'value':1}))
        self.assertEqual(HubMode(1),self.hub.mode)

    
    def test_create_behaviour(self):
        mockCommand=Mock()
        mockCommand.execute.return_value=1;
        mockCommand.commandType=CommandType.CREATE
        mockCommand.name='behaviour'
        self.hub.addCommand(mockCommand)
        self.assertEqual(1,self.hub.executeCommand(CommandType.CREATE,\
        {'create':'behaviour', 'value':{'name':'lights on'}}))
