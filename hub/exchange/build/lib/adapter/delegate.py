class Delegate:
    def discovered (self, device):
        """Invoked when a new device is discovered

        Arguments:
            device (Device): Device that was discovered
        """
        pass

    def received (self, message):
        """Invoked when a message is received by an adapter

        Arguments:
            message (Message): Message that was received
        """
        pass
