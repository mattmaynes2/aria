from .database_command import DatabaseCommand
from .command_type import CommandType
from database import Retriever

class GetEventWindowCommand(DatabaseCommand):
    def __init__(self, database):
        super().__init__(CommandType.GET,'eventWindow',database)
    
    def execute(self,hub,data):
        start=data['start']
        count=data['count']
        results = self.retriever.getEventWindow(start,count)
        self.formatEvents(results,hub)
        return {'total':len(results),'records':results}