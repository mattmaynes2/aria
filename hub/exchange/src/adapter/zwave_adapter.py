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
from ipc import Message
import threading

logger = logging.getLogger(__name__)

class ZWaveAdapter(Adapter):

    CONTROLLER_NODE = 1
    DISCOVERY_TIMEOUT = 10

    def __init__(self,controller='/dev/zstick',\
    configPath='/home/pi/python-openzwave/openzwave/config',
    userPath ='.'):
        """
        controller: The device path to the zstick. Defaults to /dev/zstick
        configPath: Path to the OpenZWave config directory
        """
        super().__init__()

        # Set up condition variable allowing us to check if the network is ready or not
        self._ready = False
        self._lock = threading.Lock()

        self._discovered = False

        #self._ready_condition = threading.Condition(self._lock)

        # Pass some default options to OpenZWave
        self.defaultOptions= ZWaveOption(controller,config_path=configPath,user_path=userPath)
        self.defaultOptions.set_log_file('Zwave.log')
        self.defaultOptions.set_logging(True)
        self.defaultOptions.set_console_output(False)
        self.defaultOptions.lock()
        self.network = ZWaveNetwork(self.defaultOptions, autostart=False)
        self._devices={}
        self._setupCallbacks()

    def _networkReadyCallback(self, *args, **kwargs):
        logger.info("ZWave network is ready")
        #with self._ready_condition:
         #   self._ready = True
          #  self._ready_condition.notifyAll()

    def _nodeEventCallback(self, *args, **kwargs):
        node = kwargs['node']

        try:
            #Ignore value changes from devices that aren't fully discovered yet
            if node.location in self._devices:
                device = self._devices[node.location]
                data = device.processEvent(kwargs['value'].label)
                if not data:
                    return
                    
                event = Message(type_ = Message.Event, \
                                data = data, \
                                sender = device.address, \
                                receiver = Message.DEFAULT_ADDRESS)
                logger.info("Received a ZWave event")
                self.notify('received', event)

        except Exception as e:
            logger.exception("Error in node event callback: " + str(e))

    def _deviceDiscoveredCallback(self,*args, **kwargs):
        """
        This is a callback for the OpenZWave SIGNAL_NODE_QUERIES_COMPLETE notification
        """
        self._discovered = True
        node = kwargs["node"]
        if node.location in self._devices:
            return
        self._removeNodeAssociations(node)
        device=self.buildDevice(node)
        self._devices[node.location]=device
        logger.info("Discovered a ZWave device: " + device.name + " " + node.location)
        self.notify('discovered',device)

    def _removeNodeAssociations(self, node):
        for index, group in node.groups.items():
            for association in group.associations:
                if association != ZWaveAdapter.CONTROLLER_NODE:
                    group.remove_association(association)

    def _setupCallbacks(self):
        """
        This method registers the class to receive notifications from OpenZWave
        """
        dispatcher.connect(self._deviceDiscoveredCallback, ZWaveNetwork.SIGNAL_NODE_QUERIES_COMPLETE)
        dispatcher.connect(self._nodeEventCallback, ZWaveNetwork.SIGNAL_VALUE_CHANGED)
        dispatcher.connect(self._networkReadyCallback, ZWaveNetwork.SIGNAL_NETWORK_READY)

    def send(self, message):
        logger.debug("ZWave adapter attempting to send message: " + str(message))
        if(message.type == Message.Request):
            receiverString = str(UUID(bytes=message.receiver))
            device = self._devices[receiverString]
            self._handleRequest(message, device)
        else:
            logger.warning("Invalid message type sent to ZWaveAdapter: " + str(message.type))
            
    def setDeviceValue(self, message, device):
        self.network.controller.kill_command()
        attributeName = message.data["set"]
        value = message.data["value"]
        paramChanges =  []
        for param in value:
            change = device.setValue(param["name"], param["value"])  
            paramChanges.append(change)
        response = {
	    "device" : device.getName(),
	    "deviceType" : device.getDeviceType(),
	    "attribute" : {
	        "name" : attributeName,
	        "parameters" : paramChanges
            }
        }
        return response

    def _handleRequest(self, message, device):
        if "get" in message.data:
            attributeName = message.data["get"]
            self.notify("received", Message(
                type_ = Message.Response,
                data = {"response" : attributeName,
                        "value" : device.getValue(attributeName)
                        },
                sender = message.receiver,
                receiver = message.sender
                ))
            return True
        elif "set" in message.data:
            response = self.setDeviceValue(message, device)
            self.notify("received", Message(
                type_ = Message.Response,
                data = response,
                sender = message.receiver,
                receiver = message.sender
            ))
            return True

        return False

    def discover(self):
        self._discovered = False
        self.network.controller.kill_command()
        self.network.controller.add_node()
        t = threading.Timer(ZWaveAdapter.DISCOVERY_TIMEOUT, lambda self : self.network.controller.kill_command() if not self._discovered else None)


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
