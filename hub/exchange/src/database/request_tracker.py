from adapter import Message
from database import DatabaseTranslator 

class RequestTracker(DatabaseTranslator):

    def __init__(self,databaseTranslator):
        self.dbTranslator=databaseTranslator
        self.requests={}

    def received(self,message):
        """
            decorates the receive of database translator to assosiate a request to a device
            with an event/response from a device. If a previous request doesn't exist
            for a device then this was a manual user action, a request is created for this 
            action.
        """
        if(Message.Request == message.type):
            self.requests[message.receiver]=self.databaseTranslator.received(message)
        elif(Message.Event == message.type or Message.Response == message.type):
            reqid=self.requests.pop(message.receiver,None)
            if(reqid):
                self.sendEvent(reqid,message)
            else:
                msg=self.createRequest(message)
                reqid=self.databaseTranslator.received(msg)

        else:
            self.databaseTranslator.received(message)
        
        
        def sendEvent(self,reqid,message):
            message.data['requestId']= reqid
            self.databaseTranslator.received(message)
        
        def createRequest(self,message):
            # Event messages have the form {attribute:value}
            # Requests have the form {'action':attribute, 'value':value }
            keys=list(message.data.keys())
            data={'action':keys[0],'value':message.data[keys[0]]}
            return Message(type_=Message.Request,data=data,receiver=message.sender)

            
