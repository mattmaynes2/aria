from unittest import TestCase
from unittest.mock import Mock
from unittest import mock
import uuid
import sys
from ipc import Message


# This is nasty but saves time running tests because OpenZWave lib doesn't need to be built
sys.modules["openzwave"] = Mock()
sys.modules["pydispatch"] = Mock()
sys.modules["openzwave.node"] = Mock()
sys.modules["openzwave.node"] = Mock()
sys.modules["openzwave.value"] = Mock()
sys.modules["openzwave.scene"] = Mock()
sys.modules["openzwave.controller"] = Mock()
sys.modules["openzwave.network"] = Mock()
sys.modules["openzwave.option"] = Mock()

from adapter.zwave_adapter import ZWaveAdapter

class ZWaveAdapterTest(TestCase):

    def setUp(self):

        self.mockNode = Mock()
        self.mockNode.get_values.return_value = {}
        self.mockNode.name = "testdevice"
        self.mockNode.product_name = "testproduct"
        self.mockNode.manufacturer_name = "unittest"
        self.mockNode.version = 1
        self.associationGroup1 = Mock()
        associations = [1, 3]
        self.associationGroup1.associations = associations
        self.mockNode.groups = { "1" : self.associationGroup1 }
        self.mockNode.location = ""

        self.mockDevice = Mock()
        self.myUuid = uuid.uuid4()
        self.mockDevice.address = self.myUuid.bytes
        self.mockDevice.name = "testname"
        self.mockDevice.getName.return_value = "testname"
        self.mockDevice.getDeviceType.return_value = "testproduct"

        self.adapter = ZWaveAdapter()
        self.delegate = Mock()
        self.adapter.add_delegate(self.delegate)

    def test_adapter_removes_node_associations(self):
        '''
        Some ZWave devices attempt to control other nodes that they are associated with. This will
        interfere with the behaviour of our system; to prevent this we are currently removing all 
        associations between devices when they are discovered
        '''
        self.adapter._deviceDiscoveredCallback(node=self.mockNode)
        self.associationGroup1.remove_association.assert_called_once_with(3)

    @mock.patch("adapter.zwave_adapter.ZWaveDevice")
    def test_adapter_notifies_of_device_discovery(self, deviceModule):
        deviceModule.return_value = self.mockDevice
      
        self.adapter._deviceDiscoveredCallback(node=self.mockNode)
        discoveredDevice = self.delegate.discovered.call_args[0][0]
        self.assertEqual("testname", discoveredDevice.name)
        self.assertEqual(str(self.myUuid), self.mockNode.location)

    @mock.patch("adapter.zwave_adapter.ZWaveDevice")
    def test_adapter_notifies_of_device_events(self, deviceModule):
        deviceModule.return_value = self.mockDevice
        self.mockDevice.processEvent.return_value = { "event" : "device.event" }
        self.adapter._deviceDiscoveredCallback(node=self.mockNode)
        mockValue = Mock()
        self.adapter._nodeEventCallback(node=self.mockNode, value=mockValue)
        event = self.delegate.received.call_args[0][0]
        self.assertEqual(Message.Event, event.type)
        self.assertEqual({"event" : "device.event"}, event.data)
        self.assertEqual(self.myUuid.bytes, event.sender)
        self.assertEqual(Message.DEFAULT_ADDRESS, event.receiver)

    @mock.patch("adapter.zwave_adapter.ZWaveDevice")
    def test_adapter_ignores_events_from_undiscovered_devices(self, deviceModule):
        mockValue = Mock()
        self.adapter._nodeEventCallback(node=self.mockNode, value=mockValue)
        self.assertEqual(0, self.delegate.received.call_count)

    @mock.patch("adapter.zwave_adapter.ZWaveDevice")
    def test_adapter_sets_device_values_when_set_message_received(self, deviceModule):
        testMessage = Mock()
        testMessage.type = Message.Request
        testMessage.sender = bytes([0x00, 0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, 0x00, 0x00, 0x00, 0x00, 0x01])
        testMessage.receiver = self.mockDevice.address
        testMessage.data = { "set" : "Brightness", "value" : [ { "name" : "Brightness", "value" : 10} ] }
        deviceModule.return_value = self.mockDevice
        self.mockDevice.setValue.return_value = {"Brightness" : 100}
        self.adapter._deviceDiscoveredCallback(node=self.mockNode)
        self.adapter.send(testMessage)
        response = self.delegate.received.call_args[0][0]
        self.assertEqual("testname", response.data["device"])
        self.assertEqual("testproduct", response.data["deviceType"])
        self.assertEqual("Brightness", response.data["attribute"]["name"])
        self.assertEqual(100, response.data["attribute"]["parameters"][0]["Brightness"])
        self.assertEqual(Message.Response, response.type)
        self.assertEqual(testMessage.receiver, response.sender)
        self.assertEqual(testMessage.sender, response.receiver)
    
    @mock.patch("adapter.zwave_adapter.ZWaveDevice")
    def test_adapter_response_with_device_value_when_get_message_received(self, deviceModule):
        testMessage = Mock()
        testMessage.type = Message.Request
        testMessage.sender = bytes([0x00, 0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, 0x00, 0x00, 0x00, 0x00, 0x01])
        testMessage.receiver = self.mockDevice.address
        testMessage.data = { "get" : "Brightness" }
        deviceModule.return_value = self.mockDevice
        self.mockDevice.getValue.return_value = 10
        self.adapter._deviceDiscoveredCallback(node=self.mockNode)
        self.adapter.send(testMessage)
        response = self.delegate.received.call_args[0][0]
        self.assertEqual(Message.Response, response.type)
        self.assertEqual(10, response.data["value"])
        self.assertEqual("Brightness", response.data["response"])
        self.assertEqual(testMessage.receiver, response.sender)
        self.assertEqual(testMessage.sender, response.receiver)
   