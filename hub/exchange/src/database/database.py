import sqlite3
import logging
import os.path
log=logging.getLogger(__name__)

class Database:
    
    
    def __init__ (self, db_name = "aria.db"):
        self.name = db_name
        self.connect()

    def connect (self, timeout=5):
        if(not os.path.isfile(self.name)):
            self.connection = sqlite3.connect(self.name, timeout,check_same_thread=False)
            self.createDB()
        else:
            self.connection = sqlite3.connect(self.name, timeout,check_same_thread=False)

    def execute (self, sql):
        try:
            log.debug("Running SQL statement: " + sql)
            self.connection.execute(sql)
        except Exception as e:
            log.error("Could not execute command " + sql + " " + str(e))

    def shutdown (self):
        self.connection.close()

    def createDB(self):
        with open('database//database-setup.sql') as f:
            sql = f.read()
            self.connection.executescript(sql)





