from unittest import TestCase
from unittest.mock import Mock
from unittest import mock
from ipc import Message
from brain.strategies.v1_strategy import V1Strategy
import uuid

class V1StrategyTest(TestCase):

    def setUp(self):
        id1=uuid.uuid4()
        self.testEvents= [{
                            'source': str(id1),
                            'attribute_name': 'Foo',
                            'parameter_name': 'Foo',
                            'value': '5',
                            'request_id': 2
                        }]
                        
        self.testDeviceEvent = Mock()
        self.testDeviceEvent.type = Message.Event
        self.testDeviceEvent.sender = uuid.uuid4().bytes
        self.testDeviceEvent.receiver = uuid.uuid4().bytes
        self.testDeviceEvent.data = { "event" : "device.event" }

    def test_strategy_should_return_no_decision_if_no_sessions_processed(self):
        strategy = V1Strategy()
        self.assertEqual([], strategy.decide(self.testDeviceEvent))
        

    def test_strategy_should_respond_with_set_message_for_any_device_event(self):
        strategy = V1Strategy()
        strategy.processSession(self.testEvents)
        self.assertEqual(strategy.decide(self.testDeviceEvent)[0].data["value"], 
                            [ { "name" : "Foo", "value" : '5'} ])
        