from .device import Device
from .parameter import Parameter
from .data_types import DataType
from .attribute import Attribute
from .device_type import DeviceType
import time
import logging
import uuid

logger = logging.getLogger(__name__)

class ZWaveValueWrapper():

    COMMAND_CLASS_MULTILEVEL_SWITCH = 38

    def __init__(self, value):
        self._wrappedValue = value
        if value.data == 0:
            self.on = False

    @property
    def data(self):
        if self._wrappedValue.type == 'Byte' and self._wrappedValue.command_class == ZWaveValueWrapper.COMMAND_CLASS_MULTILEVEL_SWITCH and not self.on:
            return 0
        return self._wrappedValue.data

    @data.setter
    def data(self, value):
        if self._wrappedValue.type == 'Byte' and self._wrappedValue.command_class == ZWaveValueWrapper.COMMAND_CLASS_MULTILEVEL_SWITCH:
            self.on = (value != 0)

        self._wrappedValue.data = value

    def __getattr__(self, attr):
        """Everything else is delegated to the object"""
        return getattr(self._wrappedValue, attr)

class ZWaveDevice(Device):
    PROTOCOL='zwave'
    dataMappings={'Bool':DataType.Binary,'Byte':DataType.Byte, 'Decimal':DataType.Float,\
    'Int':DataType.Int, 'Short':DataType.Int, 'String':DataType.String, 'Button':DataType.Binary, \
    'List':DataType.List}

    def __init__ (self, node):
        self.__valueMap = {}
        nodeName = node.name
        if not nodeName:
            nodeName = node.product_name

        super().__init__(self._getDeviceType(node), name = nodeName,address=uuid.uuid4().bytes,\
        version=str(node.version))
        self.__node = node

    def _getDeviceType(self, node):
        attributes = []
        for key,val in node.get_values(genre='User').items():
            if val.type == 'Byte' and val.command_class == ZWaveValueWrapper.COMMAND_CLASS_MULTILEVEL_SWITCH:
                max = 99
            else:
                max = val.max
            parameter= Parameter(val.label, ZWaveDevice.dataMappings[val.type],max_=max, \
            min_=val.min, value=val.data)
            attribute=Attribute(val.label,parameters=[parameter],isControllable=not val.is_read_only)
            attributes.append(attribute)
            self.__valueMap[val.label] = ZWaveValueWrapper(val)

        return DeviceType(node.product_name, ZWaveDevice.PROTOCOL, node.manufacturer_name,\
        attributes=attributes)

    def getName(self) :
        return self.__node.name

    def getDeviceType(self) : 
        return self.__node.product_name

    def getValue(self, attribute):
        """
        Returns the value of an attribute
        attribute is the name of the attribute (String)
        """
        parameters = {
            "name" : attribute,
            "value" : self.__valueMap[attribute].data
        }
        return parameters

    def buildParamChange(self, val):
        parameterChange = {
            'name' : val.label,
            'value' : val.data,
            'dataType' : ZWaveDevice.dataMappings[val.type]
        }
        return parameterChange

    def setValue(self, attribute, value):
        """
        Sets the value of an attribute. This affects the state of the physical device
        attribute is the name of an attribute
        value is the new value of the attribute
        """
        zwaveVal = self.__valueMap[attribute]
        checkedVal = zwaveVal.check_data(value)
        logger.debug("Received request to set value of attribute: " + attribute)         
        if checkedVal == None:
            raise ValueError("Invalid value for parameter " + attribute + " of attribute " + attribute + ": " + value)
        else:
            logger.debug("Attempting to set attribute: " + str(attribute) + " to value " + str(value))
            zwaveVal.data = checkedVal
            return self.buildParamChange(zwaveVal)


    def processEvent(self, label):
        val = self.__valueMap[label]
        parameters = []
        parameterChange = self.buildParamChange(val)
        parameters.append(parameterChange)
        data = {
            'event' : 'device.event',
            'timestamp' : int(time.time()*1000),
            'device' : self.__node.name,
            'deviceType' : self.__node.product_name,
            'attribute' : {
                'name' : val.label,
                'parameters' : parameters
            }
	}
        return data

