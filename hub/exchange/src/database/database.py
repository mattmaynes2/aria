import sqlite3
import logging

log=logging.getLogger(__name__)

class Database:
    
    
    def __init__ (self, db_name = "aria.db"):
        self.name = db_name
        self.connect()

    def connect (self, timeout=5):
        self.connection = sqlite3.connect(self.name, timeout, check_same_thread=False)

    def execute (self, sql):
        try:
            log.debug("Running SQL statement: " + sql)
            self.connection.execute(sql)
        except Exception as e:
            log.error("Could not execute command " + sql + " " + str(e))

    def shutdown (self):
        self.connection.close()





