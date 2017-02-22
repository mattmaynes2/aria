import sys
import time
from unittest import TestCase
from unittest.mock import Mock
from unittest import mock
from adapter.sonos_adapter import SonosAdapter
from device.sonos_device import SonosDevice
from ipc import Message

class SonosAdapterTest(TestCase):

    def setUp(self):
        self.adapter=SonosAdapter()
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
    
    @mock.patch('soco.discover')
    def test_discover(self,MockScan):
        s=set()
        s.add(self.mockNode)
        MockScan.return_value=s
        mockDelegate= Mock()
        self.adapter.add_delegate(mockDelegate)
        self.adapter.discover()
        device=mockDelegate.discovered.call_args[0][0]
        self.assertEqual(type(device),SonosDevice)
        self.assertEqual("Media Room",device.name)

    def test_event_push(self):
        mockDelegate= Mock()
        self.adapter.add_delegate(mockDelegate)

        mockService = Mock()
        self.mockNode.renderingControl=mockService
        device = SonosDevice(self.mockNode,self.adapter)

        event_time=time.time()
        mockEvent= Mock()
        mockEvent.service=mockService
        mockEvent.variables={'volume':{'Master':100}}
        mockEvent.timestamp=event_time
        device.handleEvent(mockEvent)   

        mockDelegate.received.assert_called_with(Message(Message.Event,{
            'event' : 'device.event',
            'timestamp' : int(event_time*1000),
            'device':'Media Room',
            'deviceType': 'Sonos PLAY:1',
            'attribute': device.getAttribute('volume')
        },sender=device.address))

    @mock.patch('soco.discover')
    def test_set_request(self, MockScan):
        s=set()
        s.add(self.mockNode)
        MockScan.return_value=s
        mockDelegate= Mock()
        self.adapter.add_delegate(mockDelegate)
        self.adapter.discover()
        device =SonosDevice(self.mockNode,self.adapter)
        
        data={
            "set": "mute", "value": [
                {
                    "dataType": "binary", 
                    "max": 'null', 
                    "min": 'null',
                    "name": "mute",
                    "step": 'null', 
                    "value": 1
                  }
                ]
            }
        message = Message(Message.Request,data,receiver=device.address)
        self.adapter.send(message)
        response = mockDelegate.received.call_args[0][0]
        self.assertEqual({  
                            'device':'Media Room',
                            'deviceType':'Sonos PLAY:1',
                            'attribute':{  
                                'name':'mute',
                                'parameters':[  
                                    {  
                                        'name':'mute',
                                        'value':1,
                                        'dataType':'binary'
                                    }
                                ]
                              }
                            }, response.data  )