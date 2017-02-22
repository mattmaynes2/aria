import time
import logging
import uuid
from .device import Device
from .parameter import Parameter
from .data_types import DataType
from .attribute import Attribute
from .device_type import DeviceType
from ipc import Message

logger = logging.getLogger(__name__)

# turn soco logger to error 
_SOCO_LOGGER = logging.getLogger('soco')
_SOCO_LOGGER.setLevel(logging.ERROR)
_REQUESTS_LOGGER = logging.getLogger('requests')
_REQUESTS_LOGGER.setLevel(logging.ERROR)

class SonosQueue():
    
    def __init__(self,device):
        self.__device=device

    def put(self,item, block=True, timeout=None):
        self.__device.handleEvent(item)

class SonosDevice(Device):

    PROTOCOL ='sonos'
    # list of parameters that use the Master key for current value
    MASTERVALS=['volume','mute','loudness']
    def __init__(self, device,adapter):
        self.__device=device
        self.__adapter=adapter
        # fromat UID from device into UUID
        address= uuid.UUID(bytes=bytes(device.uid.replace('RINCON_',''),'utf-8')[:16])
        info =device.get_speaker_info()
        name =info['zone_name']
        version= info['display_version']
        super().__init__(self._buildDeviceType(),name,address.bytes,version,
            icon='http://{}:1400{}'.format(self.__device.ip_address,info.get('player_icon')))
        self.__queue=SonosQueue(self)
        self.__device.avTransport.subscribe(auto_renew=True,event_queue=self.__queue)
        self.__device.renderingControl.subscribe(auto_renew=True,event_queue=self.__queue)
    
    def _buildDeviceType(self):
        attributes=[]
        info = self.__device.speaker_info

        attributes.append(Attribute('bass',[Parameter('bass',DataType.Int,min_=-10,max_=10,
        value=self.__device.bass)]))
        attributes.append(Attribute('treble',[Parameter('treble',DataType.Int,min_=-10,max_=10,
        value=self.__device.treble)]))
        attributes.append(Attribute('loudness',[Parameter('loudness',DataType.Binary,
        value=self.__device.loudness)]))
        attributes.append(Attribute('volume',[Parameter('volume',DataType.Int,min_=0,max_=100,
        value=self.__device.volume)]))
        attributes.append(Attribute('mute',[Parameter('mute',DataType.Binary,
        value=self.__device.mute)]))
        return DeviceType(info['model_name'],SonosDevice.PROTOCOL,attributes=attributes)

    def handleEvent(self,event):
        print("service: {}".format(type(event.service)))
        print("variables: {}".format(event.variables))
        print("timestamp: {}".format(event.timestamp))
        if event.service == self.__device.avTransport :
            pass
        elif event.service == self.__device.renderingControl:
            attribute=self._handleRenderingEvent(event)
            data = {
                'event' : 'device.event',
                'timestamp' : int(event.timestamp*1000),
                'device' : self.name,
                'deviceType' : self.deviceType.name,
                'attribute' : attribute
                }
            self.__adapter.received(Message(Message.Event,data,sender=self.address))


    def handleRequest(self, request):
        pass
    
    def _handleRenderingEvent(self,event):
        variables=event.variables
        for val in SonosDevice.MASTERVALS: 
            if(val in variables):
                variable= variables[val]
                value=variable.get('Master',0)
                attribute=self.getAttribute(val)
                attribute.parameters[0].value=value
                return attribute
        if 'bass' in variables:
            value=variables.get('bass',0)
            attribute=self.getAttribute('bass')
            attribute.parameters[0].value=value
            return attribute
        if 'treble' in variables:
            value=variables.get('treble',0)
            attribute=self.getAttribute('treble')
            attribute.parameters[0].value=value
            return attribute
        
    

