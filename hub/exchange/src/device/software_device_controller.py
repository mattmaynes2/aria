from .device import Device
from .device import DeviceType
from .device import Attribute
from .device import DataType
from .device import ObservableDevice

class SoftwareDeviceController(ObservableDevice):

    def __init__(self):
        deviceListAttribute = Attribute("deviceList", DataType.List)
        deviceType = DeviceType("SoftwareDeviceController", "software", "cameron",\
         isControllable = True, attributes = [deviceListAttribute])
        self.device = []
        super().__init__()

    def send(self, message):
        """
        This will receive messages pertaining to control of software devices
        """
        if message.data["get"] == "deviceList" :
            self.notify(self.devices)


    

