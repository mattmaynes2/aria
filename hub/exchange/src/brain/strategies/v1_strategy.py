
class V1Strategy():

    def __init__(self, triggeredEvent):
        self.triggeredEvent = triggeredEvent

    def decide(self, event):
        return self.triggeredEvent
