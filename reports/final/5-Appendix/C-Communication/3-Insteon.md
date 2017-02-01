### C-3 Insteon {- #C-3}

#### Description {-}

Insteon is substantially different from the two above protocols.

#### Technical Overview {-}

Insteon uses a similar mesh topology to the above protocols, but it is not limited to radio
frequencies. It utilizes a dual-mesh system to increase overall stability. The dual-mesh system is a
combination of radio frequencies at 915 MHz (in the US), and powerline layer operating at 131.65
KHz.Powerline communication is a technology that uses a home's electrical wiring to transfer data.  
When the radio frequencies encounter interference, the powerline layer makes sure the message
gets broadcasted to the appropriate destination. Insteon also uses a different message delivery 
system compared to ZigBee and Z-Wave. Instead of sending a message from one device and routing it
through other devices, it takes advantage of simulcasting. This is the process of having multiple
devices broadcasting the same message, so the intended recipient gets the message faster and more
reliably. This method is not feasible for high data rates, but Insteon shares it's low data rates
with ZigBee and Z-Wave. Simulcasting is also a result of the fact that an Insteon network does not
have a master/slave relationship. Every node has the ability to send and receive messages without
having a controller. This makes it possible to have any number of devices in a network without being
restricted by a maximum number of connections to a controlling device.

One thing Insteon is lacking compared to ZigBee and Z-Wave is third party support for their devices.
They manufacture almost all of their own devices, which leads to a limited amount of choice in terms
of different types of devices designed for the same task.

A unique advantage of Insteon is its ability to interface with devices following the X10 protocol.
The X10 protocol was one of the original protocols designed to work using only power lines. It is
outdated now in terms of being a reasonable choice for a new system, as it was designed over 30
years ago. This means that there is no wireless communication involved, which is essential for a
modern day smart home communication protocol. That said, there are many legacy automation systems in
place which still use X10 devices. If this were the case, then Insteon would be an ideal choice for
a communication protocol.

