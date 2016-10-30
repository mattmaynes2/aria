from .message import Message
from .adapter import Adapter


class HubAdapter (Adapter):

    def __init__ (self, hub):
        super().__init__()
        self.hub = hub

    def send (self, message):
        if ('action' not in message.data):
            return False

        if (message.data['action'] == 'status'):
            self.notify(
                'received',
                Message(data = self.hub.status(), sender = Message.DEFAULT_ADDRESS, receiver = message.sender)
            )

