## Data Flows

### Add Device Data Flow {#section-workflow-addDevice}

This data flow outlines the details of how a new device is connected to the system. In
particular, this workflow focuses on adding a Z-Wave device to the system after. This
workflow assumes that the system is already online and operational, that the Z-Wave
stick is plugged into the smart hub and that the network is live

![](./uml/addDeviceFlow.png)

When the Z-Wave adapter starts up, it uses the OpenZWave library to initiate a Z-Wave network. When 
a Z-Wave device is first paired with the Z-Stick (which is attached to the Raspberry Pi), the network
initiated by our Z-Wave adapter receives a device object. This device object has been built by the 
OpenZWave library. An example of a such an object is shown below. For all of the data received from 
the device see [Appendix-G](#ZwaveDeviceData)

```
basic:4
product_name:LB60Z-1 Dimmable LED Light Bulb
device_type:Light Dimmer Switch
values:{  
   72057594093076481:{  
      'label':'Level',
      'data':99,
      'genre':'User',
      'value_id':72057594093076481,
      'units':'',
      'node_id':3
   },
   72057594093076504:{  
      'label':'Bright',
      'data':False,
      'genre':'User',
      'value_id':72057594093076504,
      'units':'',
      'node_id':3
   },
   72057594093076520:{  
      'label':'Dim',
      'data':False,
      'genre':'User',
      'value_id':72057594093076520,
      'units':'',
      'node_id':3
   },
}
node_id:3
location:
name:
product_name:LB60Z-1 Dimmable LED Light Bulb
type:Light Dimmer Switch
manufacturer_name:Linear
name:
home_id:4036346586
```

Once this ZWave object is received by the adapter, it is converted into a generic device object which
can be used internally in our system, shown below. We also set the location on the ZWave device to
a UUID we have generated so that we are able to track this device if it is ever disconnected from 
the system.

```
name: LB60Z-1 Dimmable LED Light Bulb 
DeviceType: {
                LB60Z-1 Dimmable LED Light Bulb
                protocol: zwave, 
                maker: Linear
                Attributes: 
                [
                   {
                       name: Bright, 
                       parameters:  [
                                        {
                                            name: Bright,
                                            DataType: binary, 
                                            value: False, 
                                            min 0, 
                                            max: 0, 
                                            step: None
                                         }

                                    ]
                   },
                   {
                       name: Level 
                       parameters:  [ 
                                        {
                                            name: Level, 
                                            DataType: byte, 
                                            value: 99, 
                                            min 0, 
                                            max: 99, 
                                            step: None
                                        }

                                    ]
                   },
                   {
                        name: Dim, 
                        parameters: [
                                        {
                                            name: Dim, 
                                            DataType: binary, 
                                            value: False, 
                                            min 0, 
                                            max: 0, 
                                            step: None
                                        }

                                    ]
                   }
                ]
            }
address: abb757fc-5d38-45c8-bbbc-81cf6bf29d92 
version: 4
```

Our ZWave adapter now notifies the Exchange that a device has been discovered, passing it the new
device object. From here, the device must be stored in the database, and the UI needs to be updated 
to display the new device and its information. The exchange forwards the device object to the 
database and to another adapter, which formats it properly for the UI.

The device adapter is responsible for doing this formatting. In order to be properly displayed on the 
UI, the device object must be converted into a JSON string. Once this is done, a device discovered 
message is sent to the Gateway.

The purpose of the Gateway is to take messages received over a UDP socket and forward them over a 
Web socket to the user interface.
 
