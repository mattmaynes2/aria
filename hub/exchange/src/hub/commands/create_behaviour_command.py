from .database_command import DatabaseCommand
from .command_type import CommandType
from database import Retriever

class CreateBehavioursCommand(DatabaseCommand):
    def __init__(self, database):
        super().__init__(CommandType.CREATE,'behaviours',database)
    
    def execute(self,hub,data):
        name=data['name']
        results = self.retriever.addBehaviour(name)
        return results