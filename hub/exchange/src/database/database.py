import sqlite3
import logging
import os.path
import pkgutil
import sys

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
            log.info("Opened connection to " + self.name)

    def execute (self, sql):
        try:
            log.debug("Running SQL statement: " + sql)
            self.connection.execute(sql)
            self.connection.commit()
        except Exception as e:
            log.error("Could not execute command " + sql + " " + str(e))

    def shutdown (self):
        self.connection.close()
        log.info("Closed connection to " + self.name)

    def createDB(self):
        sql = pkgutil.get_data('database','database-setup.sql')
        sql = sql.decode('utf-8')
        self.connection.executescript(sql)
        self.connection.commit()





