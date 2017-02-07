import sqlite3
import logging
from device import DataType
log = logging.getLogger(__name__)

class Retriever:

    GET_BEHAVIOUR_WINDOW    = "SELECT id, name, created_date, last_updated, active FROM Behaviour \
                               ORDER BY id DESC LIMIT ?,?" 
    GET_SESSION_WINDOW      = "SELECT id, name, created_date, active FROM Session WHERE \
                               behaviour_id = ? ORDER BY id DESC LIMIT ?,?"
    GET_ALL_EVENT_WINDOW    = "SELECT id as 'index', timestamp, source \
                               FROM Event WHERE source NOT IN (?) ORDER BY id DESC LIMIT ?,?"
    GET_DEVICE_EVENT_WINDOW = "SELECT * FROM Event WHERE source = ? LIMIT  ?,?"
    GET_PARAM_CHANGE        = "SELECT parameter, value FROM Parameter_Change WHERE event_id = ?"
    GET_PARAM_INFO          = "SELECT name, data_type FROM Parameter WHERE id = ?" 
    GET_DEVICE_TYPE         = "SELECT type, name FROM Device WHERE address = ?"
    GET_ATTRIBUTE_ID        = "SELECT id FROM Attribute WHERE device_type = ?"
    GET_ATTRIBUTE_NAME      = "SELECT name FROM Attribute WHERE id = ?"

    GET_LAST_EVENT_ID       = "SELECT id FROM Event ORDER BY id DESC LIMIT 1 "
    GET_LAST_BEAVIOUR_ID    = "SELECT id FROM Behaviour ORDER BY id DESC LIMIT 1 "
    GET_LAST_SESSION_ID     = "SELECT id FROM Session ORDER BY id DESC LIMIT 1 "

    ADD_NEW_BEHAVIOUR       = "INSERT INTO Behaviour (name) VALUES (?)"
    ADD_NEW_SESSION         = "INSERT INTO Session (behaviour_id, name) VALUES (?, ?)"

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
        for r in results:
            device = self._getDeviceType(r["source"])
            #log.error("\rType is: " + str(_type[0]["type"]))
            id = self._getAttribute(device[0]["type"])
            #log.error("\rID is: " + id["id"])
            r["attribute"] = {}
            r["attribute"]["name"] = self._getAttributeName(id[0]['id'])[0]['name']
            r['device']= device[0]['name']
            params = self._getParametersChanged(r["index"])

            r["attribute"]["parameters"] = []
            
            for p in params:
                newParam = {}
                paramInfo = self._getParameterInfo(p["parameter"])
                newParam["value"] = p["value"]
                newParam["name"] = paramInfo[0]['name']
                newParam["dataType"] = DataType(paramInfo[0]['data_type'])
                r["attribute"]["parameters"].append(newParam)
            
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
        values = (id_, start,count)
        results = self.database.execute(Retriever.GET_ALL_EVENT_WINDOW, values)
        return results

    ###
    # Add a new behaviour
    # @param name    Name of the new behaviour
    #
    # @return        The id of newly created behaviour
    ###
    def addBehaviour(self, name):
        self.database.execute(Retriever.ADD_NEW_BEHAVIOUR, [name])
        return self.database.execute(Retriever.GET_LAST_BEAVIOUR_ID)[0]["id"]

    ###
    # Add a new session
    # @param name    Name of the new session
    #
    # @return        The id of newly created session
    ###
    def addSession(self,behaviourId, name):
        values = (behaviourId, name) 
        self.database.execute(Retriever.ADD_NEW_SESSION, values)
        return self.database.execute(Retriever.GET_LAST_SESSION_ID)[0]['id']


    ###
    # Get a list of count behaviours
    # @param start   Index in the database to start retrieving from, with 0 being the most recent
    #                record
    # @param count   Number of behaviours to retrieve
    #
    # @return        List of count number of event objects across all devices
    ###
    def getBehaviourWindow(self, start, count):
        values = (start, count)
        return self.database.execute(Retriever.GET_BEHAVIOUR_WINDOW, values)

    ###
    # Get a list of count training sessions for a behaviour
    # @param start        Index in the database to start retrieving from, with 0 being the most recent
    #                     record
    # @param count        Number of sessions to retrieve
    # @param behaviourId  The behaviour to retrieve training sessions from
    #
    # @return        List of count number of event objects across all devices
    ###
    def getSessionWindow(self, start, count, behaviourId):
        values = (start, count, behaviourId)
        return self.database.execute(Retriever.GET_SESSION_WINDOW, values)

    def _getAttribute(self, deviceType):
        return self.database.execute(Retriever.GET_ATTRIBUTE_ID, [deviceType])

    def _getAttributeName(self, attributeID):
        return self.database.execute(Retriever.GET_ATTRIBUTE_NAME, [attributeID])

    def _getDeviceType(self, address):
        return self.database.execute(Retriever.GET_DEVICE_TYPE, [address])

    def _getParametersChanged(self, eventID):
        return self.database.execute(Retriever.GET_PARAM_CHANGE, [eventID])

    def _getParameterInfo(self, paramID):
        return self.database.execute(Retriever.GET_PARAM_INFO, [paramID])






    