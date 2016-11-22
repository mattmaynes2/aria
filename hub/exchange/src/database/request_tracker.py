import logging
from adapter import Message
from database import DatabaseTranslator 

log= logging.getLogger(__name__)


class RequestTracker(DatabaseTranslator):

    def __init__(self,databaseTranslator,hub):
        self.dbTranslator=databaseTranslator
        self.requests={}
        self.hub=hub

    def received(self,message):
        """
            decorates the receive of database translator to assosiate a request to a device
            with an event/response from a device. If a previous request doesn't exist
            for a device then this was a manual user action, a request is created for this 
            action.
        """
        device= self.hub if message.sender == self.hub.address else self.hub.getDevice(message.sender)
        if(not device):
            log.warning('Unknown sender')
            return False
        # ignore requests to hub they don't need to be logged
        if(Message.Request == message.type and message.receiver != self.hub.address):
            self.requests[message.receiver]=self.dbTranslator.received(message)
        elif(Message.Event == message.type or Message.Response == message.type):
            reqid=self.requests.pop(message.receiver,None)
            # don't create a request for a non controllable device
            if(reqid or not device.deviceType.isControllable):
                self.sendEvent(reqid,message)
            else:
                try:
                    msg=self.createRequest(message)
                    reqid=self.received(msg)
                    self.sendEvent(reqid,message)
                except Exception as e:
                    log.warning ('Invalid Event message '+str(message)+ str(e),exc_info=True)
        else:
            self.dbTranslator.received(message)
        
            
    def sendEvent(self,reqid,message):
        if(reqid):
            message.data['requestId']= reqid
        self.dbTranslator.received(message)
        
    def createRequest(self,message):
        # Event messages have the form {'response':<Atribute>, 'value':<value>}
        # Requests have the form {'set':<attribute>, 'value':<value> }
        data={'set':message.data['response'],'value':message.data['value']}
        return Message(type_=Message.Request,data=data,receiver=message.sender)

            
