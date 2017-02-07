from hub.commands import Command
from hub.commands.command_type import CommandType

class SetHubModeCommand(Command):
    def __init__(self):
        super().__init__(CommandType.SET,'mode')
    
    def execute(self,hub,data):
        hub.setMode(data['value'])
        return hub.mode