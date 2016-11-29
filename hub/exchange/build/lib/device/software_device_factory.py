from device import TimerDevice
import logging

logger = logging.getLogger(__name__)

class SoftwareDeviceFactory:

    @classmethod
    def setDeviceListener(cls, registrationFunction):
        cls.registerFunction = registrationFunction

    @staticmethod
    def getSoftwareAdapter(self):
        return self.adapter

    """
    Returns a list of device types that the factory can create
    """
    @staticmethod
    def getAvailableDevices():
        devices = []
        devices.append(TimerDevice.getDeviceType())
        return devices

    """
    Adds a new software device to the system
    """
    @classmethod
    def create(cls, deviceArgs):
        if deviceArgs['name'] == 'timer':
            device = TimerDevice(**deviceArgs['config'])
            cls.registerFunction(device)
            device.start()
            return device