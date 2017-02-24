import uuid
import json
from unittest import TestCase
from unittest.mock import Mock,patch
from device import Device, DeviceType,Attribute,DataType, Parameter
from hub import Hub
from delegate.request_tracker import RequestTracker
from ipc import Message
from database import Database
from hub.hub_mode import HubMode


class RequestTrackerTest(TestCase):

    def setUp(self):
        self.id=uuid.uuid4().bytes        
        self.dev=Device(DeviceType('WeMo Switch','wemo', maker='WeMo', \
        attributes=[Attribute('state',[Parameter('state',DataType.Binary)]),\
        Attribute('noControl',[Parameter('noControl',DataType.Binary, value=1)],isControllable=False)])\
        , name= 'Lamp Switch', address=self.id,version='0.1.0')
        self.hub=Hub()
        self.hub.mode=HubMode.Learning



    @patch('database.DatabaseTranslator')       
    def test_ignore_message(self,MockTranslator):
        MockTranslator.received.return_value=True
        tracker=RequestTracker(MockTranslator, self.hub)
        self.hub.addDevice(self.dev)
        # test ignore request for hub
        self.assertFalse(tracker.received(Message(Message.Request,sender=self.id)))
    
    @patch('database.DatabaseTranslator')
    def test_request(self,MockTranslator):
        tracker=RequestTracker(MockTranslator, self.hub)
        self.hub.addDevice(self.dev)
        tracker.received(Message(Message.Request,\
            sender=self.id,receiver=uuid.uuid4().bytes))
        self.assertTrue(MockTranslator.received.called)

        
    @patch('database.DatabaseTranslator')
    def test_create_request(self,MockTranslator):

        def receive(message):
            if (message.type == Message.Request):
                return 10
            elif (message.type == Message.Event):
                self.assertTrue('requestId' in message.data)
                self.assertEqual(message.data['requestId'],10)
                
        MockTranslator.received=receive

        self.hub.addDevice(self.dev)
        tracker=RequestTracker(MockTranslator, self.hub)
        tracker.received(Message(Message.Event, data={'attribute':{'name':'state', 'parameters':\
        [{'name':'state', 'value':0}]}},\
            sender=self.id,receiver=uuid.uuid4().bytes))
        
        self.assertEqual(tracker.requests.get(self.dev.address),None)


    @patch('database.DatabaseTranslator')
    def test_no_request(self,MockTranslator):

        self.hub.addDevice(self.dev)
        tracker=RequestTracker(MockTranslator, self.hub)
        ret=tracker.received(Message(Message.Event, data={'attribute':{'name':'noControl', 'parameters':\
        [{'name':'noControl', 'value':0}]}},\
            sender=self.id,receiver=uuid.uuid4().bytes))
        self.assertTrue(MockTranslator.received.calledwith({'attribute':{'name':'noControl', 'parameters':\
        [{'name':'noControl', 'value':0}]}}))
        self.assertIsNone(ret)
        self.assertEqual(tracker.requests.get(self.dev.address),None)
        

    @patch('database.DatabaseTranslator')
    def test_dont_log(self,MockTranslator):
        self.hub.mode = HubMode.Normal
        tracker=RequestTracker(MockTranslator, self.hub)
        self.hub.addDevice(self.dev)
        tracker.received(Message(Message.Request,\
            sender=self.id,receiver=uuid.uuid4().bytes))
        self.assertFalse(MockTranslator.received.called)

         


