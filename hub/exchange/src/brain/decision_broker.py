from ipc import Message
from delegate import Delegate

MACHINE_LEARNING_ADDRESS=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02'

class DecisionBroker(Delegate):

    def __init__(self, adapter, hub,decisionStrategy=None):
        super().__init__()
        self.id=MACHINE_LEARNING_ADDRESS
        self.adapter = adapter
        self.hub=hub
        self.decisionStrategy = decisionStrategy

    def handleEventMessage(self, data):
        if (data["event"] == "device.event"):
            decision = self.decisionStrategy.decide(data)
            if (decision):
                decision.sender=self.id
                self.adapter.received(decision)

    def received(self, message):
        if not self.decisionStrategy:
            return
        if (self.hub.isNormalMode() and message.type == Message.Event):
            self.handleEventMessage(message.data)