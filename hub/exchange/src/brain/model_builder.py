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
    
    def createStrategy(self,events):
        for event in reversed(events):
            if event['request_id']:
                message = Message(Message.Request, data=
                {
                    'set':event['attribute_name'],
                    'value':[{'name':event['parameter_name'], 'value':event['value']}]
                }, receiver=UUID(event['source']).bytes)
                return V1Strategy(message)
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

            

