import logging
from ipc import Message
from delegate import Delegate
from .strategies.v1_strategy import V1Strategy
from uuid import UUID

log= logging.getLogger(__name__)

class ModelBuilder(Delegate):
    
    def __init__(self,retriever, decisionBroker):
        self.retriever =retriever
        self.decisionBroker=decisionBroker
    
    def received(self,message):
        if message.type == Message.Request and isSessionStopMessage(message):
            events=self.retriever.getSessionEvents(message.data['id'])
            
            strategy=self.createStrategy(events)
            log.debug('setting strategy {}'.format(strategy.triggeredEvent))
            self.decisionBroker.decisionStrategy=strategy
    
    def createStrategy(self,events):
        for event in reversed(events):
            if event['request_id']:
                message = Message(Message.Request, data=
                {
                    'set':event['attribute_name'],
                    'value':[{'name':event['parameter_name'], 'value':event['value']}]
                }, receiver=UUID(event['source']).bytes)
                return V1Strategy(message)

def isSessionStopMessage(message):
    data= message.data
    return data.get('deactivate',None) == 'session'

            

