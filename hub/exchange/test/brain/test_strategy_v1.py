from unittest import TestCase
from unittest.mock import Mock
from unittest import mock
from ipc import Message
from brain.strategies.v1_strategy import V1Strategy
import uuid

class V1StrategyTest(TestCase):

    def setUp(self):
        self.testRequest = Mock()
        self.testRequest = Message.Request
        self.testRequest = uuid.uuid4().bytes
        self.testRequest = uuid.uuid4().bytes
        self.testRequest = { "set" : "Brightness", "value" : [ { "name" : "Brightness", "value" : 10} ] }

        self.testDeviceEvent = Mock()
        self.testDeviceEvent.type = Message.Event
        self.testDeviceEvent.sender = uuid.uuid4().bytes
        self.testDeviceEvent.receiver = uuid.uuid4().bytes
        self.testDeviceEvent.data = { "event" : "device.event" }

    def test_strategy_should_respond_with_set_message_for_any_device_event(self):
        strategy = V1Strategy(self.testRequest)
        self.assertEqual(strategy.decide(self.testDeviceEvent)["value"], 
                            [ { "name" : "Brightness", "value" : 10} ])
        