from device import Device 

class Observable(Device):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.eventListeners = []

    """
    Register a callback to be called when the timer fires
    callback should take one datetime argument
    """
    def registerEventCallback(self, callback):
        self.eventListeners.append(callback)

    def notify(self, data):
        for listener in self.eventListeners:
            listener(self.address, data)