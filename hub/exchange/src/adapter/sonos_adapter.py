import uuid
import logging
import soco
from Adapter import Adapter
from device import Device, DeviceType
from ipc import Message

import sys

log=logging.getLogger(__name__)

class SonosAdapter (Adapter):
    def __init__(self):
        super().__init__()

    def discover(self):
        devices=soco.discover()

    def send (self, message):
        pass

    def receive (self):
        return None