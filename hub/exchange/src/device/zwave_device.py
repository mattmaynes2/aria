from .device import Device
from .parameter import Parameter
from .data_types import DataType
from .attribute import Attribute
from .device_type import DeviceType
import time

import uuid

class ZWaveDevice(Device):
    PROTOCOL='zwave'
    dataMappings={'Bool':DataType.Binary,'Byte':DataType.Byte, 'Decimal':DataType.Float,\
    'Int':DataType.Int, 'Short':DataType.Int, 'String':DataType.String, 'Button':DataType.Binary, \
    'List':DataType.List}

    def __init__ (self, node):
        self.__valueMap = {}
        super().__init__(self._getDeviceType(node), name = node.name,address=uuid.uuid4().bytes,\
        version=str(node.version))
        self.__node = node

    def _getDeviceType(self, node):
        attributes = []
        for key,val in node.get_values(genre='User').items():
            parameter= Parameter(val.label, ZWaveDevice.dataMappings[val.type],max_=val.max, \
            min_=val.min, value=val.data)
            attribute=Attribute(val.label,parameters=[parameter],isControllable=not val.is_read_only)
            attributes.append(attribute)
            self.__valueMap[val.label] = val

        return DeviceType(node.product_name, ZWaveDevice.PROTOCOL, node.manufacturer_name,\
        attributes=attributes)


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

    def processEvent(self, val):
        parameters = []
        parameterChange = {
            'name' : val.label,
            'value' : val.data,
            'dataType' : ZWaveDevice.dataMappings[val.type]
        }
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

