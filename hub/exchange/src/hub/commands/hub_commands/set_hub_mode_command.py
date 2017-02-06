from hub.commands import Command
from hub.commands.command_type import CommandType

class SetHubModeCommand(Command):
    def __init__(self):
        super().__init__(self,CommandType.SET,'mode')
    
    def execute(hub,data):
        hub.mode=setMode(data['value'])
        return hub.mode