from hub.commands import Command
from hub.commands.command_type import CommandType

class GetDevicesCommand(Command):
    def __init__(self):
        super().__init__(self,CommandType.GET,'devices')
    
    def execute(hub,data):
        return list(hub.devices.values())