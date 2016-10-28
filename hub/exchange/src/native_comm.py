import socket
import comm
import message

class NativeComm (comm.Comm):
    PORT = 7600 # Default system port

    def __init__ (self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.port = NativeComm.PORT

    def setup (self):
        try:
            self.socket.bind(('localhost', self.port))
            print('Socket opened to port ' + str(self.port))
        except socket.error as msg:
            print('Socket failed to connect to port ' + str(self.port) + ' with: ' + msg);
            return False;
        return True

    def teardown (self):
        self.socket.close()
        return True


    """
    scan network for any new devices
    """
    def discover(): pass

    """
    send a message to a device
    """
    def send(device, msg):pass

    """
    listen for messages from devices
    """
    def receive(): pass
