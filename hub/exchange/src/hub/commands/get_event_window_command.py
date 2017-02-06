from .database_command import DatabaseCommand
from .command_type import CommandType
from database import Retriever

class GetEventWindowCommand(DatabaseCommand):
    def __init__(self, database):
        super().__init__(self,CommandType.GET,'eventWindow',database)
    
    def execute(self,hub,data):
        start=data['start']
        count=data['count']
        ignore=data.get('ignore','')
        if(ignore):
            ignore =",".join(ignore)
        results = self.retriever.getEventWindow(start,count,ignore)
        self.formatEvents(results)
        return {'total':len(results),'records':results}