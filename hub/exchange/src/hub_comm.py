import comm
import message

class HubComm (comm.Comm):

    def __init__ (self, hub):
        super().__init__()
        self.hub = hub

    def setup (self, listener):
        self.listener = listener

    def send (self, msg):
        if ('action' in msg.data and msg.data.action == 'status'):
            self.listener.message(
                message.Message(
                    data  = self.hub.status(),
                    sender = message.default,
                    receiver = msg.sender
                    )
            )


