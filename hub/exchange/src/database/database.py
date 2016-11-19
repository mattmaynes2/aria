import sqlite3
import logging

log=logging.getLogger(__name__)

class Database:
    
    
    def __init__ (self, db_name = "aria.db"):
        self.name = db_name
        self.connect()

    def connect (self, timeout=5):
        self.connection = sqlite3.connect(self.name, timeout)

    def execute (self, sql):
        try:
            self.connection.execute(sql)
        except:
            log.error("Could not execute command" + sql)

    def shutdown (self):
        self.connection.close()





