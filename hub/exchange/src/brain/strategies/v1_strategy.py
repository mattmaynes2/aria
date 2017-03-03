
class V1Strategy():

    def __init__(self):
        self.triggeredEvent = None

    def processSession(self, events):
        for event in reversed(events):
            if event['request_id']:
                message = Message(Message.Request, data=
                {
                    'set':event['attribute_name'],
                    'value':[{'name':event['parameter_name'], 'value':event['value']}]
                }, receiver=UUID(event['source']).bytes)
                self.triggeredEvent = message

    def decide(self, event):
        return self.triggeredEvent
