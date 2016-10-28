class Message:

    default         = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

    def __init__(self, type, msg,destination=default):
        self.type = type
        self.msg = msg
        self.destination=destination
