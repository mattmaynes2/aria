from hub.commands import Command
from hub.commands.command_type import CommandType

class GetHubStatusCommand(Command):
    def __init__(self):
        super().__init__(CommandType.GET,'status')
    
    def execute(self,hub,data):
        return hub.status