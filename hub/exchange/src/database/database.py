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
            self.connection = sqlite3.connect(self.name, timeout)
            self.createDB()
        else:
            self.connection = sqlite3.connect(self.name, timeout)
        log.info("Opened connection to " + self.name)

    def execute (self, sql):
        try:
            self.connection.execute(sql)
        except:
            log.error("Could not execute command" + sql)

    def shutdown (self):
        self.connection.close()
        log.info("Closed connection to " + self.name)

    def createDB(self):
        with open('database//database-setup.sql') as f:
            sql = f.read()
            self.connection.executescript(sql)





