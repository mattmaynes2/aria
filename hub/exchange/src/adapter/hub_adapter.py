from .message import Message
from .adapter import Adapter


class HubAdapter (Adapter):

    def __init__ (self, hub):
        super().__init__()
        self.hub = hub

    def send (self, message):
        if ('action' not in message.data):
            return False
        self.notify(
            'received',
            Message(type_= Message.Ack,data = self.hub.command(message.data['action']), 
            sender = Message.DEFAULT_ADDRESS, receiver = message.sender)
            )


