from hub.commands import Command
from hub.commands.command_type import CommandType

class GetHubModeCommand(Command):
    def __init__(self):
        super().__init__(self,CommandType.GET,'mode')
    
    def execute(hub,data):
        return hub.mode