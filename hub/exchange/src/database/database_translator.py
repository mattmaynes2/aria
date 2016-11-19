import sqlite3
import logging

from adapter import Delegate
from adapter import Message
from uuid import UUID

log=logging.getLogger(__name__)

class DatabaseTranslator(Delegate):

    ignore = {Message.Error, Message.Discover, Message.Ack}
    def __init__ (self, database):
       self.database = database 

    def processEvent (self, message):
        log.info("Received " + str(message))

    def received (self, message):
        log.info('Received ' + str(message))
        if (message.type not in self.ignore):
            for key in message.data:
                self.database.execute("INSERT into event (type, sender, receiver, key, value) VALUES("\
                + str(message.type) + ", '" + str(UUID(bytes = message.sender)) + "', '" \
                + str(UUID(bytes = message.receiver)) + "', '" + str(key) + "', '" + str(message.data[key]) + \
                "');")
                
                


    
        
        
    
    

    

    
    





