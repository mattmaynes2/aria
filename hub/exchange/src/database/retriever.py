import sqlite3
import logging

log = logging.getLogger(__name__)

class Retriever:

    GET_ALL_EVENT_WINDOW    = "SELECT * FROM Event WHERE source NOT IN (?) ORDER BY id DESC LIMIT ?,?"

    GET_DEVICE_EVENT_WINDOW = "SELECT * FROM Event where source = ? LIMIT  ?,?" 

    GET_LAST_EVENT_ID       = "SELECT * FROM Event ORDER BY id DESC LIMIT 1 "

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
        values = (ignore, start, count)
        results = self.database.execute(Retriever.GET_ALL_EVENT_WINDOW, values)
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
        lastEventId = self.database.execute(Retriever.GET_LAST_EVENT_ID)
        print("EVENT ID: " + str(lastEventId))
        values = (id_, start,count)
        results = self.database.execute(Retriever.GET_ALL_EVENT_WINDOW, values)
        return results





    