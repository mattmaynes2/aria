import logging
from ipc import Message
from delegate import Delegate
from uuid import UUID

log= logging.getLogger(__name__)

class ModelBuilder(Delegate):
    
    def __init__(self,retriever, decisionBroker,strategy,devices):
        self.retriever =retriever
        self.decisionBroker=decisionBroker
        self.strategy=strategy
        self.devices=devices
        self.state=[]
    
    def received(self,message):
        if message.type == Message.Request and isSessionStartMessage(message):
            self.state=self.getState()
        elif message.type == Message.Request and isSessionStopMessage(message):
            events=self.retriever.getSessionEvents(message.data['id']) 
            self.strategy.processSession(events,self.state)
    
    @property
    def strategy (self):
        return self.__strategy

    @strategy.setter
    def strategy(self, strategy):
        self.__strategy=strategy
        log.debug('setting Decision Broker to {}'.format(strategy))
        self.decisionBroker.decisionStrategy=strategy

    def getState(self):
        state=[]
        for device in self.devices:
            state.append({"device":device.address,"attributes":\
                    [dict(attribute) for attribute in device.deviceType.attributes]})
        log.debug("Current State: {}".format(state))
        return state

def isSessionStopMessage(message):
    data= message.data
    return data.get('deactivate',None) == 'session'

def isSessionStartMessage(message):
    data= message.data
    return data.get('activate',None) == 'session'

            

