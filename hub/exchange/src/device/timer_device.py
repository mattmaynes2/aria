import datetime
import uuid
import threading
from .device_type import DeviceType
from .observable import Observable

class TimerDevice(Observable):
    """
    TimerDevice calls a function at a certain configurable frequency
    TimerDevice(period, callback)
    period is the period at which the timer will generate events
    callback will be called for every event
    """

    def __init__(self, period):
        myType = getDeviceType
        super().__init__(myType)
        self.uuid = uuid.uuid4().bytes
        self.period = period
        self.lastTime = datetime.datetime.now()
    
    @staticmethod
    def getDeviceType():
        return DeviceType("timer", "software", "cameron")

    """
    Get this device's UUID
    """
    def get_uuid(self):
        return self.uuid

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