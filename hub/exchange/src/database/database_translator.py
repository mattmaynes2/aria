import sqlite3
import logging

from adapter import Delegate

log=logging.getLogger(__name__)

class DatabaseTranslator(Delegate):

    def processEvent (self, message):
        log.info("Received " + message)

    def received (self, message):
        log.info('Received ' + str(message))
        
        
    
    

    

    
    





