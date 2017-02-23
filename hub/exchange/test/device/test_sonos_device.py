import uuid
import unittest
import time
from unittest import mock
from unittest import TestCase
from unittest.mock import Mock
from device.data_types import DataType
from device.sonos_device import SonosDevice
from device.music_controls import MusicControls
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
        self.mockNode.get_current_transport_info.return_value={'current_transport_state':'STOPPED'}
        
    def test_create(self):
        device= SonosDevice(self.mockNode,None)
        self.assertEqual("Media Room",device.name)
        self.assertEqual('Sonos PLAY:1',device.deviceType.name)
        self.assertEqual('http://localhost:1400/img/icon-S1.png',device.icon)
        self.assertEqual(MusicControls.Stop, device.music_control)
        self.assertEqual([x.value for x in MusicControls],
                        device.getAttribute('music_control').parameters[0].enum)
    
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

    def test_RenderRequest(self):
        mockAdapter = Mock()
        device= SonosDevice(self.mockNode,mockAdapter)

        response=device.handleRequest('volume',30)
        self.assertEqual({ 
                    'name' : 'volume',
                    'value' : 30,
                    'dataType' : 'int'
                }, response)
        self.assertEqual(30,device.volume)

    def test_setLoudness(self):
        mockAdapter = Mock()
        device= SonosDevice(self.mockNode,mockAdapter)

        response=device.handleRequest('loudness',1)
        self.assertEqual({ 
                    'name' : 'loudness',
                    'value' : 1,
                    'dataType' : 'binary'
                }, response)
        
    def test_bass(self):
        device= SonosDevice(self.mockNode,None)
        self.assertEqual(0,device.bass)

    def test_play(self):
        mockAdapter = Mock()
        device= SonosDevice(self.mockNode,mockAdapter)
        response= device.handleRequest('music_control','play')
        self.assertEqual({
                            'name' : 'music_control',
                             'value': MusicControls.Play,
                              'dataType': 'enum'
                            },response)
        self.assertTrue(self.mockNode.play.called)

    def test_next(self):
        mockAdapter = Mock()
        device= SonosDevice(self.mockNode,mockAdapter)
        response= device.handleRequest('music_control','next')
        self.assertEqual({
                            'name' : 'music_control',
                             'value': MusicControls.Stop,
                              'dataType': 'enum'
                            },response)
        self.assertTrue(self.mockNode.next.called)

    def test_change_play_mode(self):
        mockService = Mock()
        self.mockNode.avTransport=mockService
        mockAdapter= Mock()
        device= SonosDevice(self.mockNode,mockAdapter)

        event_time=time.time()
        mockEvent= Mock()
        mockEvent.service=mockService
        mockEvent.variables={'current_play_mode': 'NORMAL', 'number_of_tracks': '2', 
        'current_crossfade_mode': '0',
         'current_track_duration': '0:05:19', 'current_track': '1', 'transport_state': 'PLAYING', 
         'enqueued_transport_uri': 'x-file-cifs://localhost/Music/song/url.mp3', 
         'current_section': '0'}
        mockEvent.timestamp=event_time
        device.handleEvent(mockEvent)   

        mockAdapter.received.assert_called_with(Message(Message.Event,{
            'event' : 'device.event',
            'timestamp' : int(event_time*1000),
            'device':'Media Room',
            'deviceType': 'Sonos PLAY:1',
            'attribute': device.getAttribute('music_control')
        },sender=device.address))
        self.assertEqual(MusicControls.Play,device.music_control)
        
        # make sure we don't call play when updateing the value
        self.assertFalse(self.mockNode.play.called)
    
    def test_no_change(self):
        """
        test that no event generated when system state isn't changed
        """
        mockService = Mock()
        self.mockNode.avTransport=mockService
        mockAdapter= Mock()
        device= SonosDevice(self.mockNode,mockAdapter)

        event_time=time.time()
        mockEvent= Mock()
        mockEvent.service=mockService
        mockEvent.variables={'transport_state': 'STOPPED'}
        mockEvent.timestamp=event_time
        device.handleEvent(mockEvent)   

        self.assertFalse(mockAdapter.received.called)
        self.assertEqual(MusicControls.Stop,device.music_control)