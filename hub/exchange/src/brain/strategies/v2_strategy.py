from uuid import UUID
from ipc import Message
from .decision_broker import MACHINE_LEARNING_ADDRESS
import logging

logger = logging.getLogger(__name__)
fileHandler = logging.FileHandler('Decisions.log')
logger.addHandler(fileHandler)
logger.setLevel(logging.DEBUG)

class V2Strategy():

    def __init__(self):
        self.eventMapping = {}

    def addDecision(self, triggeringEvent, action):
        triggerString = self.buildEventIdentifierFromDatabaseObject(triggeringEvent)
        logger.debug("Adding decision for trigger string " + triggerString)
        logger.debug("The action taken will be " + str(action))
        if triggerString not in self.eventMapping:
            self.eventMapping[triggerString] = []

        self.eventMapping[triggerString].append(action)

    # It is assumed that the list of events passed to the strategy are sorted by time of occurance
    def processSession(self, events,state=None):
        logger.debug("Processing data from a new session")
        for i, event in enumerate(events):
            if event['request_id']:
                logger.debug("Found a request made during the session")
                triggeringEvent = self.findLastEventBefore(i, events)
                if (triggeringEvent):
                    message=self.buildMessageFromEvent(event)
                    self.addDecision(triggeringEvent, message)

    def buildMessageFromEvent(self,event):
        return Message(Message.Request, data=
                {
                    'set':event['attribute_name'],
                    'value':[{'name':event['parameter_name'],
                    'value':event['value']}]
            }, receiver=UUID(event['source']).bytes, sender=MACHINE_LEARNING_ADDRESS )
                    

    def findLastEventBefore(self, index, eventList):
        for event in reversed(eventList[:index]):
            if not event["request_id"]:
                logger.debug("Found a trigger event for the request")
                return event

    def buildEventIdentifierFromMessage(self, message):
        source = str(UUID(bytes=message.sender))
        attributeName = message.data["attribute"]["name"]
        parameterName = message.data["attribute"]["parameters"][0]["name"]
        value = message.data["attribute"]["parameters"][0]["value"]
        return self.buildEventIdentifier(source, attributeName, parameterName, value)

    def buildEventIdentifierFromDatabaseObject(self, event):
        return self.buildEventIdentifier(event['source']  
                                , event['attribute_name']
                                , event['parameter_name']
                                , event['value'])

    def buildEventIdentifier(self, source, name, parameter, value):
        return str(source) + str(name) + str(parameter) + str(value)

    def decide(self, event):
        logger.debug("Looking for decision for event " + str(event))
        eventString = self.buildEventIdentifierFromMessage(event)
        logger.debug("Looking for decision for trigger string " + eventString)

            
        decision=self.getDecision(eventString)
        if decision :
           logger.debug("Found a decision " + str(decision))
        return decision


    def getDecision(self,eventString):
        return self.eventMapping.get(eventString,[])