from .database_command import DatabaseCommand
from .command_type import CommandType
from hub.hub_mode import HubMode

class DeactivateSessionCommand(DatabaseCommand):
    def __init__(self,database):
        super().__init__(CommandType.DEACTIVATE,'session',database)
    
    def execute(self,hub,data):
        sessionId=int(data['id'])
        if  sessionId == int(hub.session.id):
            hub.session=None
            self.retriever.stopSession(sessionId)
            hub.mode=HubMode.Normal
            return 'Success'
        raise ValueError("Invalid session id {}".format(data.get('id')))

# change the database dictionary into a session object
class _session:
    def __init__(self,dict):
        self.__dict__=dict