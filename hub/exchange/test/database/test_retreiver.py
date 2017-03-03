import uuid
import os
from unittest   import TestCase
import sqlite3
from database import Database, Retriever

class RetrieverTest(TestCase):

    def setUp(self):
        try:
            os.remove(self._testMethodName + ".db")
        except OSError as e:
            pass
        self.database    = Database(self._testMethodName + ".db")
        self.testDatabase  =TestDatabase(self._testMethodName + ".db") 
        self.retriever = Retriever(self.database)

    
    def setupDevices(self):
       
        self.testDatabase.execute("INSERT INTO Device_Type VALUES(2,'Dummy','foo','');")
        self.testDatabase.execute("INSERT INTO Device VALUES('00000000-0000-0000-0000-000000000000','0.5.0',2,'Dummy');")

        # create a sonos device
        self.testDatabase.execute("INSERT INTO Device_Type VALUES(1,'Sonos PLAY:1','sonos','');")
        self.testDatabase.execute("INSERT INTO Device VALUES('35434141-4644-4335-3139-414530313430','7.1',1,'Media Room');")
        self.testDatabase.execute("INSERT INTO Attribute VALUES(1,'bass','1','True');")
        self.testDatabase.execute("INSERT INTO Attribute VALUES(2,'treble','1','True');")
        self.testDatabase.execute("INSERT INTO Attribute VALUES(3,'loudness','1','True');")
        self.testDatabase.execute("INSERT INTO Attribute VALUES(4,'volume','1','True');")
        self.testDatabase.execute("INSERT INTO Attribute VALUES(5,'mute','1','True');")
 
        self.testDatabase.execute("INSERT INTO Parameter VALUES(1,'bass',1,'int',10,-10,'None');")
        self.testDatabase.execute("INSERT INTO Parameter VALUES(2,'treble',2,'int',10,-10,'None');")
        self.testDatabase.execute("INSERT INTO Parameter VALUES(3,'loudness',3,'binary','None','None','None');")
        self.testDatabase.execute("INSERT INTO Parameter VALUES(4,'volume',4,'int',100,0,'None');")
        self.testDatabase.execute("INSERT INTO Parameter VALUES(5,'mute',5,'binary','None','None','None');")
        self.testDatabase.commit()
    
    def test_get_session_events(self):
        self.setupDevices()
        # setup behaviour and sessions
        self.testDatabase.execute("INSERT INTO Behaviour(id,name) VALUES(1,'Test')")
        self.testDatabase.execute("INSERT INTO Session(id,name,behaviour_id) VALUES(1,'Take 1',1)")
        self.testDatabase.execute("INSERT INTO Session(id,name,behaviour_id) VALUES(2,'Take 2',1)")

        # create events
        self.testDatabase.execute("INSERT INTO event(id,source, session_id)" + \
                              " VALUES(1,'35434141-4644-4335-3139-414530313430', 1)")
        self.testDatabase.execute("INSERT INTO event(id,source, session_id)" + \
                              " VALUES(2,'35434141-4644-4335-3139-414530313430', 1)")
        self.testDatabase.execute("INSERT INTO event(id,source, session_id)" + \
                              " VALUES(3,'35434141-4644-4335-3139-414530313430', 2)")

        # create parameter changes
        self.testDatabase.execute("INSERT INTO parameter_change VALUES(1,4,'10',1)")
        self.testDatabase.execute("INSERT INTO parameter_change VALUES(2,1,'0',2)")
        self.testDatabase.execute("INSERT INTO parameter_change VALUES(3,3,'1',3)")
        self.testDatabase.commit()

        results=self.retriever.getSessionEvents(1)
        self.assertEqual(2,len(results))

        self.assertEqual('volume',results[0]['parameter_name'])
        self.assertEqual('bass',results[1]['parameter_name'])


    def test_addBehaviour(self):
        self.assertTrue(set({"name":"Test", "id": 1}).issubset(
            set(self.retriever.addBehaviour("Test"))))

    def test_addSession(self):
        self.database.execute("INSERT INTO Behaviour(id,name) VALUES(1,'Test')",None)
        self.assertTrue(set({"name":"Take 1", "id": 1, "behaviour_id":1}).issubset(
            set(self.retriever.addSession(1,"Take 1"))))

    def test_stop_session(self):
        self.database.execute("INSERT INTO Behaviour(id,name) VALUES(1,'Test')")
        self.database.execute("INSERT INTO Session(id,name,behaviour_id) VALUES(1,'Take 1',1)")

        self.retriever.stopSession(1)
        result=self.database.execute("select * from session")[0]
        self.assertEqual(1,result['stopped'])

class TestDatabase:

    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)

    def execute(self,sql):
        self.conn.execute(sql)
    
    def commit(self):
        self.conn.commit()