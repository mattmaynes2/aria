from .cli import CLI
from ipc import Message
from delegate import Delegate
import logging
from uuid import UUID
from database import DatabaseTranslator
from delegate import RequestTracker
from threading import Lock
from sync import synchronized
log =logging.getLogger(__name__)

lock = Lock()

class Exchange (Delegate):

    def __init__ (self, hub, cli, database):
        self._hub       = hub
        self._cli       = cli
        self._adapters  = {}
        self._devices   = {}
        self._database  = RequestTracker(DatabaseTranslator(database),hub)
        self._delegates=[]
        self.addDelegate(self._database)

    def start (self):
        for _, adapter in self._adapters.items():
            log.debug('Starting adapter: ' + str(adapter))
            adapter.start()

    def register (self, device_type, adapter):
        log.info('Registered adapter: ' + str(adapter))
        adapter.add_delegate(self)
        self._adapters[device_type] = adapter

    def send (self, device, message):
        # TODO Log sending a message here
        if (device.deviceType.protocol in self._adapters):
            log.info('Sending ' + str(message) + ' to device ' + str(device))
            self._adapters[device.deviceType.protocol].send(message)
            self.notify('received',message)
    def teardown (self):
        for _, adapter in self._adapters.items():
            log.debug('Tearing down adapter: ' + str(adapter))
            adapter.teardown()
            adapter.join()

    def received (self, message):
        log.info('Received ' + str(message))
        if( 'action' in message.data and message.data['action'] == 'discover'):
            self.send(self._devices[message.sender],Message(
                type_=Message.Ack,
                data={'success':'True'},
                receiver=message.sender))
            self.discoverDevices()
        elif (message.receiver in self._devices):
            log.debug('Routing message to ' + str(UUID(bytes=message.receiver)))
            self.send(self._devices[message.receiver], message)
            log.debug('Done routing message')
        else:
            log.error('FUCK this message '+str(message))

    def discoverDevices(self):
        for _, adapter in self._adapters.items():
            adapter.discover()

    def discovered (self, device):
        log.info('Discovered device: ' + str(device))
        self._devices[device.address] = device
        # add device to hub
        self._hub.addDevice(device)
        self.notify('discovered',device)

    def notify (self, event, data):
        """Notifies all delegates of the given event with the supplied data

        Arguments:
            event (str): Name of event to trigger
            data (obj): Data to pass to delegate
        """
        for delegate in self._delegates:
            getattr(delegate, event)(data)

    def addDelegate(self,delegate):
        self._delegates.append(delegate)
