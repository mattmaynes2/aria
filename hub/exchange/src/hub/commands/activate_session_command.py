import logging
from .database_command import DatabaseCommand
from .command_type import CommandType
from hub.hub_mode import HubMode

log = logging.getLogger(__name__)

class ActivateSessionCommand(DatabaseCommand):
    def __init__(self,database):
        super().__init__(CommandType.ACTIVATE,'session',database)
    
    def execute(self,hub,data):
        session=self.retriever.getSession(data['id'])
        if( not bool(session['stopped'])):
            hub.session=_session(session)
            hub.mode=HubMode.Learning
            return 'Success'
        raise ValueError("Session {} has already been captured".format(session['name']))

# change the database dictionary into a session object
class _session:
    def __init__(self,dict):
        self.__dict__=dict