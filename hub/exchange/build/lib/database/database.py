import sqlite3
import logging
import os.path
import pkgutil

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
        # turn foreign keys on
        self.connection.execute('pragma foreign_keys=ON')

        def dict_factory(cursor, row):
            #returns results as dictionary instead of tuple
            d = {}
            for idx, col in enumerate(cursor.description):
                d[col[0]] = row[idx]
            return d
        self.connection.row_factory = dict_factory
        self.cursor = self.connection.cursor()

    def execute (self, sql, values=None):
        try:
            log.debug("Running SQL statement: " + sql)
            results = self.cursor.execute(sql, values)
            self.connection.commit()
            return self.cursor.fetchall()
        except Exception as e:
            log.error("Could not execute command " + sql + " " + str(e))

    def shutdown (self):
        self.cursor.close()
        log.info("Closed connection to " + self.name)

    def createDB (self):
        sql = pkgutil.get_data('database','database-setup.sql')
        sql = sql.decode('utf-8')
        self.connection.executescript(sql)
        self.connection.commit()

    def getLastInsertId(self):
        return self.cursor.lastrowid





