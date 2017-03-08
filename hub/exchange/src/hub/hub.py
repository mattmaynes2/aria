import json
import logging
import uuid
from .hub_mode  import HubMode
from .commands import CommandType, Command
from .commands.hub_commands import *
from device import Device, DeviceType, Attribute, DataType, Parameter
from ipc import Message
from device import SoftwareDeviceFactory
from datetime import datetime

log=logging.getLogger(__name__)

class Hub(Device):
    VERSION = '0.6.1'
    ADDRESS= Message.DEFAULT_ADDRESS
    GATEWAY_ADDRESS=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01'

    def __init__ (self, args = {}, exit = None):
        # setup device attributes and DeviceType
        methods=[Attribute('name',[Parameter('name',DataType.String)]), \
        Attribute('devices',[Parameter('devices',DataType.List)]),\
        Attribute('mode',[Parameter('mode',DataType.String)])]
        devType=DeviceType('Hub','hub',attributes=methods)
        super().__init__(devType,'Smart Hub',Hub.ADDRESS, version= Hub.VERSION)
        self.devices = {}
        self.mode    = HubMode.Normal
        self.exit    = exit if exit else lambda: None
        self.__commands= { key.value: {}  for key in CommandType}
        self.addAttributeCommands()
        self.session= None

    def addAttributeCommands(self):
        self.addCommand(get_name.GetHubNameCommand())
        self.addCommand(get_mode.GetHubModeCommand())
        self.addCommand(set_name.SetHubNameCommand())
        self.addCommand(set_mode.SetHubModeCommand())
        self.addCommand(get_devices.GetDevicesCommand())
        self.addCommand(get_status.GetHubStatusCommand())

    def addCommand(self,command):
        self.__commands[command.commandType.value][command.name]=command

    def executeCommand(self,commandType,data):
        # execute the command specified by the incoming message
        return self.__commands[commandType.value][data[commandType.value]].execute(self,data)

    @property
    def status (self):
        sessionDict = None
        if (self.session)
            sessionDict = self.session.__dict__
            
        return {
            'version'   : self.version,
            'mode'      : self.mode.value,
            'devices'   : len(self.devices),
            'session'   : sessionDict
        }

    def addDevice (self,device):
       # don't add the hub or gateway to devices
        if(device == self):
            return
        elif (device.address == Hub.GATEWAY_ADDRESS):
            return
        log.debug('adding device '+str(device))
        self.devices[device.address]=device

    def setMode(self,mode):
        self.mode=HubMode(mode)

    def getDevice(self,address):
        return self if address == self.address else self.devices.get(address)

    def isNormalMode(self):
        return self.mode == HubMode.Normal
