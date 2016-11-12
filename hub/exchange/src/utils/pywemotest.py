import pywemo
devices= pywemo.discover_devices()
for device in devices:
    print(device.explain())
