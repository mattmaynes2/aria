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
            log.info("Received " + str(message))
            return _request(message)
        elif (message.type == Message.Event):
            _event(message)
            
    def discovered (self, device):
        log.info('Received ' + str(device))
        self.database.execute("INSERT into Device (address, name, version, type) VALUES (?, ?, ?, ?);", \
        str(device.address), str(device.name), str(device.type), str(device.device_type))  

    def _request(self, message):
        self.databse.execute("INSERT into Request (source, receiver, action, value) VALUES (?, ?, ?);" \
        , str(UUID(bytes = message.sender)), str(UUID(bytes = message.receiver)), str(key), \
        str(message.data[key]))  
        results = self.database.execute("SELECT last_insert_rowid()")
        return results.get_points()

    def _event(self, event):
        id = message.data["requestId"] if "requestId" in message.data else None
        self.database.execute("INSERT into Event (request_id, source, attribute, value) VALUES( \
        ?, ?, ?, ?);", id, str(UUID(bytes = message.sender)), str(UUID(bytes = message.receiver)), \
        str(key), str(message.data[key]))


                
                


    
        
        
    
    

    

    
    





