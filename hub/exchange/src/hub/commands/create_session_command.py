from .database_command import DatabaseCommand
from .command_type import CommandType
from database import Retriever

class CreateSessionCommand(DatabaseCommand):
    def __init__(self, database):
        super().__init__(CommandType.CREATE,'session',database)
    
    def execute(self,hub,data):
        name=data['name']
        behaviourId=data['behaviourId']
        _id = self.retriever.addSession(behaviourId,name)
        return {"id":_id}