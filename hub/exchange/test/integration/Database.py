from unittest import TestCase
import unittest
from hub        import Hub, Exchange, CLI, args, daemon
from device     import Device
from device     import DeviceType
from adapter import Message
from adapter import Adapter
from database import Database
from database import RequestTracker
import queue
import sqlite3
import os
import uuid
import time
import json
import logging
import traceback
import threading
from uuid import UUID

logging.disable(logging.WARNING)

class TestDatabaseIntegration(TestCase):

    @classmethod
    def setUpClass(self):
        self.devices = [Device(DeviceType("testname", "stub", "nobody")) for i in range(0,20)]

    def registerFakeDevices(self):
        for device in self.devices:
            self.exchange.discovered(device)
            
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
        self.exchange.discovered(self.hub)
        self.registerFakeDevices()
        self.exchange.start()

        self.db = TestDatabase()

    def tearDown(self):
        self.exchange.teardown()
        if (self.testAdapter.exceptionTrace):
           raise Exception(self.testAdapter.exceptionTrace)
        
    def test_sensor_event_message_should_be_logged_to_database(self):
        myUuid = self.devices[0].address
 
        sensorStateChangeMessage = Message()
        sensorStateChangeMessage.type = Message.Event
        sensorStateChangeMessage.sender = myUuid
        sensorStateChangeMessage.data = {"response" : "state", "value" : 1}

        self.testAdapter.enqueueMessage(sensorStateChangeMessage)
        self.exchange.teardown()
        results = self.db.query("SELECT * FROM Event").fetchone()
        self.assertEqual(results["request_id"], 0)
        self.assertEqual(results["source"], str(UUID(bytes=myUuid)))
        self.assertEqual(results["attribute"], "state")
        self.assertEqual(results["value"], "1")

    def test_requests_to_hub_should_not_be_logged_to_database(self):
        sensorStateChangeMessage = Message()
        sensorStateChangeMessage.type = Message.Request
        sensorStateChangeMessage.sender = self.devices[0].address

        sensorStateChangeMessage.data = {"set" : "mode", "value" : "2"}
        self.testAdapter.enqueueMessage(sensorStateChangeMessage)
        self.exchange.teardown()
 

        results = self.db.query("SELECT count(*) as count FROM Event")
        self.assertEqual(results.fetchone()["count"], 0)


    def test_events_should_be_linked_to_requests(self):

        myUuid = self.devices[0].address
        requestMessage = Message()
        requestMessage.type = Message.Request
        requestMessage.data = {"set" : "brightness", "value" : 100}
        requestMessage.receiver = myUuid
        self.testAdapter.enqueueMessage(requestMessage)
        
        eventMessage = Message()
        eventMessage.data = { "response" : "brightness", "value" : 100 }
        eventMessage.type = Message.Event 
        eventMessage.sender = myUuid
        eventMessage.receiver = bytes([0 for i in range(0,16)])
        self.testAdapter.enqueueMessage(eventMessage)    
        self.exchange.teardown()

        results = self.db.query("SELECT count(*) as count FROM \
                                Event e INNER JOIN Request r ON e.request_id = r.id\
                                WHERE e.attribute = 'brightness' AND e.value = 100")

        firstResult = results.fetchone()
        self.assertEqual(firstResult['count'], 1)

    def test_request_event_window_returns_events(self):
        # Put twenty events in the database
        for device in self.devices:
            sensorStateChangeMessage = Message()
            sensorStateChangeMessage.type = Message.Event
            sensorStateChangeMessage.data = {"response" : "state", "value" : 1}
            sensorStateChangeMessage.sender = device.address
            self.testAdapter.enqueueMessage(sensorStateChangeMessage)

        # Give some time to write to database
        time.sleep(0.5)

        # Request the last 10 events that occurred
        sensorEventWindowRequest = Message()
        sensorEventWindowRequest.type = Message.Request
        sensorEventWindowRequest.data = {"get": "eventWindow", "start": 0, "count": 10}

        # Give some time for the hub to respond to the request
        time.sleep(0.5)

        response = self.testAdapter.receivedMessages[0]

 
        self.assertEqual(response.data["response"], "eventWindow")
        self.assertEqual(response.data["value"]["total"], 10)
        self.assertEqual(len(response["value"]["records"]), 10)        

    def test_request_event_window_ignores_specified_devices(self):
        # Send a bunch of events from random devices
        for device in self.devices:
            sensorStateChangeMessage = Message()
            sensorStateChangeMessage.type = Message.Event
            sensorStateChangeMessage.data = {"response" : "state", "value" : 1}
            sensorStateChangeMessage.sender = device.address
            self.testAdapter.enqueueMessage(sensorStateChangeMessage)

        # Give some time to write to database
        time.sleep(0.5)

        # Request the last 10 events that occurred
        sensorEventWindowRequest = Message()
        sensorEventWindowRequest.type = Message.Request
        sensorEventWindowRequest.data = {"get": "eventWindow", "start": 0, "count": 10, "ignore" : [str(self.devices[0].address)]}

        # Give some time for the hub to respond to the request
        time.sleep(0.5)

        response = self.testAdapter.receivedMessages[0]
        self.assertEqual(response.data["response"], "eventWindow")
        self.assertEqual(response.data["value"]["total"], 5)
        self.assertEqual(len(response["value"]["records"]), 5)
        for device in response.data["value"]["records"]:
            self.assertNotEquals(device["device"], str(self.devices[0].address))

class TestDatabase:

    def __init__(self):
        self.conn = sqlite3.connect("aria.db")

        def dict_factory(cursor, row):
            d = {}
            for idx, col in enumerate(cursor.description):
                d[col[0]] = row[idx]
            return d
        self.conn.row_factory = dict_factory
        self.cursor = self.conn.cursor()

    def query(self, sql):
        return self.cursor.execute(sql)



class StubDeviceAdapter(Adapter):

    def __init__(self):
        super().__init__()
        self.q = queue.Queue()
        self.receivedMessages = []
        self.exceptionTrace = None

    def enqueueMessage(self, m):
        """
        Add a message to the queue of messages returned when receive() is called
        """
        self.q.put(m)

    def send(self, message):
        self.receivedMessages.append(message)

    def receive(self):
        try:
            """
            Pops the next message of the queue and notifies subscribers
            """
            message = self.q.get()
            if (message == None):
                return None

            self.notify('received', message)
            self.q.task_done()
            return True
        except:
            self.exceptionTrace = traceback.format_exc()
        return True

    def teardown(self):
        super().teardown()
        self.q.put(None)
