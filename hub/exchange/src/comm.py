"""
Abstract class used for communicating with devices
using a specific protocol
"""
class Comm:

    """
    bind to port and any other setup required to
    communicate with devices

    """
    def setup(self) : pass

    """
    scan network for any new devices
    """
    def discover() : pass

    """
    send a message to a device
    """
    def send (message) : pass

    """
    close connections and unbind from port
    """
    def teardown() : pass

    """
    listen for messages from devices
    """
    def receive(): pass
