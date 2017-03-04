from unittest import TestCase
from unittest.mock import Mock
from unittest import mock
from ipc import Message
from brain.strategies.v3_strategy import V3Strategy
import uuid
from io import StringIO

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


    @mock.patch("builtins.open")
    def test_strategy_should_save_decisions_to_file(self, mock_open):
        testFile = StringIO()
        testFile.close = Mock()

        mock_open.return_value = testFile

        strategy = V3Strategy("testFile.dec")
        strategy.processSession(self.testEvents)
        strategy.save()

        testFile.seek(0)

        strategy2 = V3Strategy("testFile.dec")
        self.assertEqual(strategy2.decide(self.testTriggeringEvent)[0].data["value"], 
                            [{
                                "name": "Foo",
                                "value": "5"
                            }])
        


