### C-6 Summary {- #C-6}

#### Evaluation Criteria {-}

| Protocol  | Transfer Rate | Battery Life | Interoperability | ## of Connections | Frequency | Range   | Topology |
| --------- | ------------  | ------------ | ---------------- | ---------------- | --------- | ------- | -------- |
| ZigBee    | 250 kbps      | Good         | Good             | 256              | 2.4 GHz   | 35  Ft. | Mesh     |
| Z-Wave    | 40 kbps       | Great        | Great            | 232              | 915 MHz   | 100 Ft. | Mesh     |
| Insteon   | 13 kbps       | Good         | Bad              | N/A              | 915 MHz   | 150 Ft. | Mesh     |
| WiFi      | 54 Mbps       | Bad          | Great            | 256              | 2.4 GHz   | 105 Ft. | Star     |
| BLE       | 10 kbps       | Good         | Great            | 9                | 2.4 GHz   | 200 Ft. | Star     |

As stated above, the goal of this research was to pick an appropriate protocol for our system.
One of the differing attributes between the protocols is the data transfer rates. The required
data rate for most smart home devices is minimal, and a higher data rate demands more power. The
data rate provided by WiFi is more than required for our project so it will not be the primary
communication protocol used. That being said, WiFi compatibility is important to this project
because of its prevalence in homes, and because of the enormous amount of devices that communicate
over WiFi.

Having as inclusive device support as possible is a key aspect to our project, as it allows a
user to have whatever functionality they desire. This heavily influenced us in deciding not
to use Insteon as our primary protocol, as the backwards compatibility with X10 power line 
communication protocol is not something we require.

ZigBee and Z-Wave are very similar, with the key difference in our eyes being the consistent
interface that Z-Wave devices provide for controlling them. In additionally, avoiding interference
conflicts between the prevalent communication protocol, WiFi, is a benefit. Z-Wave operates in
the less used 900 MHz frequency band, avoiding any potential conflicts.

A mesh network topology has many benefits over a star topology for message routing and
communication in home automation systems. The stability offered by a mesh topology is aids in
reliability, and the amount of data transmission is low enough that the redundant connections are
not costly. This makes Z-Wave a more attractive alternative than Bluetooth Low Energy.

Overall, using Z-Wave as our primary communication protocol appears to be the best choice
for this project. For industry compliance, WiFi will be required as well.

#### Z-Wave Implementation Specifics {-}

Any processing unit with USB support can be easily turned into a Z-Wave master, using a Z-Wave
USB stick. Converting an Arduino into a Z-Wave slave is not simple. There are specialized
Arduino boards that have the Z-Wave protocol built in. Another option is to attach a radio
frequency device to an Arduino, and to implement the Z-Wave stack protocol manually. The easiest
way to have Z-Wave slave devices is simply not to make them, but to buy them.

