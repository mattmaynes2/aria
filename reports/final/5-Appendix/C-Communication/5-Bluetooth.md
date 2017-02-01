### C-5 Bluetooth {- #C-5}

#### Description {-}

Bluetooth is the most similar to WiFi of the alternative options. It is fairly common in households,
and non-technical users are more likely to be familiar with it than other protocols. There are
two main classifications of Bluetooth when it comes to home automation, both of which will be
discussed below.

#### Technical Overview {-}

Bluetooth operates in the 2.4 GHz frequency band, alongside WiFi and ZigBee. Bluetooth also shares
the star network topology with WiFi, and is ideal for master and slave devices.
This can lead to the same interference problems as discussed in the WiFi and ZigBee sections. As the
number of devices on the same radio frequency increases, the competition for bandwidth also
increases, causing potential latency and interference. The range and data transfer rate for
Bluetooth ranges from 1 Mbps and 10 meters to 24 Mbps and 100 meters. All of these data transfer
rates are acceptable for a smart home system. The range on the earlier versions
of Bluetooth is potentially very restricting. Bluetooth is somewhere between WiFi devices and
ZigBee/Z-Wave devices in terms of power consumption.

There is another choice for Bluetooth that addresses some of the issues above. Bluetooth version
4.0, also branded as Bluetooth Low Energy (BLE). This is a direct competitor with ZigBee and
Z-Wave. The range for a BLE device is 50 meters and  BLE is able to take advantage of a mesh
network topology. The maximum data transfer rate 1 Mbps in theory, but it is generally much
lower than that in practise. BLE splits the 2.4 GHz channel into smaller sub-channels to
help avoid interference with WiFi channels.

One of the goals of BLE is to make devices that do not require constant data transmission more
efficient. It accomplishes this by closing inactive connections while no data is being transferred.
Once data needs to be transferred, it reestablishes the necessary connection, completes the
transfer, and closes the connection again.
