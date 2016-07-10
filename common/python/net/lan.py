import os
import socket

if os.name != "nt":
    import fcntl
    import struct

    __IF_NAMES = [
        "eth0"  , "eth1" , "eth2",
        "wlan0" , "wlan1", "wifi0",
        "ath0"  , "ath1" , "ppp0"
    ]

    def __interface_ip(ifname):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(
            fcntl.ioctl(s.fileno(), 0x8915,
                struct.pack('256s', ifname[:15])
            )[20:24]
        )

def get_ip():
    ip = socket.gethostbyname(socket.gethostname())
    if ip.startswith("127.") and os.name != "nt":
        for ifname in __IF_NAMES:
            try:
                ip = __interface_ip(ifname)
                break
            except IOError:
                # This will occur if the given interface name
                # has not been configured or this script does
                # not have sufficient permissions to read it
                pass
    return ip
