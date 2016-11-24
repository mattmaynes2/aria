import logging
import sqlite3
from uuid import UUID

from ipc import  Message
from delegate import Delegate

log=logging.getLogger(__name__)

class DatabaseTranslator(Delegate):

    DISCOVER        = "INSERT INTO Device (address, version, name) VALUES (?, ?, ?)"
    REQUEST         = "INSERT INTO Request (source, receiver, attribute, value) VALUES (?, ?, ?, ?)"
    EVENT           = "INSERT INTO Event (request_id, source, attribute, value) VALUES (?, ?, ?, ?)"

    def __init__ (self, database):
       self.database = database 

    def received (self, message):
        if (message.type == Message.Request):
            log.info("Received " + str(message))
            return self._request(message)
        elif (message.type == Message.Event or message.type == Message.Response):
            self._event(message)
            
    def discovered (self, device):
        log.info('Received ' + str(device))
        if device.address and device.version and device.name:
            self.database.execute(DatabaseTranslator.DISCOVER, str(device.address)\
            str(device.version), str(device.name)) 
        else:
            log.warning("Device discoverd with null address, version, or name")       

    def _request(self, message):
        values =  (self._getStr(message.sender), self._getStr(message.receiver)\
        , str(message.data['set']), str(message.data['value']))        
        self.database.execute(DatabaseTranslator.REQUEST, values)
        results = self.database.execute
        return self.database.getLastInsertId()

    def _event(self, event): 
        if "requestId" in event.data:
            id_ = event.data["requestId"]
        else:
            id_ = "0"
        values = (id_, self._getStr(event.sender), str(event.data['response'])\
        , str(event.data['value']))
        self.database.execute(DatabaseTranslator.EVENT, values)

    def _getStr(self, bytes_):
        return str(UUID(bytes = bytes_))
