import uuid
import unittest
import time
from unittest import mock
from unittest import TestCase
from unittest.mock import Mock
from device.data_types import DataType
from device.sonos_device import SonosDevice
from ipc import Message


class SonosDeviceTest(TestCase):
    
    def setUp(self):
        self.mockNode = Mock()
        self.mockNode.uid='RINCON_5CAAFDC519AE01400'
        self.mockNode.get_speaker_info.return_value={'mac_address': '5C-AA-FD-C5-19-AE', 
                'uid': 'RINCON_5CAAFDC519AE01400', 'zone_name': 'Media Room', 'software_version': 
                '34.16-37101', 'player_icon': '/img/icon-S1.png', 'display_version': '7.1',
                'serial_number': '5C-AA-FD-C5-19-AE:3', 'hardware_version': '1.8.3.7-1',
                'model_name': 'Sonos PLAY:1', 'model_number': 'S1'}
        self.mockNode.speaker_info= self.mockNode.get_speaker_info()
        self.mockNode.bass=0
        self.mockNode.treble=0
        self.mockNode.volume=50
        self.mockNode.loudness=True
        self.mockNode.mute=False
        self.mockNode.ip_address='localhost'
        
    def test_create(self):
        device= SonosDevice(self.mockNode,None)
        self.assertEqual("Media Room",device.name)
        self.assertEqual('Sonos PLAY:1',device.deviceType.name)
        self.assertEqual(5,len(device.deviceType.attributes))
        self.assertEqual('http://localhost:1400/img/icon-S1.png',device.icon)
    
    def test_handleRenderingEvent(self):
        mockService = Mock()
        self.mockNode.renderingControl=mockService
        mockAdapter= Mock()
        device= SonosDevice(self.mockNode,mockAdapter)

        event_time=time.time()
        mockEvent= Mock()
        mockEvent.service=mockService
        mockEvent.variables={'volume':{'Master':100}}
        mockEvent.timestamp=event_time
        device.handleEvent(mockEvent)   

        mockAdapter.received.assert_called_with(Message(Message.Event,{
            'event' : 'device.event',
            'timestamp' : int(event_time*1000),
            'device':'Media Room',
            'deviceType': 'Sonos PLAY:1',
            'attribute': device.getAttribute('volume')
        },sender=device.address))
        self.assertEqual(100,device.getAttribute('volume').parameters[0].value)

    def test_bass_event(self):
        mockService = Mock()
        self.mockNode.renderingControl=mockService
        mockAdapter= Mock()
        device= SonosDevice(self.mockNode,mockAdapter)

        event_time=time.time()
        mockEvent= Mock()
        mockEvent.service=mockService
        mockEvent.variables={'bass':5}
        mockEvent.timestamp=event_time
        device.handleEvent(mockEvent)   

        mockAdapter.received.assert_called_with(Message(Message.Event,{
            'event' : 'device.event',
            'timestamp' : int(event_time*1000),
            'device':'Media Room',
            'deviceType': 'Sonos PLAY:1',
            'attribute': device.getAttribute('bass')
        },sender=device.address))
        self.assertEqual(5,device.getAttribute('bass').parameters[0].value)

    def test_treble_event(self):
        mockService = Mock()
        self.mockNode.renderingControl=mockService
        mockAdapter= Mock()
        device= SonosDevice(self.mockNode,mockAdapter)

        event_time=time.time()
        mockEvent= Mock()
        mockEvent.service=mockService
        mockEvent.variables={'treble':-10}
        mockEvent.timestamp=event_time
        device.handleEvent(mockEvent)   

        mockAdapter.received.assert_called_with(Message(Message.Event,{
            'event' : 'device.event',
            'timestamp' : int(event_time*1000),
            'device':'Media Room',
            'deviceType': 'Sonos PLAY:1',
            'attribute': device.getAttribute('treble')
        },sender=device.address))
        self.assertEqual(-10,device.getAttribute('treble').parameters[0].value)