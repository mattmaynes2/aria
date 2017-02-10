from .command import Command
from .command_type import CommandType
from database import Retriever
import uuid
from datetime import datetime

class DatabaseCommand(Command):
    def __init__(self, commandType, name,database):
        super().__init__(commandType,name)
        self.retriever= Retriever(database)


    def formatEvents(self,events,hub):
        for event in events:
            source=event['source']
            if(source):
                device=hub.getDevice(uuid.UUID(source).bytes)
                if(device):
                    event['deviceType']=device.deviceType.name
            event['timestamp']=self.formatDate(event['timestamp'])

    def formatDate(self,date):
        time=datetime.strptime(date,'%Y-%m-%d %H:%M:%S')
        return int(time.timestamp()*1000)