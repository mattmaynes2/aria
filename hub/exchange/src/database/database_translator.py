import sqlite3
import logging

from adapter import Delegate
from adapter import Message
from uuid import UUID

log=logging.getLogger(__name__)

class DatabaseTranslator(Delegate):

    def __init__ (self, database):
       self.database = database 

    def received (self, message):
        if (message.type == Message.Request):
            log.info("Received ")
            return _request(message)
        elif (message.type == Message.Event):
            _event(message)
            
    def discovered (self, device):
        log.info('Received ' + str(device))
        self.database.execute("INSERT into Device (type, name, address) VALUES ('" + str(device.type) + \
        "', '" + device.name + "', '" + str(UUID(bytes =device.address)) + "');")

    def _request(self, message):           
            self.database.execute("INSERT into Request (sender, receiver, action, value) VALUES('"\
            + str(UUID(bytes = message.sender)) + "', '" \
            + str(UUID(bytes = message.receiver)) + "', '" + str(key) + "', '" + str(message.data[key]) + \
            "');")
            #return self.connection.last_insert_rowid()
            results = self.database.execute("SELECT last_insert_rowid()")
            return results.get_points()

    def _event(self, event):
        id = message.data["requestId"] if "requestId" in message.data else None
        self.database.execute("INSERT into Event (request_id, sender, attribute, value) VALUES("\
            + id + ", '" + str(UUID(bytes = message.sender)) + "', '" \
            + str(UUID(bytes = message.receiver)) + "', '" + str(key) + "', '" + str(message.data[key]) + \
            "');")

                
                


    
        
        
    
    

    

    
    





