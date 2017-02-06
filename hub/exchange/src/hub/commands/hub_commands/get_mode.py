from hub.commands import Command
from hub.commands.command_type import CommandType

class GetHubModeCommand(Command):
    def __init__(self):
        super().__init__(CommandType.GET,'mode')
    
    def execute(self,hub,data):
        return hub.mode