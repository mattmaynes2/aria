class Oracle:
    def __init__(self, data, trigger, expected):
        self.data = data
        self.broker = broker
        self.trigger = trigger
        self.expected = expected
        self.triggerCount = 0
        self.truePositive = 0
        self.falsePositiveCount = 0
        self.delegates = []

    def registerForEvents(delegate):
        self.delegates.append(delegate)

    def messageIsExpectedAction(message):
        return message == self.expected

    def messageIsTriggerEvent(message):
        return message == self.trigger

    def received(self, message):
        if (messageIsTriggerEvent(message)):
            self.triggerCount += 1

        if (messageIsExpectedAction()):
            if (self.triggerCount > self.expectedCount):
                self.expectedCount += 1
            else:
                self.falsePositiveCount += 1

    def run (self, message):
        if not self.delegates:
            throw Exception("Nothing is registered for events")




