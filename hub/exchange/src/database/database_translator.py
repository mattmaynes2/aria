import logging
import sqlite3
from uuid import UUID

from ipc import  Message
from delegate import Delegate

log=logging.getLogger(__name__)

class DatabaseTranslator(Delegate):

    DISCOVER          = "INSERT INTO Device (address, version, name) VALUES (?, ?, ?)"
    REQUEST           = "INSERT INTO Request (source, receiver) VALUES (?, ?)"
    EVENT             = "INSERT INTO Event (request_id, source) VALUES (?, ?)"
    PARAMETER_CHANGE  = "INSERT INTO Parameter_Change (parameter, value, request_id, event_id) VALUES \
                        (?, ?, ?, ?)"
    PARAMETER         = "INSERT INTO Parameter (attribute, data_type, max, min, step) VALUES \
                         (?, ?, ?, ?, ?)"
    DEVICE_TYPE       = "INSERT INTO DEVICE_TYPE (protocol, maker) VALUES (?, ?)"
    GET_PARAMETER     = "SELECT id FROM Parameter WHERE attribute = ? and name = ?"
    GET_DEVICE_TYPE   = "SELECT type FROM Device WHERE id = ?"
    GET_ATTRIBUTE     = "SELECT id FROM Attribute WHERE device_type = ? AND name = ?"

    GET_LAST_PARAMETER_ID       = "SELECT * FROM Parameter_Change ORDER BY id DESC LIMIT 1"

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
        values =  (self._getStr(message.sender), self._getStr(message.receiver)\
        , str(message.data['set']), str(message.data['value']))
        self.database.execute(DatabaseTranslator.REQUEST, values)
        results = self.database.execute
        return self.database.getLastInsertId()

    def _event(self, event):
        if "requestId" in event.data:
            id_ = event.data["requestId"]
        else:
            id_ = None

        values = (id_, self._getStr(event.sender))
        self.database.execute(DatabaseTranslator.EVENT, values)
        eventID = self.database.getLastInsertId()

        attributeName = str(message.data["attribute"])
        changes = message.data["changes"]
        attributeID = _getAttributeID(self._getStr(event.sender), attributeName)
        parameterID = _getParameterID(attributeID, parameter["name"])
        for parameter in change:
            _setParameterChange(parameterID, parameter["value"], eventID)             

    def _getParameterID(self, attributeID, paramName):       
        paramResults = self.database.execute(DatabaseTranslator.PARAMETER, (name, attribute))
        return paramResults["id"]

    def _getAttributeID(self, UUID, attributeName):
        typeResults = _getDeviceType(UUID)
        type_ = str(typeResults["type"])
        return self.database.execute(DatabaseTranslator.GET_ATTRIBUTE, (type_, attributeName))

    def _getDeviceType(self, UUID):
        return self.database.execute(DatabaseTranslator.GET_DEVICE_TYPE, UUID)

    def _getStr(self, bytes_):
        return str(UUID(bytes = bytes_))

    def _setParameterChange(self, parameter, value, event=None):
        values = (parameter, value, event, request)
        self.database.execute(DatabaseTranslator.PARAMETER_CHANGE, values)
        return self.database.execute(GET_LAST_PARAMETER_ID)
