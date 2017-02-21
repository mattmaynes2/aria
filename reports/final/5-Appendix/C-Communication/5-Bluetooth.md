### C-5 Bluetooth {- #C-5}

#### Description {-}

Bluetooth is the most similar to WiFi of the alternative options. It is fairly common in households,
and non-technical users are more likely to be familiar with it than other protocols. There are
two main classifications of Bluetooth when it comes to home automation, both of which will be
discussed below.

#### Technical Overview {-}

Bluetooth operates in the 2.4 GHz frequency band, alongside WiFi and ZigBee. Bluetooth also shares
the star network topology with WiFi, and is ideal for master and slave devices [^C-5-1].
This can lead to the same interference problems as discussed in the WiFi and ZigBee sections. As the
number of devices on the same radio frequency increases, the competition for bandwidth also
increases, causing potential latency and interference. The range and data transfer rate for
Bluetooth ranges from 1 Mbps and 10 meters to 24 Mbps and 100 meters [^C-5-2]. All of these data transfer
rates are acceptable for a smart home system. The range on the earlier versions
of Bluetooth is potentially very restricting. Bluetooth is somewhere between WiFi devices and
ZigBee/Z-Wave devices in terms of power consumption.

There is another choice for Bluetooth that addresses some of the issues above. Bluetooth version
4.0, also branded as Bluetooth Low Energy (BLE). This is a direct competitor with ZigBee and
Z-Wave. The range for a BLE device is 50 meters and  BLE is able to take advantage of a mesh
network topology [^C-5-3]. The maximum data transfer rate 1 Mbps in theory, but it is generally much
lower than that in practise. BLE splits the 2.4 GHz channel into smaller sub-channels to
help avoid interference with WiFi channels.

One of the goals of BLE is to make devices that do not require constant data transmission more
efficient. It accomplishes this by closing inactive connections while no data is being transferred.
Once data needs to be transferred, it reestablishes the necessary connection, completes the
transfer, and closes the connection again[^C-5-4].

[^C-5-1]: J. 0, "Bluetooth basics," in Sparkfun. [Online]. Available: https://learn.sparkfun.com/tutorials/bluetooth-basics/how-bluetooth-works. Accessed: Oct. 10, 2016.

[^C-5-2]: Jim, "Bluetooth basics," in Sparkfun. [Online]. Available: https://learn.sparkfun.com/tutorials/bluetooth-basics/common-versions. Accessed: Oct. 9, 2016.

[^C-5-3]: "Data rates using BLE," in Anaren atmosphere. [Online]. Available: https://atmosphere.anaren.com/wiki/Data_rates_using_BLE. Accessed: Oct. 9, 2016.

[^C-5-4]: "Bluetooth low energy," in CSR. [Online]. Available: https://www.bluetooth.org/DocMan/handlers/DownloadDoc.ashx?doc_id=227336. Accessed: Oct. 9, 2016.






