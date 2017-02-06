from .database_command import DatabaseCommand
from .command_type import CommandType
from database import Retriever

class GetDeviceEventsCommand(DatabaseCommand):
    def __init__(self, database):
        super().__init__(self,CommandType.GET,'deviceEvents',database)
    
    def execute(hub,data):
        id_=data['id']
        start=data['start']
        count=data['count']
        results = self.retriever.getEventWindow(id_,start,count)
        self.formatEvents(results)
        return{'total':len(results),'records':results}