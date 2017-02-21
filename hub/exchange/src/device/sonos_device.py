from .device import Device
from .parameter import Parameter
from .data_types import DataType
from .attribute import Attribute
from .device_type import DeviceType
import time
import logging
import uuid

logger = logging.getLogger(__name__)

class SonosQueue():
    
    def __init__(self,device):
        self.__device=device

    def put(self,item, block=True, timeout=None):
        self.__device.handleEvent(item)

class SonosDevice(Device):

    PROTOCOL ='sonos'

    def __init__(self,device):
        self.__device=device
        self.__queue=SonosQueue(self)
        self.__device.avTransport.subscribe(auto_renew=True,event_queue=self.__queue)
        self.__device.renderingControl.subscribe(auto_renew=True,event_queue=self.__queue)


    def handleEvent(event):
        print(str(event))

    