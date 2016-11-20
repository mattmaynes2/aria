import datetime
from threading import Thread

class TimerDevice(Thread):
    """
    TimerDevice calls a function at a certain configurable frequency
    TimerDevice(period, callback)
    period is the period at which the timer will generate events
    callback will be called for every event
    """

    def __init__(self, period):
        super().__init__()
        self.period = period
        self.eventListeners = []
        self.lastTime = datetime.datetime.now()
    
    """
    Register a callback to be called when the timer fires
    callback should take one datetime argument
    """
    def registerEventCallback(self, callback):
        self.eventListeners.append(callback)

    def tick(self):
        time = datetime.datetime.now()
        if time >= (self.lastTime + self.period):
            self.lastTime = time
            for listener in self.eventListeners:
                listener(time)

    def run():
        
