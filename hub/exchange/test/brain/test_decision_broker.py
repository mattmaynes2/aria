from unittest import TestCase
from unittest.mock import Mock
from unittest import mock
from ipc import Message
from brain.decision_broker import DecisionBroker
import uuid

class DecisionBrokerTest (TestCase):

    def randomUuid(self):
        return uuid.uuid4().bytes

    def setUp(self):
        self.stubAdapter = Mock()
    
        self.testDeviceEvent = Mock()
        self.testDeviceEvent.type = Message.Event
        self.testDeviceEvent.sender = self.randomUuid()
        self.testDeviceEvent.receiver = self.randomUuid()
        self.testDeviceEvent.data = { "event" : "device.event" }

        self.testNonDeviceEvent = Mock()
        self.testNonDeviceEvent.type = Message.Event
        self.testNonDeviceEvent.sender = self.randomUuid()
        self.testNonDeviceEvent.receiver = self.randomUuid()
        self.testNonDeviceEvent.data = { "event" : "boring.event" }

        self.testNonDeviceEvent = Mock()
        self.testNonDeviceEvent.type = Message.Event
        self.testNonDeviceEvent.sender = self.randomUuid()
        self.testNonDeviceEvent.receiver =  self.randomUuid()
        self.testNonDeviceEvent.data = { "event" : "boring.event" }

        self.testNonEventMessage = Mock()
        self.testNonEventMessage.type = Message.Request
        self.testNonEventMessage.sender =  self.randomUuid()
        self.testNonEventMessage.receiver = self.randomUuid()
        self.testNonEventMessage.data = {  }
        
        self.mockHub=Mock()
        self.mockHub.isNormalMode.return_value=True

    def test_model_should_send_response_from_learning_strategy(self):
        strategy = Mock()
        mockDecision= Mock()
        strategy.decide.return_value =mockDecision
        model = DecisionBroker(self.stubAdapter, self.mockHub, strategy)
        model.received(self.testDeviceEvent)
        self.stubAdapter.received.assert_called_with(mockDecision)

        
    def test_model_should_not_attempt_to_forward_null_decision(self):
        strategy = Mock()
        strategy.decide.return_value = None
        model = DecisionBroker(self.stubAdapter, self.mockHub,strategy)
        model.received(self.testDeviceEvent)
        self.stubAdapter.received.assert_not_called()

    def test_model_should_not_respond_to_non_device_event_messages(self):
        strategy = Mock()
        model = DecisionBroker(self.stubAdapter,self.mockHub, strategy)
        model.received(self.testNonDeviceEvent)
        self.stubAdapter.received.assert_not_called()

    def test_model_should_only_respond_to_event_messages(self):
        strategy = Mock()
        model = DecisionBroker(self.stubAdapter, self.mockHub, strategy)
        model.received(self.testNonEventMessage)
        self.stubAdapter.received.assert_not_called()
    
    def test_dont_send_if_learning(self):
        strategy = Mock()
        mockDecision= Mock()
        strategy.decide.return_value =mockDecision
        self.mockHub.isNormalMode.return_value= False
        model = DecisionBroker(self.stubAdapter, self.mockHub, strategy)
        model.received(self.testDeviceEvent)
        self.stubAdapter.received.assert_not_called()
        