import logging
from .database_command import DatabaseCommand
from .command_type import CommandType
from database import Retriever

log = logging.getLogger(__name__)

class DeleteSessionCommand(DatabaseCommand):
    def __init__(self, database):
        super().__init__(CommandType.DELETE,'session',database)
    
    def execute(self,hub,data):
        _id=data['id']
        log.info("Deleteing Session id: {}".format(_id))
        self.retriever.deleteSession(_id)