import time
import logging
import uuid
from .device import Device
from .parameter import Parameter
from .data_types import DataType
from .attribute import Attribute
from .device_type import DeviceType
from ipc import Message

log = logging.getLogger(__name__)

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
    
    @property
    def volume(self):
        return self.__device.volume

    @volume.setter
    def volume(self,val):
       self.__setValue('volume',val)
            
    
    @property
    def mute(self):
        return self.__device.mute
    
    @mute.setter
    def mute(self,val):
        self.__setValue('mute',val)

    @property
    def bass(self):
        return self.__device.bass
    
    @bass.setter
    def bass(self,val):
       self.__setValue('bass',val)

    @property
    def treble(self):
        return self.__device.treble
    
    @treble.setter
    def treble(self,val):
       self.__setValue('treble',val)

    @property
    def loudness(self):
        return self.__device.loudness
    
    @loudness.setter
    def loudness(self,val):
       self.__setValue('loudness',val)
    
    def __setValue(self,attribute,val):
        param =self.getAttribute(attribute).parameters[0]
        if param.isValidValue(val):
            param.value=val
            setattr(self.__device,attribute,val)
        else:
            raise ValueError('{} is not a valid value for {}'.format(val,attribute))

    def _buildDeviceType(self):
        attributes=[]
        info = self.__device.speaker_info

        self._buildRenderingControlAttributes(attributes)
        return DeviceType(info['model_name'],SonosDevice.PROTOCOL,attributes=attributes)

    def _buildRenderingControlAttributes(self,attributes):
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
    
    def handleEvent(self,event):
        """
         Handle events from the sonos device
         an event object is composed of: 
            service: The service on the sonos that sent the event
            variables: A python dictionary with the modified data
            timestamp: The time the event took replace
        """

        log.debug("service: {}".format(type(event.service)))
        log.debug("variables: {}".format(event.variables))
        log.debug("timestamp: {}".format(event.timestamp))
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


    def handleRequest(self, attribute,value):
        if hasattr(self,attribute):
            setattr(self,attribute,value)
            param =self.getAttribute(attribute).parameters[0]
            return {
                    'name' : param.name,
                    'value' : param.value,
                    'dataType' : param.dataType.value
                    }

    def _handleRenderingEvent(self,event):
        """
         Handles events from the device for changes to:
            mute
            volume
            bass
            treble
            loudness
        """
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
