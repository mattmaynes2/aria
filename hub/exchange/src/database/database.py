import sqlite3
import logging

log=logging.getLogger(__name__)

class Database:
    
    self.name
    self.connection

    def _init_ (self, db_name):
        self.name = db_name
    
    def connect (timeout=5):
        connection = ssqlite3.connect(self.db, timeout)

    def execute (sql)
        try:
            sql
        except:
            log.error("Could not execute command" + sql)

    def shutdown ():
        connection.close()





