from unittest import TestCase
import unittest
from hub        import Hub, Exchange, CLI, args, daemon
from device     import Device
from adapter import Message
from adapter import Adapter
from database import Database
import queue
import sqlite3

class TestDatabaseIntegration(TestCase):

    def setUp(self):
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
