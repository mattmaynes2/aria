import uuid
from unittest   import TestCase
from unittest.mock import Mock
from brain.model_builder import ModelBuilder
from ipc import Message

class ModelBuilderTest (TestCase):

    def setUp(self):
        self.mockRetriever=Mock()
        self.modelBuilder= ModelBuilder(self.mockRetriever)
    
    def test_retrieve_session(self):
        id1=uuid.uuid4()
        id2=uuid.uuid4()
        self.mockRetriever.getSessionEvents.return_value=[{'source':id1}]

        self.modelBuilder.received(Message(Message.Request,data={'delete':'event', 'id':1}))
        self.assertFalse(self.mockRetriever.getSessionEvents.called)

        self.modelBuilder.received(Message(Message.Request,data={'deactivate':'session', 'id':1}))
        self.mockRetriever.getSessionEvents.assert_called_with(1)