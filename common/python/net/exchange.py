import socket

import lan

class Exchange ():
    PORT = 8080

    def __init__ (self):
        self.socket = socket.socket(socket.AF_NET, socket.DGRAM)

    def announce (self, req, port = PORT):
        map(
            lambda addr : self.send(req, addr, port),
            lan.get_local_ips()
        )

    def send (self, req, address, port = PORT):
        pass

    def receive (self):
        pass

