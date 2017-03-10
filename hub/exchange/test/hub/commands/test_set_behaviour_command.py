import os
import uuid
from hub import Hub
from ipc import Message
from adapter import HubAdapter
from unittest import TestCase
from database import Database
from unittest.mock import Mock
from hub.commands import SetBehaviourCommand

class TestSetBehaviourCommand(TestCase):

    def setUp(self):
        try:
            os.remove(self._testMethodName + ".db")
        except OSError as e:
            pass
        self.database    = Database(self._testMethodName + ".db")

    def testExecute(self):
        self.database.execute("INSERT INTO Behaviour(id,name) VALUES(1,'Test')")
        hub = Hub()
        mockDelegate=Mock()
        adapter =HubAdapter(hub)
        adapter.add_delegate(mockDelegate)

        command=SetBehaviourCommand(self.database)
        hub.addCommand(command)

        message=Message(Message.Request,
            {"set": "behaviour", "id": 1, "name": "New Name", "active": 0},uuid.uuid4())
        adapter.send(message)
        responce = mockDelegate.received.call_args[0][0]
        behaviour=responce.data['value']
        self.assertEqual("New Name",behaviour['name'])
        self.assertEqual(0,behaviour['active'])