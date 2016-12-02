from .device import Device
from .parameter import Parameter
from .data_types import DataType
import uuid

class ZWaveDevice(Device):
    PROTOCOL='zwave'
    dataMappings={'Bool':DataType.Binary,'Byte':DataType.Byte, 'Decimal':DataType.Float,\
    'Int':DataType.Int, 'Short':DataType.Int, 'String':DataType.String, 'Button':DataType.Binary, \
    'List':DataType.List}

    def __init__ (self, node):
        super().__init__(ZWaveDevice.getDeviceType(node), name = node.name,uuid.uuid4(),str(node.version))
        self._node = node
    
    @staticmethod
    def getDeviceType(node):
        attributes = []
        for key,val in node.get_values(genre='User').items():
            parameter= Parameter(val.label, ZWaveDevice.dataMappings[val.type],max_=val.max, \
            min_=val.min)
            attribute=Attribute(val.label,parameters=[parameter])
        return DeviceType(node.product_name, ZWaveDevice.PROTOCOL, node.manufacturer_name, attributes)