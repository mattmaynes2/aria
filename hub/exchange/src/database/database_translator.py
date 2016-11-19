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
        if (message.type not in ignore):
            for key in message.data:
                self.database.execute("INSERT into Dvent (type, sender, receiver, key, value) VALUES("\
                + message.type + ", " + str(UUID(bytes = message.sender)) + ", " \
                + str(UUID(bytes = message.receiver)) + ", " + key + ", " + message.data[key] + \
                ");")

    def discovered (self, device):
        log.info('Received ' + str(device))
        self.database.execute("INSERT into Device (type, name, address) VALUES (" + device.type + \
        ", " + device.name + ", " + device.address + ");")

                
                


    
        
        
    
    

    

    
    





