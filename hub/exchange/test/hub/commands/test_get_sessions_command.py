import os
import uuid
from hub import Hub
from ipc import Message
from adapter import HubAdapter
from unittest import TestCase
from database import Database
from unittest.mock import Mock
from hub.commands import GetSessionsCommand

class TestGetSessionsCommand(TestCase):

    def setUp(self):
        try:
            os.remove(self._testMethodName + ".db")
        except OSError as e:
            pass
        self.database    = Database(self._testMethodName + ".db")

    def testExecute(self):
        self.database.execute("INSERT INTO Behaviour(id,name) VALUES(1,'Test')")
        self.database.execute("INSERT INTO Session(id,name,behaviour_id) VALUES(1,'Take 1',1)")
        self.database.execute("INSERT INTO Session(id,name,behaviour_id) VALUES(2,'Take 2',1)")
        hub = Hub()
        mockDelegate=Mock()
        adapter =HubAdapter(hub)
        adapter.add_delegate(mockDelegate)

        command=GetSessionsCommand(self.database)
        hub.addCommand(command)

        message=Message(Message.Request,
            {"behaviourId": 1, "count": 10, "get": "sessions", "start": 0},uuid.uuid4())
        adapter.send(message)
        responce = mockDelegate.received.call_args[0][0]
        sessions=responce.data['value']
        self.assertEqual(2,sessions['total'])
        self.assertEqual('Take 2',sessions['records'][0]['name'])
        self.assertTrue('createdDate' in sessions['records'][0])




