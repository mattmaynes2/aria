import logging
import sqlite3
from uuid import UUID

from ipc import  Message
from delegate import Delegate

log=logging.getLogger(__name__)

class DatabaseTranslator(Delegate):

    DISCOVER          = "INSERT INTO Device (address, version, name) VALUES (?, ?, ?)"
    REQUEST           = "INSERT INTO Request (source, receiver, change, value) VALUES (?, ?, ?, ?)"
    EVENT             = "INSERT INTO Event (request_id, source, change, value) VALUES (?, ?, ?, ?)"
    PARAMETER_CHANGE  = "INSERT INTO Parameter_Change (parameter, value) VALUES (?, ?)"
    PARAMETER         = "INSERT INTO Parameter (attribute, data_type, max, min, step) VALUES \
                         ?, ?, ?, ?, ?)"
    DEVICE_TYPE       = "INSERT INTO DEVICE_TYPE (protocol, maker) VALUES (?, ?)"

    GET_PARAMETER     = "SELECT id FROM Parameter WHERE name=? and attribute = ?""
    GET_DEVICE_TYPE   = "SELECT type FROM Device WHERE id=?"
    GET_ATTRIBUTES    = "SELECT id FROM Attribute WHERE device_type = ?"

    def __init__ (self, database):
       self.database = database

    def received (self, message):
        if (message.type == Message.Request):
            log.debug("Received " + str(message))
            return self._request(message)
        elif (message.type == Message.Event or message.type == Message.Response):
            self._event(message)

    def discovered (self, device):
        log.debug('Received ' + str(device))
        if device.address :
            self.database.execute(DatabaseTranslator.DISCOVER, (self._getStr(device.address)\
            , str(device.version), str(device.name)))
        else:
            log.warning("Device discoverd with null address")

    def _request(self, message):
        if "change" in message.data:
            change_value_ = str(message.data["value"])
            if "parameter" in message.data["change"]
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

    def _getParameter(self, name, attribute):
        return self.database.execute(DatabaseTranslator.PARAMETER, (name, attribute))

    def _getDeviceType(self, UUID):
        return self.database.execute(DatabaseTranslator.GET_DEVICE_TYPE, UUID)

    def _getStr(self, bytes_):
        return str(UUID(bytes = bytes_))

    def _setParameterChange(self, parameter, value):
        self.database.execute(DatabaseTranslator.PARAMETER_CHANGE(parameter, value))
