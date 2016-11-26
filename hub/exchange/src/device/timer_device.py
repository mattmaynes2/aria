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
        myType = self.getDeviceType()
        super().__init__(myType)
        self.uuid = uuid.uuid4().bytes
        self.period = period
    
    @staticmethod
    def getDeviceType():
        return DeviceType("timer", "software", "cameron")

    """
    Get this device's UUID
    """
    def get_uuid(self):
        return self.uuid

    def tick(self, lastTime):
        time = datetime.datetime.now()
        if time >= (lastTime + self.period):
            latestTime = time
            for listener in self.eventListeners:
                listener(self.uuid, {"value" : time})

        def next():
            self.tick(latestTime)

        self.timer = threading.Timer(self.period.total_seconds(), next)
        self.timer.start()

    def stop(self):
        self.timer.cancel()
        self.timer.join()

    def start(self):
        self.tick(datetime.datetime.now())