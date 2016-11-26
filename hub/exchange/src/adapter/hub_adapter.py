import logging
from ipc import Message
from .adapter import Adapter

log = logging.getLogger(__name__)

class HubAdapter (Adapter):

    def __init__ (self, hub):
        super().__init__()
        self.hub = hub

    def send (self, message):
        if ('get' in message.data):
            attribute=message.data['get']
            params=message.data
            try:
                value=self.hub.getCommand(attribute,params)
                self.notifyResponse(attribute,value,message.sender)
                return True
            except Exception as e:
                 log.exception("Invalid get message "+ str(message))
        elif('set' in message.data and 'value' in message.data):
            attribute= message.data['set']
            value=message.data['value']
            try:
                responseValue=self.hub.setCommand(attribute,value)
                self.notifyResponse(attribute,responseValue,message.sender)
                return True
            except Exception as e:
                log.exception("Invalid set message "+ str(message))
                log.error('really what the fuck')
        elif(message.type == Message.Error):
            log.warning('Recieved error '+str(message))
            return False
        elif(message.type == Message.Event):
            # TODO Where do event messages actually go?
            return
        log.error('about to fail message is '+str(message))
        self.notifyFailure(message.sender)

    def notifyResponse(self,attribute,responseValue,receiver):
        self.notify(
        'received',
        Message(type_= Message.Ack,data = {'response':attribute,\
        'value':responseValue},
        sender = self.hub.address, receiver = receiver)
        )

    def notifyFailure(self,receiver):
        log.error('How in the fuck did I get here')
        self.notify(
        'received',
        Message(type_= Message.Error,data = {'response':'Invalid Message'},
        sender = self.hub.address, receiver = receiver)
        )
