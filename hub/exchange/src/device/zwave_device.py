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
    COMMAND_CLASS_COLOR             = 51 
    
    def __init__(self, value):
        self._wrappedValue = value
        if value.data == 0:
            self.on = False

    def isMultilevelValue(self):
        return self._wrappedValue.type == 'Byte' and self._wrappedValue.command_class == ZWaveValueWrapper.COMMAND_CLASS_MULTILEVEL_SWITCH

    def isColourValue(self):
        return self._wrappedValue.type == 'String' and self._wrappedValue.command_class == ZWaveValueWrapper.COMMAND_CLASS_COLOR

    @property
    def data(self):
        if self.isMultilevelValue() and not self.on:
            return 0

        return self._wrappedValue.data

    @property
    def type(self):
        if self.isColourValue():
            return 'Color'
        return self._wrappedValue.type


    @data.setter
    def data(self, value):
        if self.isMultilevelValue():
            self.on = (value != 0)
        self._wrappedValue.data = value

    def buildData(self, value):
        if self.isColourValue():
            return value
        return self._wrappedValue.check_data(value)

    def check_data(self, value):
        if self.isColourValue():
            return str.encode("#"+value+"0000") 
        return self._wrappedValue.check_data(value)

    def __getattr__(self, attr):
        """Everything else is delegated to the object"""
        return getattr(self._wrappedValue, attr)

class ZWaveDevice(Device):
    PROTOCOL='zwave'
    dataMappings={'Bool':DataType.Binary,'Byte':DataType.Byte, 'Decimal':DataType.Float,\
    'Int':DataType.Int, 'Short':DataType.Int, 'String':DataType.String, 'Button':DataType.Binary, \
    'List':DataType.List, 'Color':DataType.Color}

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
            wrapped = ZWaveValueWrapper(val)
            parameter= Parameter(val.label, ZWaveDevice.dataMappings[wrapped.type],max_=max, \
            min_=val.min, value=val.data)
            attribute=Attribute(val.label,parameters=[parameter],isControllable=not val.is_read_only)
            attributes.append(attribute)
            self.__valueMap[val.label] = wrapped 

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
        logger.debug("Received request to set value of attribute: " + attribute + " to " + str(value))         
        checkedVal = zwaveVal.check_data(value)
        if checkedVal == None:
            raise ValueError("Invalid value for parameter " + attribute + " of attribute " + attribute + ": " + value)
        else:
            logger.debug("Attempting to set attribute: " + str(attribute) + " to value " + str(value))
            zwaveVal.data = checkedVal
            for att in self.deviceType.attributes : 
                if att.name == attribute:
                    att.parameters[0].value = zwaveVal.buildData(value)

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

