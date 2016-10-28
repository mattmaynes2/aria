import threading

"""
Abstract class used for communicating with devices
using a specific protocol
"""
class Comm (threading.Thread):

    def __init__ (self):
        super().__init__()
        self.active = False

    """
    bind to port and any other setup required to
    communicate with devices

    """
    def setup (self) : pass

    """
    scan network for any new devices
    """
    def discover (self) : pass

    """
    send a message to a device
    """
    def send (self, message) : pass

    """
    close connections and unbind from port
    """
    def teardown(self) :
        self.active = False

    """
    listen for messages from devices
    """
    def receive (self): pass

    def run (self):
        while (self.active):
            self.receive()
