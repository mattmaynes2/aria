from .command import Command
from .command_type import CommandType
from hub.hub_mode import HubMode

class DeactivateSessionCommand(Command):
    def __init__(self):
        super().__init__(CommandType.DEACTIVATE,'session')
    
    def execute(self,hub,data):
        if int(data['id']) == int(hub.session.id):
            hub.session=None
            hub.mode=HubMode.Normal
            return 'Success'
        raise ValueError("Invalid session id {}".format(data.get('id')))

# change the database dictionary into a session object
class _session:
    def __init__(self,dict):
        self.__dict__=dict