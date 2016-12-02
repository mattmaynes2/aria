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

class ZWaveAdapter():
    def __init__(self,controller='/dev/ttyACM0',\
    configPath='/home/pi/python-openzwave/openzwave/config',
    userPath ='.'):
        self.defaultOptions= ZWaveOption(controller,config_path=configPath,user_path=userPath)
        self.defaultOptions.set_log_file('Zwave.log')
        self.defaultOptions.set_logging(True)
        self.defaultOptions.set_console_output(False)
        self.defaultOptions.lock()
        self.network = ZWaveNetwork(self.defaultOptions, autostart=False)
        self._setupCallbacks()

    def _deviceDiscoveredCallback(*args, **kwargs):
        """
        This is a callback for the OpenZWave SIGNAL_NODE_QUERIES_COMPLETE notification
        """
        print("Args to discovered callback " + str(args))
        print("KWArgs to discovered callback " + str(kwargs))
        node = kwargs["node"]
        print(str(node.values_to_dict()))
        #print(str(node.to_dict()))
	
    def _setupCallbacks(self):
        """
        This method registers the class to receive notifications from OpenZWave 
        """
        dispatcher.connect(self._deviceDiscoveredCallback, ZWaveNetwork.SIGNAL_NODE_QUERIES_COMPLETE)

    def start(self):
        self.network.start()        

    def stop(self):
        self.network.stop()
