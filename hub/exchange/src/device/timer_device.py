import datetime
import uuid
import threading
import logging
from .device_type import DeviceType
from .observable import Observable
from .attribute import Attribute
from .data_types import DataType
from .parameter import Parameter
import sched, time

logger = logging.getLogger(__name__)

import sched, time

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
        self.runLock = threading.Lock()
        self.stopCondition = threading.Condition(self.runLock)
        self.running = False

        def tickClosure():
            self.tick(datetime.datetime.now())
        self.timerThread = threading.Thread(target=tickClosure)

    @staticmethod
    def getDeviceType():
        attributes = []
        attributes.append(Attribute("time", parameters=[Parameter("time",DataType.String)]))
        attributes.append(Attribute("period", parameters=[Parameter("period",DataType.Int)]))
        return DeviceType("timer", "software", "cameron", attributes)

    """
    Get this device's UUID
    """
    def get_uuid(self):
        return self.uuid

    def tickOnce(self, lastTime):
        logger.info("TICK " + str(lastTime))
        time = datetime.datetime.now()
        period = datetime.timedelta(seconds = self.period)

        with self.stopCondition:
            self.stopCondition.wait(self.period)

        if not self.running:
            return

        if time >= (lastTime + period):
            latestTime = time
            for listener in self.eventListeners:
                listener(self.uuid, {"event" : "device.event", "value" : str(time)})
        else:
            latestTime = lastTime
        return latestTime

    def tick(self, lastTime):
        latestTime = self.tickOnce(lastTime)
        if self.running:
            self.tick(latestTime)

    def stop(self):
        with self.runLock:
            self.running = False
            self.stopCondition.notify()
        self.timerThread.join()

    def start(self):
        with self.runLock:
            self.running = True
        self.timerThread.start()
