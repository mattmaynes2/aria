from .database_command import DatabaseCommand
from .command_type import CommandType
from database import Retriever

class GetSessionsCommand(DatabaseCommand):
    def __init__(self, database):
        super().__init__(CommandType.GET,'sessions',database)
    
    def execute(self,hub,data):
        start=data['start']
        count=data['count']
        behaviourId=data['behaviourId']
        results = self.retriever.getSessionsWindow(start,count,behaviourId)
        for i,result in enumerate(results):
            result['created_date']=self.formatDate(result['created_date'])
            results[i] = self._formatColumnNames(result)
        return{'total':len(results),'records':results}