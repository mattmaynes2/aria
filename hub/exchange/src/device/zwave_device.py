from .device import Device
from .parameter import Parameter
from .data_types import DataType
from .attribute import Attribute
from .device_type import DeviceType
import time
import logging
import uuid

logger = logging.getLogger(__name__)

class ZWaveDevice(Device):
    PROTOCOL='zwave'
    dataMappings={'Bool':DataType.Binary,'Byte':DataType.Byte, 'Decimal':DataType.Float,\
    'Int':DataType.Int, 'Short':DataType.Int, 'String':DataType.String, 'Button':DataType.Binary, \
    'List':DataType.List}

    def __init__ (self, node):
        self._valueMap = {}
        super().__init__(self._getDeviceType(node), name = node.name,address=uuid.uuid4().bytes,\
        version=str(node.version))
        self._node = node

    def _getDeviceType(self, node):
        attributes = []
        for key,val in node.get_values(genre='User').items():
            if val.type == 'Byte' and val.command_class == 38:
                max = 99
            else:
                max = val.max
            parameter= Parameter(val.label, ZWaveDevice.dataMappings[val.type],max_=max, \
            min_=val.min, value=val.data)
            attribute=Attribute(val.label,parameters=[parameter],isControllable=not val.is_read_only)
            attributes.append(attribute)
            self._valueMap[val.label] = val

        return DeviceType(node.product_name, ZWaveDevice.PROTOCOL, node.manufacturer_name,\
        attributes=attributes)

    def getName(self) :
        return self._node.name

    def getDeviceType(self) : 
        return self._node.product_name

    def getValue(self, attribute):
        """
        Returns the value of an attribute
        attribute is the name of the attribute (String)
        """
        parameters = {
            "name" : attribute,
            "value" : self._valueMap[attribute].data
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
        print(self._valueMap)
        zwaveVal = self._valueMap[attribute]
        checkedVal = zwaveVal.check_data(value)
        logger.debug("Received request to set value of attribute: " + attribute)         
        if checkedVal == None:
            raise ValueError("Invalid value for parameter " + attribute + " of attribute " + attribute + ": " + value)
        else:
            logger.debug("Attempting to set attribute: " + str(attribute) + " to value " + str(value))
            zwaveVal.data = checkedVal
            return self.buildParamChange(zwaveVal)


    def processEvent(self, val):
        parameters = []
        parameterChange = self.buildParamChange(val)
        parameters.append(parameterChange)
        data = {
            'event' : 'device.event',
            'timestamp' : int(time.time()),
            'device' : self._node.name,
            'deviceType' : self._node.product_name,
            'attribute' : {
                'name' : val.label,
                'parameters' : parameters
            }
	}
        return data

