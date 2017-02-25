import time
import logging
import uuid
from enum import Enum
from .device import Device
from .parameter import Parameter
from .data_types import DataType
from .attribute import Attribute
from .device_type import DeviceType
from ipc import Message
from .music_controls import MusicControls

log = logging.getLogger(__name__)

# turn logging from the sonos library to ERROR only
socoLogger = logging.getLogger('soco')
socoLogger.setLevel(logging.ERROR)
requestLogger = logging.getLogger('requests')
requestLogger.setLevel(logging.ERROR)

TIMESTAMP_FACTOR = 1000

class SonosQueue():
    
    def __init__(self,device):
        self.__device=device

    def put(self,item, block=True, timeout=None):
        self.__device.handleEvent(item)

class SonosDevice(Device):

    PROTOCOL ='sonos'
    # list of parameters that use the Master key for current value
    MASTERVALS=['volume','mute','loudness']
    PLAYCONTROLMAP= {'PLAYING':MusicControls.Play, 'TRANSITIONING': MusicControls.Play, 
    'PAUSED_PLAYBACK':MusicControls.Pause, 'STOPPED': MusicControls.Stop}
    def __init__(self, device,adapter):
        self.__device=device
        self.__adapter=adapter
        self.__subscriptions=[]
        # fromat UID from device into UUID
        address= uuid.UUID(bytes=bytes(device.uid.replace('RINCON_',''),'utf-8')[:16])
        info =device.get_speaker_info()
        name =info['zone_name']
        version= info['display_version']
        super().__init__(self._buildDeviceType(),name,address.bytes,version,
            icon='http://{}:1400{}'.format(self.__device.ip_address,info.get('player_icon')))
        self.__queue=SonosQueue(self)
        self.__subscriptions.append(self.__device.avTransport.subscribe(auto_renew=True,
        event_queue=self.__queue))
        self.__subscriptions.append(self.__device.renderingControl.subscribe(auto_renew=True,
        event_queue=self.__queue))
    
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

    @property
    def music_control(self):
        return self.getAttribute('music_control').parameters[0].value
    
    @music_control.setter
    def music_control(self,val):
        getattr(self.__device,val)()
        if val != MusicControls.Next.value and val != MusicControls.Prev.value:
            self.getAttribute('music_control').parameters[0].value=MusicControls(val)

    
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
        self._buildAvTransportAttributes(attributes)
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

    def _buildAvTransportAttributes(self,attributes):
        currentState=self.__device.get_current_transport_info().get('current_transport_state')
        attributes.append(Attribute('music_control',[Parameter('music_control',DataType.Enum,
        value=SonosDevice.PLAYCONTROLMAP[currentState], 
        enum=[val.value for val in MusicControls])]))
        
    
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
            self._handleAvTransportEvent(event)
        elif event.service == self.__device.renderingControl:
            attribute=self._handleRenderingEvent(event)
            self._sendEvent(attribute,event)
            


    def handleRequest(self, attribute,value):
        if hasattr(self,attribute):
            setattr(self,attribute,value)
            param =self.getAttribute(attribute).parameters[0]
            return {
                    'name' : param.name,
                    'value' : param.value if not isinstance(param.value,Enum) else param.value.value,
                    'dataType' : param.dataType.value
                    }

    def _sendEvent(self,attribute,event):
        data= {
                'event' : 'device.event',
                'timestamp' : int(event.timestamp*TIMESTAMP_FACTOR),
                'device' : self.name,
                'deviceType' : self.deviceType.name,
                'attribute' : dict(attribute)
                }
        self.__adapter.received(Message(Message.Event,data,sender=self.address))

    def _handleAvTransportEvent(self,event):
        """
        Handle events for av transport events.
        """
        transport_state= event.variables.get('transport_state')
        newVal=SonosDevice.PLAYCONTROLMAP[transport_state]

        self.getAttribute('music_control').parameters[0].value=newVal
        self._sendEvent(self.getAttribute('music_control'),event)
            
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
    
    def unsubscribe(self):
        for subscription in self.__subscriptions:
            subscription.unsubscribe()
