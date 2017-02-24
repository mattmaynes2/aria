import uuid
from unittest   import TestCase
from unittest.mock import Mock, patch
from brain.model_builder import ModelBuilder
from ipc import Message

class ModelBuilderTest (TestCase):

    def setUp(self):
        self.mockDecisionBroker=Mock()
        self.mockRetriever=Mock()
        self.modelBuilder= ModelBuilder(self.mockRetriever,self.mockDecisionBroker)
    
    def test_retrieve_session(self):
        id1=uuid.uuid4()
        id2=uuid.uuid4()
        self.mockRetriever.getSessionEvents.return_value=[{'source':id1, 'attribute_name':'Foo', 
                                                            'parameter_name':'Foo','value':'5', 
                                                            'request_id':2}]

        self.modelBuilder.received(Message(Message.Request,data={'delete':'event', 'id':1}))
        self.assertFalse(self.mockRetriever.getSessionEvents.called)

        self.modelBuilder.received(Message(Message.Request,data={'deactivate':'session', 'id':1}))
        self.mockRetriever.getSessionEvents.assert_called_with(1)

        strategy=self.mockDecisionBroker.strategy
        self.assertEqual({'set':'Foo','value':[{'name':'Foo','value':'5'}]}, strategy.triggeredEvent.data)



