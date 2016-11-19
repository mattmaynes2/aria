from unittest import TestCase
import unittest
from hub        import Hub, Exchange, CLI, args, daemon
from device     import Device
from adapter import Message
from adapter import Adapter
import queue

class TestDatabaseIntegration(TestCase):

    def setUp(self):
        self.hub         = Hub()
        self.cli         = CLI(self.hub)
        self.exchange    = Exchange(self.hub, self.cli)
        self.testAdapter = StubDeviceAdapter()
        self.exchange.register('stub', self.testAdapter)
        self.exchange.discovered(Device('hub', '', Message.DEFAULT_ADDRESS))

        self.exchange.start()

    def tearDown(self):
        self.exchange.teardown()

    @unittest.skip("test is not complete")
    def test_sensor_state_should_be_logged_to_database(self):
        sensorStateChangeMessage = Message()
        self.testAdapter.enqueueMessage(sensorStateChangeMessage)
        self.assertEqual(True, False)

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