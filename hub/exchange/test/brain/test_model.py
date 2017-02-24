from unittest import TestCase
from unittest.mock import Mock
from unittest import mock
from ipc import Message
from brain.model import Model

class ModelTest (TestCase):

    def setUp(self):
        self.stubAdapter = Mock()
    
        self.testDeviceEvent = Mock()
        self.testDeviceEvent.type = Message.Event
        self.testDeviceEvent.sender = bytes([0x00,0x01, 0x02,0x03,0x04,0x05,0x06,0x07,0x08,0x09,0x0a,0x0b, 0x0c, 0x0d, 0x0e, 0x0f])
        self.testDeviceEvent.receiver = bytes([0x01,0x01, 0x02,0x03,0x04,0x05,0x06,0x07,0x08,0x09,0x0a,0x0b, 0x0c, 0x0d, 0x0e, 0x0f])
        self.testDeviceEvent.data = { "event" : "device.event" }

        self.testNonDeviceEvent = Mock()
        self.testNonDeviceEvent.type = Message.Event
        self.testNonDeviceEvent.sender = bytes([0x00,0x01, 0x02,0x03,0x04,0x05,0x06,0x07,0x08,0x09,0x0a,0x0b, 0x0c, 0x0d, 0x0e, 0x0f])
        self.testNonDeviceEvent.receiver = bytes([0x01,0x01, 0x02,0x03,0x04,0x05,0x06,0x07,0x08,0x09,0x0a,0x0b, 0x0c, 0x0d, 0x0e, 0x0f])
        self.testNonDeviceEvent.data = { "event" : "boring.event" }

        self.testNonDeviceEvent = Mock()
        self.testNonDeviceEvent.type = Message.Event
        self.testNonDeviceEvent.sender = bytes([0x00,0x01, 0x02,0x03,0x04,0x05,0x06,0x07,0x08,0x09,0x0a,0x0b, 0x0c, 0x0d, 0x0e, 0x0f])
        self.testNonDeviceEvent.receiver = bytes([0x01,0x01, 0x02,0x03,0x04,0x05,0x06,0x07,0x08,0x09,0x0a,0x0b, 0x0c, 0x0d, 0x0e, 0x0f])
        self.testNonDeviceEvent.data = { "event" : "boring.event" }

        self.testNonEventMessage = Mock()
        self.testNonEventMessage.type = Message.Request
        self.testNonEventMessage.sender = bytes([0x00,0x01, 0x02,0x03,0x04,0x05,0x06,0x07,0x08,0x09,0x0a,0x0b, 0x0c, 0x0d, 0x0e, 0x0f])
        self.testNonEventMessage.receiver = bytes([0x01,0x01, 0x02,0x03,0x04,0x05,0x06,0x07,0x08,0x09,0x0a,0x0b, 0x0c, 0x0d, 0x0e, 0x0f])
        self.testNonEventMessage.data = {  }

    def test_model_should_send_response_from_learning_strategy(self):
        strategy = Mock()
        strategy.decide.return_value = "decision"
        model = Model(self.stubAdapter, strategy)
        model.received(self.testDeviceEvent)
        self.stubAdapter.send.assert_called_with("decision")

        
    def test_model_shold_not_attempt_to_forward_null_decision(self):
        strategy = Mock()
        strategy.decide.return_value = None
        model = Model(self.stubAdapter, strategy)
        model.received(self.testDeviceEvent)
        self.stubAdapter.send.assert_not_called()

    def test_model_should_not_respond_to_non_device_event_messages(self):
        strategy = Mock()
        model = Model(self.stubAdapter, strategy)
        model.received(self.testNonDeviceEvent)
        self.stubAdapter.send.asssert_not_called()

    def test_model_should_only_respond_to_event_messages(self):
        strategy = Mock()
        model = Model(self.stubAdapter, strategy)
        model.received(self.testNonEventMessage)
        self.stubAdapter.send.asssert_not_called()
        