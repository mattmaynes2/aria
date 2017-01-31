When the Z-Wave adapter starts up, it uses the OpenZWave library to initiate a Z-Wave network. When 
a Z-Wave device is first paired with the Z-Stick (which is attached to the Raspberry Pi), the network
initiated by our Z-Wave adapter recieves a device object. This device object has been built by the 
OpenZWave library. An example of a such an object is shown below.

Once this ZWave object is recieved by the adapter, it is converted into a generic device object which
can be used internally in our system, shown below. 

Our ZWave adapter now notifies the Exchange that a device has been discovered, passing it the new
device object. From here, the device must be stored in the database, and the UI needs to be updated 
to display the new device and its information. The exhange forwards the device object to the 
database and to another adapter, which formats it properly for the UI.

The AriaAdapter is responsible for doing this formatting. In order to be properly displayed on the 
UI, the device object must be converted into a JSON string. Once this is done, a device discovered 
message is sent to the Gateway.

The purpose of the Gateway is to take messages received over a UDP socket and forward them over a 
Web socket to the user interface. *Matt insert UI knowledge in and around this area* :^)
 