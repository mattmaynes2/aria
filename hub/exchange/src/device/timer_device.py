import datetime
import uuid
import threading
import logging
from .device_type import DeviceType
from .observable import Observable
from .attribute import Attribute
from .data_types import DataType

logger = logging.getLogger(__name__)

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
        attributes = []
        attributes.append(Attribute("time", DataType.String))
        attributes.append(Attribute("period", DataType.Int))
        return DeviceType("timer", "software", "cameron", attributes)

    """
    Get this device's UUID
    """
    def get_uuid(self):
        return self.uuid

    def tick(self, lastTime):
        logger.info("TICK")
        time = datetime.datetime.now()
        period = datetime.timedelta(seconds = self.period)
        if time >= (lastTime + period):
            latestTime = time
            #for listener in self.eventListeners:
             #   listener(self.uuid, {"value" : time})
        else:
            latestTime = lastTime

        def next():
            self.tick(latestTime)

        self.timer = threading.Timer(period.total_seconds(), next)
        self.timer.start()

    def stop(self):
        self.timer.cancel()
        self.timer.join()

    def start(self):
        self.tick(datetime.datetime.now())