from .database_command import DatabaseCommand
from .command_type import CommandType
from database import Retriever

class CreateBehavioursCommand(DatabaseCommand):
    def __init__(self, database):
        super().__init__(CommandType.CREATE,'behaviour',database)
    
    def execute(self,hub,data):
        name=data['name']
        behaviour = self.retriever.addBehaviour(name)
        behaviour['created_date']=self.formatDate(behaviour['created_date'])
        behaviour['last_updated']=self.formatDate(behaviour['last_updated'])
        return self._formatColumnNames(behaviour)