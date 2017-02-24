import logging
from ipc import Message
from delegate import Delegate

log= logging.getLogger(__name__)

class ModelBuilder(Delegate):
    
    def __init__(self,retriever):
        self.retriever =retriever
    
    def received(self,message):
        if message.type == Message.Request and isSessionStopMessage(message):
            events=self.retriever.getSessionEvents(message.data['id'])
    
def isSessionStopMessage(message):
    data= message.data
    return data.get('deactivate',None) == 'session'
