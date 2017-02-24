from ipc import Message
from delegate import Delegate

class Model(Delegate):

    def __init__(self, adapter, decisionStrategy):
        super().__init__()
        self.adapter = adapter
        self.decisionStrategy = decisionStrategy

    def handleEventMessage(self, data):
        if (data["event"] == "device.event"):
            decision = self.decisionStrategy.decide(data)
            if (decision):
                self.adapter.send(decision)

    def received(self, message):
        if (message.type == Message.Event):
            self.handleEventMessage(message.data)