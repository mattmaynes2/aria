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
    DEVICE_TYPE       = "INSERT INTO DEVICE_TYPE (name, protocol, maker) VALUES (?, ?, ?)"
    GET_PARAMETER     = "SELECT id FROM Parameter WHERE attribute = ? and name = ?"
    GET_DEVICE_TYPE   = "SELECT type FROM Device WHERE id = ?"
    GET_ATTRIBUTE     = "SELECT id FROM Attribute WHERE device_type = ? AND name = ?"

    SET_ATTRIBUTE     = "INSERT INTO Attributes (name, device_type, controllable) VALUES (?, ?, ?)"
    SET_PARAMETER     = "INSERT INTO Parameter (name, attribute_id, data_type, max, min, step) \
                         VALUES (?, ?, ?, ?, ?, ?)"

    GET_LAST_PARAMETER_ID = "SELECT * FROM Parameter_Change ORDER BY id DESC LIMIT 1"

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
            typeValues = (str(device.deviceType.name), str(device.deviceType.protocol)\
            , str(device.deviceType.maker))
            self.database.execute(DatabaseTranslator.DEVICE_TYPE, typeValues)
            deviceType = self.database.getLastInsertId()
            for attribute in device.deviceType.attributes:
                self._setAttribute(attribute, deviceType)
                attributeId = self.database.getLastInsertId()
                for parameter in device.deviceType.attributes.parameters:
                    self._setParameter(attributeId, parameter)

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
        changes = event.data["changes"]
        attributeID = self._getAttributeID(self._getStr(event.sender), attributeName)
        parameterID = self._getParameterID(attributeID, parameter["name"])
        for parameter in change:
            self._setParameterChange(parameterID, parameter["value"], eventID)             

    def _getParameterID(self, attributeID, paramName):       
        paramResults = self.database.execute(DatabaseTranslator.PARAMETER, (name, attribute))
        return paramResults["id"]

    def _getAttributeID(self, UUID, attributeName):
        typeResults = self._getDeviceType(UUID)
        type_ = str(typeResults["type"])
        return self.database.execute(DatabaseTranslator.GET_ATTRIBUTE, (type_, attributeName))

    def _getDeviceType(self, UUID):
        return self.database.execute(DatabaseTranslator.GET_DEVICE_TYPE, UUID)

    def _getStr(self, bytes_):
        return str(UUID(bytes = bytes_))

    def _setParameterChange(self, parameter, value, event=None):
        values = (parameter, value, event, request)
        self.database.execute(DatabaseTranslator.PARAMETER_CHANGE, values)
        return self.database.execute(DatabaseTranslator.GET_LAST_PARAMETER_ID)

    def _setAttribute(self, attribute, type_):
        values = (str(attribute.name), type_, str(attribute.isControllable))
        self.database.execute(DatabaseTranslator.SET_ATTRIBUTE, values)

    def _setParameter(self, attributeId, parameter):
        values = (str(parameter.name), attributeId, str(parameter.dataType), str(parameter.max)\
        , str(parameter.min), str(parameter.step))
        self.database.execute(DatabaseTranslator.SET_PARAMETER, values)
