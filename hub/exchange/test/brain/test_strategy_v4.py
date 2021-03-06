from unittest import TestCase
from unittest.mock import Mock
from unittest import mock
from ipc import Message
from brain.strategies import V4Strategy
import uuid
from io import StringIO
import os


class V4StrategyTest(TestCase):

    def setUp(self):
        self.userActionId = uuid.uuid4()
        self.sensorId = uuid.uuid4()

        self.testEvents = [{
            'source': str(self.sensorId),
            'attribute_name': 'Bar',
            'parameter_name': 'Foo',
            'value': '5',
            'request_id': None,
            'behaviour_id': 1
        },

            {
            'source': str(self.sensorId),
            'attribute_name': 'Bar',
            'parameter_name': 'Foo',
            'value': '5',
            'request_id': None,
            'behaviour_id': 1
        },

            {
            'source': str(self.sensorId),
            'attribute_name': 'FuBar',
            'parameter_name': 'Foo',
            'value': '5',
            'request_id': None,
            'behaviour_id': 1
        },

            {
            'source': str(self.sensorId),
            'attribute_name': 'Bar',
            'parameter_name': 'Foo',
            'value': '8',
            'request_id': None,
            'behaviour_id': 1
        },
            {
            'source': str(self.sensorId),
            'attribute_name': 'Bar',
            'parameter_name': 'Foo',
            'value': '5',
            'request_id': None,
            'behaviour_id': 1
        },

            {
            'source': str(self.sensorId),
            'attribute_name': 'FuBar',
            'parameter_name': 'Foo',
            'value': '10',
            'request_id': None,
            'behaviour_id': 1
        },

            {
            'source': str(self.sensorId),
            'attribute_name': 'Bar',
            'parameter_name': 'Foo',
            'value': '8',
            'request_id': None,
            'behaviour_id': 1
        },

            {
            'source': str(self.userActionId),
            'attribute_name': 'Foo',
            'parameter_name': 'Foo',
            'value': '5',
            'request_id': 2,
            'behaviour_id': 1
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
                    "value": "8"
                }]
            }
        }

        self.testTriggeringEvent = Mock()
        self.testTriggeringEvent.type = Message.Event
        self.testTriggeringEvent.sender = self.sensorId.bytes
        self.testTriggeringEvent.receiver = uuid.uuid4().bytes
        self.testTriggeringEvent.data = {
            "event": "device.event",
            "attribute": {
                "name": "FuBar",
                "parameters": [{
                    "name": "Foo",
                    "value": "10"
                }]
            }
        }
        self.testState = {
            str(self.sensorId): {
                "attributes": [
                    {
                        "name": "FuBar",
                        "parameters": [
                            {
                                "name": "Foo",
                                "value": '1'
                            }
                        ]
                    },
                    {
                        "name": "Bar",
                        "parameters": [
                            {
                                "name": "Foo",
                                "value": '2'
                            }
                        ]
                    }
                ]
            }
        }

    def test_processSession(self):
        strategy = V4Strategy("v4.json")
        state = self.testState.copy()
        strategy.processSession(self.testEvents, state)
        eventMap = strategy.eventMapping
        self.assertEqual(strategy.decide(self.testTriggeringEvent)[0].data["value"],
                         [{
                             "name": "Foo",
                             "value": "5"
                         }])
        self.testTriggeringEvent.data['attribute']['parameters'][0]['value'] = '5'
        self.assertEqual(strategy.decide(self.testTriggeringEvent)[0].data["value"],
                         [{
                             "name": "Foo",
                             "value": "5"
                         }])
        self.assertEqual(strategy.decide(self.testNonTriggeringEvent), [])

        session2 = [{
            'source': str(self.sensorId),
            'attribute_name': 'Bar',
            'parameter_name': 'Foo',
            'value': '5',
            'request_id': None,
            'behaviour_id': 1
        }, {
            'source': str(self.sensorId),
            'attribute_name': 'FuBar',
            'parameter_name': 'Foo',
            'value': '5',
            'request_id': None,
            'behaviour_id': 1
        },

            {
            'source': str(self.sensorId),
            'attribute_name': 'Bar',
            'parameter_name': 'Foo',
            'value': '8',
            'request_id': None,
            'behaviour_id': 1
        },
            {
            'source': str(self.sensorId),
            'attribute_name': 'Bar',
            'parameter_name': 'Foo',
            'value': '5',
            'request_id': None,
            'behaviour_id': 1
        },
            {
            'source': str(self.sensorId),
            'attribute_name': 'Bar',
            'parameter_name': 'Foo',
            'value': '8',
            'request_id': None,
            'behaviour_id': 1
        },
            {
            'source': str(self.sensorId),
            'attribute_name': 'Bar',
            'parameter_name': 'Foo',
            'value': '5',
            'request_id': None,
            'behaviour_id': 1
        },

            {
            'source': str(self.sensorId),
            'attribute_name': 'FuBar',
            'parameter_name': 'Foo',
            'value': '10',
            'request_id': None,
            'behaviour_id': 1
        },

            {
            'source': str(self.sensorId),
            'attribute_name': 'Bar',
            'parameter_name': 'Foo',
            'value': '8',
            'request_id': None,
            'behaviour_id': 1
        },

            {
            'source': str(self.userActionId),
            'attribute_name': 'Foo',
            'parameter_name': 'Foo',
            'value': '5',
            'request_id': 2,
            'behaviour_id': 1
        },
            {
            'source': str(self.sensorId),
            'attribute_name': 'Bar',
            'parameter_name': 'Foo',
            'value': '5',
            'request_id': None,
            'behaviour_id': 1
        },
            {
            'source': str(self.userActionId),
            'attribute_name': 'Foo',
            'parameter_name': 'Foo',
            'value': '5',
            'request_id': 3,
            'behaviour_id': 1
        }]

        strategy.processSession(session2, self.testState)
        self.testTriggeringEvent.data['attribute']['parameters'][0]['value'] = '10'
        self.assertEqual(strategy.decide(self.testTriggeringEvent)[0].data["value"],
                         [{
                             "name": "Foo",
                             "value": "5"
                         }])

        mapping = strategy.eventMapping
        eventString = strategy.buildEventIdentifierFromMessage(
            self.testTriggeringEvent)
        row = mapping.table[eventString]
        self.assertEqual(2, row.getCount(1))
        self.assertEqual(3, row.decisions[0].count)

        # After the second training session Foobar =5  shouldn't trigger an
        # event
        self.testTriggeringEvent.data['attribute']['parameters'][0]['value'] = '5'
        eventString = strategy.buildEventIdentifierFromMessage(
            self.testTriggeringEvent)
        row = mapping.table[eventString]
        self.assertEqual(strategy.decide(self.testTriggeringEvent), [])

        # test save and reload
        strategy.save()
        strategy.eventMapping = {}
        strategy.load()

        self.testTriggeringEvent.data['attribute']['parameters'][0]['value'] = '10'
        self.assertEqual(strategy.decide(self.testTriggeringEvent)[0].data["value"],
                         [{
                             "name": "Foo",
                             "value": "5"
                         }])
        try:
            os.remove("v4.json")
        except OSError as e:
            pass

    def test_toggle_behaviour(self):
        # Setup the strategy with
        strategy = V4Strategy("v4.json", [1])
        session2 = [{
            'source': str(self.sensorId),
            'attribute_name': 'Bar',
            'parameter_name': 'Foo',
            'value': '10',
            'request_id': None,
            'behaviour_id': 2
        },

            {
            'source': str(self.userActionId),
            'attribute_name': 'Foo',
            'parameter_name': 'Foo',
            'value': '5',
            'request_id': 2,
            'behaviour_id': 2
        }]

        event = Mock()
        event.type = Message.Event
        event.sender = self.sensorId.bytes
        event.receiver = uuid.uuid4().bytes
        event.data = {
            "event": "device.event",
            "attribute": {
                "name": "Bar",
                "parameters": [{
                    "name": "Foo",
                    "value": "10"
                }]
            }
        }

        # process both sessions
        strategy.processSession(self.testEvents, self.testState)
        strategy.processSession(session2, self.testState)
        # test that disabled behaviour doesn't trigger decisions
        self.assertEqual(strategy.decide(self.testTriggeringEvent), [])

        # test that non disabled devices still trigger events
        self.assertEqual(strategy.decide(event)[0].data["value"],
                         [{
                             "name": "Foo",
                             "value": "5"
                         }])
        # reactivate event
        strategy.activateBehaviour(1)
        # test that resactivated event  trigger events
        self.assertEqual(strategy.decide(self.testTriggeringEvent)[0].data["value"],
                         [{
                             "name": "Foo",
                             "value": "5"
                         }])

        # test that the deactivated behaviour doesn't make decisions
        strategy.deactivateBehaviour(2)
        self.assertEqual(strategy.decide(event), [])

        strategy.removeBehaviour(1)
        self.assertEqual(strategy.decide(self.testTriggeringEvent), [])

    def test_dont_trigger_on_self_events(self):
        strategy = V4Strategy("v4.json")
        session = [{
            'source': str(self.userActionId),
            'attribute_name': 'Foo',
            'parameter_name': 'Foo',
            'value': '5',
            'request_id': 2,
            'behaviour_id': 2
        }, {
            'source': str(self.userActionId),
            'attribute_name': 'Foo',
            'parameter_name': 'Foo',
            'value': '6',
            'request_id': 2,
            'behaviour_id': 2

        }]
        event = Mock()
        event.type = Message.Event
        event.sender = self.userActionId.bytes
        event.receiver = uuid.uuid4().bytes
        event.data = {
            "event": "device.event",
            "attribute": {
                "name": "Foo",
                "parameters": [{
                    "name": "Foo",
                    "value": "5"
                }]
            }
        }
        strategy.processSession(session, self.testState)
        # test that disabled behaviour doesn't trigger decisions
        self.assertEqual(strategy.decide(event), [])
