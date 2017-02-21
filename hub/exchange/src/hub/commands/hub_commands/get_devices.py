from hub.commands import Command
from hub.commands.command_type import CommandType

class GetDevicesCommand(Command):
    def __init__(self):
        super().__init__(CommandType.GET,'devices')
    
    def execute(self,hub,data):
        deviceList = []
        for device in hub.devices.values():
            device.refreshValues()
            deviceList.append(device)

        return deviceList