import logging
from .database_command import DatabaseCommand
from .command_type import CommandType
from database import Retriever

log = logging.getLogger(__name__)

class DeleteBehaviourCommand(DatabaseCommand):
    def __init__(self, database):
        super().__init__(CommandType.DELETE,'behaviour',database)
    
    def execute(self,hub,data):
        _id=data['id']
        log.info("Deleteing Behaviour id: {}".format(_id))
        self.retriever.deleteBehaviour(_id)