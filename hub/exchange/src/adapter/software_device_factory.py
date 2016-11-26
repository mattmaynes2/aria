from device import TimerDevice

class SoftwareDeviceFactory():

    def loadDevicesFromFile(self, file_name, adapter):
        with open(file_name, 'r') as f:
            conf = json.load(f)

    def _createListOfDevices(deviceList, adapter):
        return [adapter.createDevice(device) for device in deviceList]

    def createDevice(self, config):
        if (config['type'].lower() == 'timer'):
            return TimerDevice(config['period'])
    
