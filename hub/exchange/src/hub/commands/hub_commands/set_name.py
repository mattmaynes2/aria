from hub.commands import Command
from hub.commands.command_type import CommandType

class SetHubNameCommand(Command):
    def __init__(self):
        super().__init__(CommandType.SET,'name')
    
    def execute(self,hub,data):
        hub.name=data['value']
        return hub.name