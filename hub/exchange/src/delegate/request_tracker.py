import logging
from ipc import Message
from database import DatabaseTranslator 
from uuid import UUID

log= logging.getLogger(__name__)


class RequestTracker(DatabaseTranslator):

    def __init__(self,databaseTranslator,hub):
        super().__init__(databaseTranslator.database)
        self.dbTranslator=databaseTranslator
        self.requests={}
        self.hub=hub

    def received(self,message):
        """
            decorates the receive of database translator to associates a request to a device
            with an event/response from a device. If a previous request doesn't exist
            for a device then this was a manual user action, a request is created for this 
            action.
        """
        # ignore requests to hub they don't need to be logged
        if(Message.Request == message.type and message.receiver != self.hub.address):
            self.requests[message.receiver]=self.dbTranslator.received(message)
            return self.requests[message.receiver]
        elif(Message.Event == message.type):
            device= self.hub.getDevice(message.sender)
            if(not device):
                log.warning('Unknown sender '+str(UUID(bytes=message.sender)))
                return False
            reqid=self.requests.pop(message.sender,None)
            # don't create a request for a non controllable device
            attribute = device.getAttribute(message.data['attribute']['name'])
            if(not attribute):
                log.warning("{} dosen't have attribute {}".format(device.name,message.data.get('attribute')))
                return False
            if(reqid or not attribute.isControllable):
                self.sendEvent(reqid,message)
            else:
                try:
                    msg=self.createRequest(message)
                    reqid=self.received(msg)
                    # remove the request from the dict
                    self.requests.pop(message.sender,None)
                    self.sendEvent(reqid,message)
                except Exception as e:
                    log.error ('Invalid Event message '+str(message)+ str(e),exc_info=True)
        
            
    def sendEvent(self,reqid,message):
        if(reqid):
            message.data['requestId']= reqid
        self.dbTranslator.received(message)
        
    def createRequest(self,message):
        data={'set':message.data['attribute']['name'],'value': message.data['attribute']['parameters']}
        return Message(type_=Message.Request,data=data,receiver=message.sender,sender=message.sender)

            
