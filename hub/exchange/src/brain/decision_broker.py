import logging
from ipc import Message
from delegate import Delegate

MACHINE_LEARNING_ADDRESS=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02'

log = logging.getLogger(__name__)

class DecisionBroker(Delegate):

    def __init__(self, adapter, hub,decisionStrategy=None):
        super().__init__()
        self.id=MACHINE_LEARNING_ADDRESS
        self.adapter = adapter
        self.hub=hub
        self.decisionStrategy = decisionStrategy

    def handleEventMessage(self, message):
        if (message.data["event"] == "device.event"):
            decisions = self.decisionStrategy.decide(message)
            for decision in decisions:
                decision.sender=self.id
                self.adapter.received(decision)

    def received(self, message):
        log.debug('received message {}'.format(message))
        if not self.decisionStrategy:
            log.debug('no strategy set')
            return
        if (self.hub.isNormalMode() and (message.type == Message.Event)):
            log.debug('handling the event')
            self.handleEventMessage(message)