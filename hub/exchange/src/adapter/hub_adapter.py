import logging
from .message import Message
from .adapter import Adapter

log = logging.getLogger(__name__)

class HubAdapter (Adapter):

    def __init__ (self, hub):
        super().__init__()
        self.hub = hub

    def send (self, message):
        if ('get' in message.data):
            attribute=message.data['get']
            value=self.hub.getCommand(attribute)
            self.notifyResponse(attribute,value,message.sender)
            return True
        elif('set' in message.data and 'value' in message.data):
            attribute= message.data['set']
            value=message.data['value']
            try:
                responseValue=self.hub.setCommand(attribute,value)
                self.notifyResponse(attribute,responseValue,message.sender)
                return True
            except Exception as e:
                log.exception("Invalid set message "+ str(message))
                self.notifyFailure(message.sender)
        return False

    def notifyResponse(self,attribute,responseValue,receiver):
        self.notify(
        'received',
        Message(type_= Message.Ack,data = {'response':attribute,\
        'value':responseValue},
        sender = self.hub.address, receiver = receiver)
        )

    def notifyFailure(self,receiver):
        self.notify(
        'received',
        Message(type_= Message.Error,data = {'response':'Invalid Message'},
        sender = self.hub.address, receiver = receiver)
        )
