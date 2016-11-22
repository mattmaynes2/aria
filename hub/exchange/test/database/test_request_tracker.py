import uuid
import json
from unittest import TestCase
from unittest.mock import Mock,patch
from device import Device, DeviceType,Attribute,DataType
from hub import Hub
from database import RequestTracker


class RequestTrackerTest(TestCase):

    def setUp(self):
        self.id=uuid.uuid4()        
        self.dev=Device(DeviceType('WeMo Switch','wemo', maker='WeMo', \
        attributes=[Attribute('state',DataType.Binary)]), name= 'Lamp Switch', address=self.id.bytes,\
         version='0.1.0')
        self.hub=Hub()


    @patch('database.DatabaseTranslator')       
    def test_ignore_message(self,MockTranslator):
        tracker=RequestTracker(MockTranslator, self.hub)
        # test ignore unkown sender
        self.assertFalse(tracker.received(Message(Message.Request,sender=uuid.uuid4(),\
        receiver=self.id)))
        self.hub.addDevice(self.dev)
        # test ignore request for hub
        self.assertFalse(tracker.received(Message(Message.Request,sender=self.id)))
