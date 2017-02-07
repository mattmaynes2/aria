from .database_command import DatabaseCommand
from .command_type import CommandType
from database import Retriever

class GetBehavioursCommand(DatabaseCommand):
    def __init__(self, database):
        super().__init__(CommandType.GET,'behaviours',database)
    
    def execute(self,hub,data):
        id_=data['id']
        start=data['start']
        count=data['count']
        results = self.retriever.getBehaviourWindow(id_,start,count)
        for result in results:
            result['created_date']=self.fromatDate(result['created_date'])
            result['last_updated']=self.formatDate(result['last_updated'])
        return{'total':len(results),'records':results}