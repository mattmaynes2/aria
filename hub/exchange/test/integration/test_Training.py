import os
import time
import logging
import unittest
from unittest import TestCase
from hub.commands import GetBehavioursCommand,CreateBehavioursCommand, CreateSessionCommand, \
ActivateSessionCommand, DeactivateSessionCommand, DeleteBehaviourCommand, DeleteSessionCommand
from .Database import StubDeviceAdapter, TestDatabase
from device import Device, DeviceType, Attribute, DataType, Parameter
from hub import Hub,Exchange,CLI, HubMode
from database import Database
from adapter import HubAdapter
from ipc import Message

log= logging.getLogger(__name__)

class TestBehaviours(TestCase):
    
    @classmethod
    def setUpClass(self):
         self.device = Device(DeviceType("testname", "stub", "nobody", \
        attributes=[Attribute('state',[Parameter('state',DataType.Binary)])]))
    
    
    def setUp(self):
        try:
            os.remove(self._testMethodName + ".db")
        except OSError as e:
            pass

        self.database    = Database(self._testMethodName + ".db")
        self.hub         = Hub()
        self.hub.mode    = HubMode.Learning
        self.cli         = CLI(self.hub)
        self.exchange    = Exchange(self.hub, self.cli, self.database)
        self.registerAdapters()
        self.testAdapter = StubDeviceAdapter()
        self.exchange.register('stub', self.testAdapter)
        self.exchange.register('hub',HubAdapter(self.hub))
        self.exchange.discovered(self.hub)
        self.exchange.start()
        self.db = TestDatabase(self._testMethodName + ".db")
        self.exchange.discovered(self.device)

    def registerAdapters(self):
        self.hub.addCommand(GetBehavioursCommand(self.database))
        self.hub.addCommand(CreateBehavioursCommand(self.database))
        self.hub.addCommand(CreateSessionCommand(self.database))
        self.hub.addCommand(ActivateSessionCommand(self.database))
        self.hub.addCommand(DeactivateSessionCommand(self.database))
        self.hub.addCommand(DeleteBehaviourCommand(self.database))
        self.hub.addCommand(DeleteSessionCommand(self.database))

    def tearDown(self):
        self.exchange.teardown()
        if (self.testAdapter.exceptionTrace):
           raise Exception(self.testAdapter.exceptionTrace)
        
    
    def test_create_behaviour(self):
        createMessage= Message()
        createMessage.type= Message.Request
        createMessage.data= {'create':'behaviour', 'name':'lights'}
        createMessage.sender = self.device.address
        self.testAdapter.enqueueMessage(createMessage)
        
        time.sleep(0.5)
        response = self.testAdapter.receivedMessages[0]
        self.assertEqual(response.data["response"], "behaviour")
        self.assertTrue(set({"name":"lights", "id":1}).issubset(set(response.data["value"])))


    def test_behaviours_window(self):
        self.db.query("Insert into behaviour(name) values('lights and motion')")
        self.db.query("Insert into behaviour(name) values('temperature')")

        requestMessage = Message()
        requestMessage.type = Message.Request
        requestMessage.data = {"get" : "behaviours", "start" : 0, 'count' :  10 }
        requestMessage.sender = self.device.address
        self.testAdapter.enqueueMessage(requestMessage)
        
        time.sleep(0.5)
        response = self.testAdapter.receivedMessages[0]
        self.assertEqual(response.data["response"], "behaviours")
        self.assertEqual(response.data["value"]["total"], 2)
        self.assertEqual(len(response.data["value"]["records"]), 2)
        self.assertEqual(response.data["value"]["records"][0]['name'],'temperature')


    def test_session_activate(self):
        self.db.query("Insert into behaviour(name) values('lights and motion')")
        self.db.query("INSERT into session(name,behaviour_id) values ('Feb 10',1)")
        
        createMessage= Message()
        createMessage.type= Message.Request
        createMessage.data= {'activate':'session', 'id':1}
        createMessage.sender = self.device.address
        self.testAdapter.enqueueMessage(createMessage)

        time.sleep(0.5)
        self.assertEqual(self.hub.session.id, 1)
        self.assertEqual(self.hub.session.behaviour_id, 1)
        self.assertEqual(self.hub.mode, HubMode.Learning)
    
    def test_create_session(self):
        self.db.query("Insert into behaviour(name) values('lights and motion')")
        createMessage= Message()
        createMessage.type= Message.Request
        createMessage.data= {'create':'session', 'name':'lights_1', 'behaviourId':1}
        createMessage.sender = self.device.address
        self.testAdapter.enqueueMessage(createMessage)
        time.sleep(0.5)

        response = self.testAdapter.receivedMessages[0]
        self.assertEqual(response.data["response"], "session")
        self.assertTrue(set({"name": "lights_1","behaviourId":1, "id":1}).issubset(set(response.data["value"])))
    
    def test_session_end_to_end(self):
        myUuid = self.device.address
        createMessage= Message()
        createMessage.type= Message.Request
        createMessage.data= {'create':'behaviour', 'name':'lights'}
        createMessage.sender = myUuid
        self.testAdapter.enqueueMessage(createMessage)

        createMessage= Message()
        createMessage.type= Message.Request
        createMessage.data= {'create':'session', 'name':'lights_1', 'behaviourId':1}
        createMessage.sender = myUuid
        self.testAdapter.enqueueMessage(createMessage)
        
        createMessage= Message()
        createMessage.type= Message.Request
        createMessage.data= {'activate':'session', 'id':1}
        createMessage.sender = myUuid
        self.testAdapter.enqueueMessage(createMessage)

        self.sendEvent()
        
        createMessage= Message()
        createMessage.type= Message.Request
        createMessage.data= {'deactivate':'session', 'id':1}
        createMessage.sender = myUuid
        self.testAdapter.enqueueMessage(createMessage)
        self.sendEvent()  
        
        # sleep so that messages can be processed
        time.sleep(1.5)

        self.assertEqual(self.hub.session, None)
        self.assertEqual(self.hub.mode,HubMode.Normal)
        # make sure the event isn't logged when there is no active session
        results = self.db.query("SELECT * FROM event").fetchall()
        self.assertEqual(len(results),1)
        # make sure the event was associated with the session
        self.assertEqual(1,results[0]['session_id'])

    def test_cant_start_session_twice(self):
        self.db.query("Insert into behaviour(name) values('lights and motion')")
        self.db.query("INSERT into session(name,behaviour_id) values ('Feb 10',1)")
        myUuid = self.device.address
        
        activateMessage= Message()
        activateMessage.type= Message.Request
        activateMessage.data= {'activate':'session', 'id':1}
        activateMessage.sender = myUuid
        self.testAdapter.enqueueMessage(activateMessage)
        
        deactivateMessage= Message()
        deactivateMessage.type= Message.Request
        deactivateMessage.data= {'deactivate':'session', 'id':1}
        deactivateMessage.sender = myUuid
        self.testAdapter.enqueueMessage(deactivateMessage)

        self.testAdapter.enqueueMessage(activateMessage)
        # sleep to allow time to process messages 
        time.sleep(1)
        response = self.testAdapter.receivedMessages[2]
        self.assertEqual(Message.Error, response.type)

    def test_delete_behaviour(self):
        self.db.query("Insert into behaviour(name) values('lights and motion')")
        self.db.query("Insert into behaviour(name) values('Other')")
        self.db.query("INSERT into session(name,behaviour_id) values ('Mar 3',1)")
        self.db.query("INSERT into session(name,behaviour_id) values ('Mar 3_1',1)")
        
        deleteMessage= Message()
        deleteMessage.type= Message.Request
        deleteMessage.data= {'delete':'behaviour', 'id':1}
        deleteMessage.sender = self.device.address
        self.testAdapter.enqueueMessage(deleteMessage)
       
        # sleep to allow time to process messages 
        time.sleep(0.5)

        numSessions =self.db.query("SELECT count(*) FROM SESSION").fetchone()["count(*)"]
        numBehaviours =self.db.query("SELECT count(*) FROM behaviour").fetchone()["count(*)"]
        self.assertEqual(1,numBehaviours)
        self.assertEqual(0,numSessions)

    def test_delete_session(self):
        self.db.query("Insert into behaviour(name) values('lights and motion')")
        self.db.query("Insert into behaviour(name) values('Other')")
        self.db.query("INSERT into session(name,behaviour_id) values ('Mar 3',1)")
        self.db.query("INSERT into session(name,behaviour_id) values ('Mar 3_1',1)")
        
        deleteMessage= Message()
        deleteMessage.type= Message.Request
        deleteMessage.data= {'delete':'session', 'id':1}
        deleteMessage.sender = self.device.address
        self.testAdapter.enqueueMessage(deleteMessage)
       
        # sleep to allow time to process messages 
        time.sleep(0.5)

        numSessions =self.db.query("SELECT count(*) FROM SESSION").fetchone()["count(*)"]
        numBehaviours =self.db.query("SELECT count(*) FROM behaviour").fetchone()["count(*)"]
        self.assertEqual(2,numBehaviours)
        self.assertEqual(1,numSessions)

    def sendEvent(self):
        myUuid = self.device.address
        eventMessage = Message()
        eventMessage.data = {
            'event' : 'device.event',
            'timestamp' : int(time.time()*1000),
            'device' : myUuid,
            'deviceType' : self.device.deviceType.name,
            'attribute' : {
                'name' : 'state',
                'parameters' : [
                                {
                                    'name' : 'state',
                                    'value' : 1,
                                    'dataType' : DataType.Binary
                                }
                            ]
                        }
            }
        eventMessage.type = Message.Event 
        eventMessage.sender = myUuid
        eventMessage.receiver = Message.DEFAULT_ADDRESS
        self.testAdapter.enqueueMessage(eventMessage)