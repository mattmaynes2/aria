from .database_command import DatabaseCommand
from .command_type import CommandType
from database import Retriever

class SetBehaviourCommand(DatabaseCommand):
    def __init__(self, database):
        super().__init__(CommandType.SET,'behaviour',database)
    
    def execute(self,hub,data):
        name=data.get('name')
        active= data.get('active')
        id_=data['id']
        result = self.retriever.updateBehaviour(id_,name,active)
        result['created_date']=self.formatDate(result['created_date'])
        result['last_updated']=self.formatDate(result['last_updated'])
        self._formatColumnNames(result)
        return result