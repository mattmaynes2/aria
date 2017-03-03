import logging
from ipc import Message
from delegate import Delegate
from uuid import UUID

log= logging.getLogger(__name__)

class ModelBuilder(Delegate):
    
    def __init__(self,retriever, decisionBroker,strategy):
        self.retriever =retriever
        self.decisionBroker=decisionBroker
        self.strategy=strategy
    
    def received(self,message):
        if message.type == Message.Request and isSessionStopMessage(message):
            events=self.retriever.getSessionEvents(message.data['id']) 
            self.strategy.processSession(events)
    
    @property
    def strategy (self):
        return self.__strategy

    @strategy.setter
    def strategy(self, strategy):
        self.__strategy=strategy
        log.debug('setting Decision Broker to {}'.format(strategy))
        self.decisionBroker.decisionStrategy=strategy

def isSessionStopMessage(message):
    data= message.data
    return data.get('deactivate',None) == 'session'

            

