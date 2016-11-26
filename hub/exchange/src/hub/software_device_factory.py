from device import TimerDevice

class SoftwareDeviceFactory:

    """
    Returns a list of device types that the factory can create
    """
    @staticmethod
    def getAvailableDevices():
        devices = []
        devices.append(TimerDevice.getDeviceType())
        return devices