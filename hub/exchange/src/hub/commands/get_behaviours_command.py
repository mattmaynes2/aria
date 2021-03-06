from .database_command import DatabaseCommand
from .command_type import CommandType
from database import Retriever

class GetBehavioursCommand(DatabaseCommand):
    def __init__(self, database):
        super().__init__(CommandType.GET,'behaviours',database)
    
    def execute(self,hub,data):
        start=data['start']
        count=data['count']
        results = self.retriever.getBehaviourWindow(start,count)
        for i,result in enumerate(results):
            result['created_date']=self.formatDate(result['created_date'])
            result['last_updated']=self.formatDate(result['last_updated'])
            results[i] = self._formatColumnNames(result)
        return{'total':len(results),'records':results}