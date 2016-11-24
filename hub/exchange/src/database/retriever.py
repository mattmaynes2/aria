import sqlite3
import logging
import sqlalchemy

class Retriever:

    def __init__(self, database):
        self.database = database

    ###
    # Get a list of count events across all devices
    # @param start   Index in the database to start retrieving from, with 0 being the most recent
    #                record
    # @param count   Number of events to retrieve
    # @param ignore  List of device UUIDs that should be ignored when retrieving events
    #
    # @return        List of count number of event objects across all devices
    ###
    def getEventWindow(self, start, count, ignore):
        sql = "SELECT * FROM \
                    (SELECT * FROM Event WHERE id <= ? ORDER BY id DESC)\
               WHERE id NOT LIKE ALL(ARRAY[?]) LIMIT ? ORDER BY id DESC"
        lastEventId = self.database.execute("SELECT * FROM Event LIMIT 1 ORDER BY id DESC")
        print("EVENT ID: " + str(lastEventId))
        values = (int(lastEventId) - start, ignore, count)
        results = self.database.execute(sql, values)
        print("Results: " + str(results))
        return results

    ###
    # Get a list of count events for a specific device
    # @param id      UUID of the device to get events from 
    # @param start   Index in the database to start retrieving from, with 0 being the most recent
    #                record
    # @param count   Number of events to retrieve
    #
    # @return        List of count number of event objects for the specified device id
    ###
    def getDeviceEvents(self, id_, start, count):
        sql = "SELECT * FROM\
                    (SELECT * Event WHERE id <= ? ORDER BY id DESC)\
                WHERE id LIKE ? LIMIT ? ORDER BY id DESC"
        lastEventId = self.database.execute("SELECT * FROM Event LIMIT 1 ORDER BY id DESC")
        print("EVENT ID: " + str(lastEventId))
        values = (int(lastEventId) - start, id_, count)
        results = self.database.execute(sql, values)
        print("Results: " + str(results))
        return results



    