from unittest import TestCase
import unittest
from hub        import Hub, Exchange, CLI, args, daemon
from device     import Device
from adapter import Message
from adapter import Adapter
from database import Database
from database import RequestTracker
import queue
import sqlite3
import os
import uuid

class TestDatabaseIntegration(TestCase):

    def setUp(self):

        try:
            os.remove("aria.db")
        except OSError:
            pass

        self.hub         = Hub()
        self.cli         = CLI(self.hub)
        self.database    = Database()
        self.exchange    = Exchange(self.hub, self.cli, self.database)
        self.testAdapter = StubDeviceAdapter()
        self.exchange.register('stub', self.testAdapter)
        self.exchange.discovered(Device('hub', '', Message.DEFAULT_ADDRESS))
        self.exchange.start()

        self.db = TestDatabase()

    def tearDown(self):
        self.exchange.teardown()

    def test_sensor_state_should_be_logged_to_database(self):
        sensorStateChangeMessage = Message()
        sensorStateChangeMessage.type = Message.Event
        sensorStateChangeMessage.data = {"state" : "1"}
        self.testAdapter.enqueueMessage(sensorStateChangeMessage)
        self.exchange.teardown() #Tear down exchange to ensure database is written to
        results = self.db.query("SELECT count(*) FROM Event")
        self.assertEqual(results.fetchone()[0], 1)

    def test_events_should_be_linked_to_requests(self):

        myUuid = uuid.uuid4().bytes
        requestMessage = Message()
        requestMessage.type = Message.Request
        requestMessage.data = {"action" : "brightness", "value" : 100}
        requestMessage.receiver = myUuid
        self.testAdapter.enqueueMessage(requestMessage)
        
        eventMessage = Message()
        eventMessage.data = { "brightness" : 100 }
        eventMessage.type = Message.Event 
        eventMessage.sender = myUuid
        self.testAdapter.enqueueMessage(eventMessage)    
        self.exchange.teardown()

        results = self.db.query("SELECT count(*) = 1 FROM \
                                Event e INNER JOIN Request r ON e.request_id = r.id\
                                WHERE e.attribute = 'brightness' AND e.value = 100")

        firstResult = results.fetchone()
        self.assertEqual(firstResult[0], 1)

class TestDatabase:

    def __init__(self):
        self.conn = sqlite3.connect("aria.db")
        self.cursor = self.conn.cursor()

    def query(self, sql):
        return self.cursor.execute(sql)



class StubDeviceAdapter(Adapter):

    q = queue.Queue()

    def __init__(self):
        super().__init__()

    def enqueueMessage(self, m):
        """
        Add a message to the queue of messages returned when receive() is called
        """
        self.q.put(m)

    def receive(self):
        """
        Pops the next message of the queue and notifies subscribers
        """
        message = self.q.get()
        if (message == None):
            return None
        self.notify('received', message)
        self.q.task_done()
        return True

    def teardown(self):
        super().teardown()
        self.q.put(None)
