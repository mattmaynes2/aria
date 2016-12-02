import openzwave
import logging
import os

from openzwave.node import ZWaveNode
from openzwave.node import ZWaveNode
from openzwave.value import ZWaveValue
from openzwave.scene import ZWaveScene
from openzwave.controller import ZWaveController
from openzwave.network import ZWaveNetwork
from openzwave.option import ZWaveOption
from pydispatch import dispatcher
from .adapter import Adapter
from device   import ZWaveDevice
from uuid import UUID

class ZWaveAdapter(Adapter):
    
 
    def __init__(self,controller='/dev/ttyACM0',\
    configPath='/home/pi/python-openzwave/openzwave/config',
    userPath ='.'):
        super().__init__()
        self.defaultOptions= ZWaveOption(controller,config_path=configPath,user_path=userPath)
        self.defaultOptions.set_log_file('Zwave.log')
        self.defaultOptions.set_logging(True)
        self.defaultOptions.set_console_output(False)
        self.defaultOptions.lock()
        self.network = ZWaveNetwork(self.defaultOptions, autostart=False)
        self._devices={}
        self._setupCallbacks()

    def _deviceDiscoveredCallback(self,*args, **kwargs):
        """
        This is a callback for the OpenZWave SIGNAL_NODE_QUERIES_COMPLETE notification
        """
        node = kwargs["node"]
        device=self.buildDevice(node)
        self._devices[device.address]=device
        self.notify('discovered',device)
	
    def _setupCallbacks(self):
        """
        This method registers the class to receive notifications from OpenZWave 
        """
        dispatcher.connect(self._deviceDiscoveredCallback, ZWaveNetwork.SIGNAL_NODE_QUERIES_COMPLETE)

    def setup(self):
        super().setup()
        self.network.start()        
        
    def teardown(self):
        self.network.stop()
        super().teardown()

    def buildDevice(self,node):
        device= ZWaveDevice(node)
        node.location=str(UUID(bytes=device.address))
        return device