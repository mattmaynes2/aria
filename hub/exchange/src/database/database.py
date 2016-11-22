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
        self.cur = self.connection.cursor()

    def execute (self, sql, values=None):
        try:
            log.debug("Running SQL statement: " + sql)
            results = self.cur.execute(sql, values)
            self.connection.commit()
            return results
        except Exception as e:
            log.error("Could not execute command " + sql + " " + str(e))

    def shutdown (self):
        self.cur.close()
        log.info("Closed connection to " + self.name)

    def createDB(self):
        sql = pkgutil.get_data('database','database-setup.sql')
        sql = sql.decode('utf-8')
        self.connection.executescript(sql)
        self.connection.commit()

    def getLastInsertId(self):
        return self.cur.lastrowid





