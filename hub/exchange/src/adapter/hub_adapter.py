import logging
from ipc import Message
from hub.commands import CommandType
from .adapter import Adapter

log = logging.getLogger(__name__)

class HubAdapter (Adapter):

    def __init__ (self, hub):
        super().__init__()
        self.hub = hub

    def send (self, message):
        if(message.type == Message.Error):
            log.warning('Recieved error '+str(message))
            return False
        elif(message.type == Message.Event):
            # TODO not sure what to do with events that go to the hub
            return
        for type in CommandType:
            if(type.value in message.data):           
                try:
                    value=self.hub.executeCommand(type,message.data)
                    self.notifyResponse(message.data[type.value],value,message.sender)
                    return True
                except Exception as e:
                    log.exception("Invalid message "+ str(message))
        self.notifyFailure(message.sender)

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
