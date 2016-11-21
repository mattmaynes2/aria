import datetime
import uuid
import threading

class TimerDevice():
    """
    TimerDevice calls a function at a certain configurable frequency
    TimerDevice(period, callback)
    period is the period at which the timer will generate events
    callback will be called for every event
    """

    def __init__(self, period):
        super().__init__()
        self.uuid = uuid.uuid4().bytes
        self.period = period
        self.eventListeners = []
        self.lastTime = datetime.datetime.now()
    
    """
    Get this device's UUID
    """
    def get_uuid(self):
        return self.uuid

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
                listener(self.uuid, {"value" : time})
        self.timer = threading.Timer(self.period.total_seconds(), self.tick)
        self.timer.start()

    def stop(self):
        self.timer.cancel()
        self.timer.join()

    def start(self):
        self.tick()