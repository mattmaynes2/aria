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

class ZWaveAdapter():
    def __init__(self,controller='/dev/ttyACM0',\
    configPath='/home/pi/python-openzwave/openzwave/config',
    userPath ='.'):
        self.defaultOptions= ZWaveOption(controller,config_path=configPath,user_path=userPath)
    options.set_log_file('Zwave.log')
    