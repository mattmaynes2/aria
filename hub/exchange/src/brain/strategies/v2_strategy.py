from uuid import UUID
from ipc import Message


class V2Strategy():

    def __init__(self):
        self.eventMapping = {}

    def addDecision(self, triggeringEvent, action):
        triggerString = self.makeEventStringFromDatabase(triggeringEvent)
        print("Adding decision for trigger string " + triggerString)
        if triggerString not in self.eventMapping:
            self.eventMapping[triggerString] = []

        self.eventMapping[triggerString].append(action)

    # It is assumed that the list of events passed to the strategy are sorted by time of occurance
    def processSession(self, events):
        for i, event in enumerate(events):
            if event['request_id']:
                triggeringEvent = self.findLastEventBefore(i, events)
                if (triggeringEvent):
                    message = Message(Message.Request, data=
                    {
                        'set':event['attribute_name'],
                        'value':[{'name':event['parameter_name'], 'value':event['value']}]
                    }, receiver=UUID(event['source']).bytes)
                    self.addDecision(triggeringEvent, message)

    def findLastEventBefore(self, index, eventList):
        for event in reversed(eventList[:index]):
            if not event["request_id"]:
                return event

    def makeEventStringFromEventMessage(self, event):
        source = str(UUID(bytes=event.sender))
        attributeName = event.data["attribute"]["name"]
        parameterName = event.data["attribute"]["parameters"][0]["name"]
        value = event.data["attribute"]["parameters"][0]["value"]
        return self.buildEventString(source, attributeName, parameterName, value)

    def makeEventStringFromDatabase(self, event):
        return self.buildEventString(event['source']  
                                , event['attribute_name']
                                , event['parameter_name']
                                , event['value'])

    def buildEventString(self, source, name, parameter, value):
        return source + name + parameter + value

    def decide(self, event):
        eventString = self.makeEventStringFromEventMessage(event)
        print("Looking for decision for trigger string " + eventString)

        if eventString in self.eventMapping:
            return self.eventMapping[eventString]
        return []