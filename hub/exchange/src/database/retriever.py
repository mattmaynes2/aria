import sqlite3
import logging

log = logging.getLogger(__name__)

class Retriever:

    GET_ALL_EVENT_WINDOW    = "SELECT * FROM Event WHERE source NOT IN (?) ORDER BY id DESC LIMIT ?,?"
    GET_DEVICE_EVENT_WINDOW = "SELECT * FROM Event WHERE source = ? LIMIT  ?,?"
    GET_PARAM_CHANGE        = "SELECT * FROM Parameter_Change WHERE event_id = ?" 
    GET_DEVICE_TYPE         = "SELECT type FROM Device WHERE address = ?"
    GET_ATTRIBUTE_ID        = "SELECT id FROM Attribute WHERE device_type = ? AND name = ?"
    GET_ATTRIBUTE_NAME      = "SELECT name FROM Attribute WHERE id = ?"


    GET_LAST_EVENT_ID       = "SELECT * FROM Event ORDER BY id DESC LIMIT 1 "

    def __init__(self, database):
        self.database = database

# {														
# 	"records" : [										
# 		{												
# 			"index"			: 10,						
# 			"timestamp"		: 1480262533722,			
# 			"device"		: "Temperature Sensor",		
# 			"deviceType"	: "ZigBee Temperature Sensor",
# 			"attribute"		: {							
# 				"name" 			: "State",				
# 				"parameters"	: [						
# 					{									
# 						"name"		: "State",			
# 						"value"		: 30,				
# 						"dataType"	: "float"			
# 					}									
# 					... 								
# 				]										
# 			}											
# 		}												
# 		...												
# 	]													
# }																										

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
            _type = self.getDeviceType(r["source"])
            id = self.getAttribute(r)
            attibute["name"] = self.getAttributeName(id)
            r.change
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

    def getAttribute(self, event):
        return self.database.execute(Retriever.GET_ATTRIBUTE_ID)

    def getAttributeName(self, attributeID):
        return 

    def getDeviceType(self, address):
        return self.database.execute(DatabaseTranslator.GET_DEVICE_TYPE, [address])






    