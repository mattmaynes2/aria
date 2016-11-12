import time
from netdisco.discovery import NetworkDiscovery

netdis = NetworkDiscovery()
netdis.is_discovering=True
netdis.ssdp.scan()

for dev in netdis.discoverables.items():
    print(dir(dev))
    print(dev)


netdis.stop()
