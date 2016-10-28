import comm
import message

class HubComm (comm.Comm):

    def __init__ (self, hub):
        self.hub = hub

    def setup (self, listener):
        self.listener = listener

    def send (msg):
        if (msg.data.action == 'status')
            listener.message(
                message.Message(
                data  = self.hub.status(),
                sender = message.default,
                receiver = msg.sender
                )


