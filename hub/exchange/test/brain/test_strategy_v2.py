from unittest import TestCase
from unittest.mock import Mock
from unittest import mock
from ipc import Message
from brain.strategies.v2_strategy import V2Strategy
import uuid

class V2StrategyTest(TestCase):

    def setUp(self):
        userActionId=uuid.uuid4()
        sensorId=uuid.uuid4()

        self.testEvents= [{
                            'source': str(sensorId),
                            'attribute_name': 'Bar',
                            'parameter_name': 'Foo',
                            'value': '5',
                            'request_id': None
                        },

                        {
                            'source': str(sensorId),
                            'attribute_name': 'FuBar',
                            'parameter_name': 'Foo',
                            'value': '10',
                            'request_id': None
                        },

                        {
                            'source': str(userActionId),
                            'attribute_name': 'Foo',
                            'parameter_name': 'Foo',
                            'value': '5',
                            'request_id': 2
                        }
                    ]

        self.testNonTriggeringEvent = Mock()
        self.testNonTriggeringEvent.type = Message.Event
        self.testNonTriggeringEvent.sender = uuid.uuid4().bytes
        self.testNonTriggeringEvent.receiver = uuid.uuid4().bytes
        self.testNonTriggeringEvent.data = {
                                                "event": "device.event",
                                                "attribute": {
                                                    "name": "Bar",
                                                    "parameters": [{
                                                        "name": "Foo",
                                                        "value": "10"
                                                    }]
                                                }
                                            }
                                                    
        self.testTriggeringEvent = Mock()
        self.testTriggeringEvent.type = Message.Event
        self.testTriggeringEvent.sender = sensorId.bytes
        self.testTriggeringEvent.receiver = uuid.uuid4().bytes
        self.testTriggeringEvent.data ={
                                            "event": "device.event",
                                            "attribute": {
                                                "name": "FuBar",
                                                "parameters": [{
                                                    "name": "Foo",
                                                    "value": "10"
                                                }]
                                            }
                                        }

    def test_strategy_should_return_no_decision_if_no_sessions_processed(self):
        strategy = V2Strategy()
        self.assertEqual([], strategy.decide(self.testTriggeringEvent))
        

    def test_strategy_should_respond_with_no_decision_if_event_did_not_precede_request(self):
        strategy = V2Strategy()
        strategy.processSession(self.testEvents)
        self.assertEqual([], strategy.decide(self.testNonTriggeringEvent))

    def test_strategy_should_respond_with_request_for_event_preceding_request_in_session(self):
        strategy = V2Strategy()
        strategy.processSession(self.testEvents)
        self.assertEqual(strategy.decide(self.testTriggeringEvent)[0].data["value"], 
                            [{
                                "name": "Foo",
                                "value": "5"
                            }])
        