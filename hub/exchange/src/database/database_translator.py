import logging
import sqlite3
from uuid import UUID

from ipc import  Message
from delegate import Delegate

log=logging.getLogger(__name__)

class DatabaseTranslator(Delegate):

    DISCOVER          = "INSERT INTO Device (address, version, type, name) VALUES (?, ?, ?, ?)"
    REQUEST           = "INSERT INTO Request (source, receiver) VALUES (?, ?)"
    EVENT             = "INSERT INTO Event (request_id, source, session_id) VALUES (?, ?,?)"
    PARAMETER_CHANGE  = "INSERT INTO Parameter_Change (parameter, value, event_id) VALUES \
                        (?, ?, ?)"

    GET_PARAMETER     = "SELECT id FROM Parameter WHERE attribute_id = ? AND name = ?"
    GET_DEVICE_TYPE   = "SELECT type FROM Device WHERE address = ?"
    GET_ATTRIBUTE     = "SELECT id FROM Attribute WHERE device_type = ? AND name = ?"

    SET_DEVICE_TYPE   = "INSERT INTO Device_Type (name, protocol, maker) VALUES (?, ?, ?)"
    SET_ATTRIBUTE     = "INSERT INTO Attribute (name, device_type, controllable) VALUES (?, ?, ?)"
    SET_PARAMETER     = "INSERT INTO Parameter (name, attribute_id, data_type, max, min, step) \
                         VALUES (?, ?, ?, ?, ?, ?)"

    GET_LAST_PARAMETER_ID = "SELECT * FROM Parameter_Change ORDER BY id DESC LIMIT 1"
    GET_DEVICE_TYPE_ID  = "SELECT id FROM Device_Type WHERE name = ?"

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
            typeValues = (str(device.deviceType.name), str(device.deviceType.protocol)\
            , str(device.deviceType.maker))
            
            
            deviceTypeId = None
            existingId = self._getDeviceTypeId(str(device.deviceType.name))
            
            if existingId:
                log.info("DeviceType " + str(device.deviceType.name) + " already exists in the \
                database")
                deviceTypeId = existingId[0]["id"]
                
            else:
                self.database.execute(DatabaseTranslator.SET_DEVICE_TYPE, typeValues)
                deviceTypeId = self.database.getLastInsertId()

            self.database.execute(DatabaseTranslator.DISCOVER, (self._getStr(device.address)\
            , str(device.version), deviceTypeId, str(device.name)))           
            for attribute in device.deviceType.attributes:
                self._setAttribute(attribute, deviceTypeId)
                attributeId = self.database.getLastInsertId()
                for parameter in attribute.parameters:
                    self._setParameter(attributeId, parameter)

        else:
            log.warning("Device discovered with null address")

    def _request(self, message):
        values =  (self._getStr(message.sender), self._getStr(message.receiver))
        self.database.execute(DatabaseTranslator.REQUEST, values)
        return self.database.getLastInsertId()

    def _event(self, event):
        if "requestId" in event.data:
            id_ = event.data["requestId"]
        else:
            id_ = None
        session_id= event.data.get("session_id",None) 


        values = (id_, self._getStr(event.sender),session_id)
        self.database.execute(DatabaseTranslator.EVENT, values)
        eventID = self.database.getLastInsertId()

        attribute=event.data["attribute"]
        attributeName = attribute["name"]
        parameters = attribute["parameters"]
        attributeID = self._getAttributeID(self._getStr(event.sender), attributeName)
    
        for parameter in parameters:
            parameterID = self._getParameterID(attributeID[0]["id"], parameter["name"])
            self._setParameterChange(parameterID, parameter["value"], eventID)             

    def _getParameterID(self, attributeID, paramName):       
        paramResults = self.database.execute(DatabaseTranslator.GET_PARAMETER, (attributeID, paramName))
        return paramResults[0]["id"]

    def _getAttributeID(self, address, attributeName):
        typeResults = self._getDeviceType(address)
        type_ = str(typeResults[0]["type"])
        return self.database.execute(DatabaseTranslator.GET_ATTRIBUTE, (type_, attributeName))

    def _getDeviceType(self, address):
        return self.database.execute(DatabaseTranslator.GET_DEVICE_TYPE, [address])

    def _getStr(self, bytes_):
        return str(UUID(bytes = bytes_))

    def _setParameterChange(self, parameter, value, event=None):
        values = (parameter, value, event)
        self.database.execute(DatabaseTranslator.PARAMETER_CHANGE, values)
        return self.database.getLastInsertId()

    def _setAttribute(self, attribute, type_):
        values = (str(attribute.name), type_, str(attribute.isControllable))
        self.database.execute(DatabaseTranslator.SET_ATTRIBUTE, values)

    def _setParameter(self, attributeId, parameter):
        values = (str(parameter.name), attributeId, str(parameter.dataType.value), str(parameter.max)\
        , str(parameter.min), str(parameter.step))
        self.database.execute(DatabaseTranslator.SET_PARAMETER, values)

    def _getDeviceTypeId(self, name):
        return self.database.execute(DatabaseTranslator.GET_DEVICE_TYPE_ID, [name])
