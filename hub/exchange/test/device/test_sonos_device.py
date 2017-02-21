import uuid
import unittest
from unittest import mock
from unittest import TestCase
from unittest.mock import Mock
from device.data_types import DataType
from device.sonos_device import SonosDevice

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
        device= SonosDevice(self.mockNode)
        self.assertEqual("Media Room",device.name)
        self.assertEqual('Sonos PLAY:1',device.deviceType.name)
        self.assertEqual(5,len(device.deviceType.attributes))
        self.assertEqual('http://localhost:1400/img/icon-S1.png',device.icon)