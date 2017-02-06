from hub.commands import Command
from hub.commands.command_type import CommandType

class SetHubNameCommand(Command):
    def __init__(self):
        super().__init__(self,CommandType.SET,'name')
    
    def execute(hub,data):
        hub.name=name
        return hub.name