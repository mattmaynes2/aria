from .database_command import DatabaseCommand
from .command_type import CommandType
from database import Retriever

class CreateSessionCommand(DatabaseCommand):
    def __init__(self, database):
        super().__init__(CommandType.CREATE,'session',database)
    
    def execute(self,hub,data):
        name=data['name']
        behaviourId=data['behaviourId']
        session= self.retriever.addSession(behaviourId,name)
        session['created_date']=self.formatDate(session['created_date'])
        return self._formatColumnNames(session)