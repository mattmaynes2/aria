from hub.commands import Command
from hub.commands.command_type import CommandType

class GetHubNameCommand(Command):
    def __init__(self):
        super().__init__(CommandType.GET,'name')
    
    def execute(self,hub,data):
        return hub.name