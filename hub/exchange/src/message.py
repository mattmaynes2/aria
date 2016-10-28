class Message:

    default         = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

    def __init__(self, msg, source, destination=default):
        self.message = msg
        self.source=source
        self.destination=destination
