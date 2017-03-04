import uuid
from unittest   import TestCase
from unittest.mock import Mock, patch
from brain.model_builder import ModelBuilder
from device import Device,Attribute,DeviceType,Parameter,DataType
from ipc import Message

class ModelBuilderTest (TestCase):

    def setUp(self):
        self.mockDecisionBroker=Mock()
        self.mockRetriever=Mock()
        self.mockStrategy=Mock()
        self.modelBuilder= ModelBuilder(self.mockRetriever,self.mockDecisionBroker,\
        self.mockStrategy,[])
    
    def test_retrieve_session(self):
        id1=uuid.uuid4().bytes
        id2=uuid.uuid4().bytes
        self.mockRetriever.getSessionEvents.return_value=[{'source':str(id1), 'attribute_name':'Foo', 
                                                            'parameter_name':'Foo','value':'5', 
                                                            'request_id':2}]

        self.modelBuilder.received(Message(Message.Request,data={'delete':'event', 'id':1}))
        self.assertFalse(self.mockRetriever.getSessionEvents.called)

        self.modelBuilder.received(Message(Message.Request,data={'deactivate':'session', 'id':1}))
        self.mockRetriever.getSessionEvents.assert_called_with(1)

        self.mockStrategy.processSession.assert_called_with(self.mockRetriever.getSessionEvents(),{})

    def test_set_strategy(self):
        strategy2=Mock()
        self.modelBuilder.strategy=strategy2
        self.assertEqual(strategy2, self.mockDecisionBroker.decisionStrategy)

    def test_getState(self):
        id1=uuid.uuid4().bytes
        id2=uuid.uuid4().bytes
        dev1=Device(DeviceType('WeMo Switch','wemo', maker='WeMo', \
        attributes=[Attribute('state',[Parameter('state',DataType.Binary,value=1)])]), name= 'Lamp Switch',\
        address=id1,version='0.1.0')
        
        dev2=Device(DeviceType('Speaker','sonos', maker='Sonos', \
        attributes=[Attribute('volume',[Parameter('volume',DataType.Int,min_=0,max_=100,value=5)])]), name= 'Lamp Switch',\
        address=id2,version='0.1.0')

        devices={}

        self.modelBuilder= ModelBuilder(self.mockRetriever,self.mockDecisionBroker,\
            self.mockStrategy,devices.values())
        devices[id1]=dev1
        devices[id2]=dev2
        dev2.getAttribute('volume').parameters[0].value=50
        # save current state when we start a training session 
        self.modelBuilder.received(Message(Message.Request,data={'activate':'session', 'id':1}))
        state=self.modelBuilder.state

        id1=str(uuid.UUID(bytes=id1))
        id2=str(uuid.UUID(bytes=id2))
        self.assertTrue( id1 in state)
        self.assertTrue( id2 in state)
        device1=state[id1]
        device2=state[id2]
        self.assertEqual('state',device1['attributes'][0]['name'])
        self.assertEqual(1,len(device1['attributes']))
        volume=device2['attributes'][0]
        self.assertEqual('volume',volume['name'])
        self.assertEqual(100,volume['parameters'][0]['max'])
        self.assertEqual(50,volume['parameters'][0]['value'])


