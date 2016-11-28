### IPC Protocol {#design-api-ipc}

This section defines a basic protocol for interprocess communication (IPC) between the 
HTTP gateway and the central server.

#### Protocol Definition {-}

The messages defined by this protocol are sent using UDP.

The protocol uses a simple request-response format. The server listens for messages on port 7600.
All request packets must be acknowledged by a response packet. This protocol is intended for
IPC purposes, so it is anticipated that both the server and client are running on the same
machine and packet loss is extremely unlikely.

In the event that no response is received within a reasonable amount of time, the request should
be re-sent.

Messages follow the general message structure shown below. Messages are encoded as bytes, using
Big-Endian byte order.

##### General Message Structure {-}

```
+--------+---------+----------+-------------+--------------+
|  type  |   size  |  sender  | destination |   payload    |
+--------+---------+----------+-------------+--------------+
| 1 byte | 4 bytes | 16 bytes |  16 bytes   | 'size' bytes |
+--------+---------+----------+-------------+--------------+
```

###### Message Types {-}

The type field should contain one of the following values:

| Name        | Type  | Value |
| -----       | ----- | ----- |
| Error       | ERR   | 0x00  |
| Discover    | DISC  | 0x01  |
| Request     | REQ   | 0x02  |
| Event       | EVT   | 0x03  |
| Response	  | RES   | 0x04  |

#### Data Types {-}

This section defines the data structure format of data structures used in the response to requests

##### Data Type {-}

Data type is an enum that is used to represent the data types of device attributes. The possible
values of this enum are:

- 'binary'
- 'int'
- 'float'
- 'color'
- 'enum'
- 'time'
- 'date'
- 'string'
- 'list'

##### Attribute Parameter {-}

Represents a parameter to an attribute of a device

```
{
    "name"      : <string>,
    "dataType"  : <DataType>,
    "max"       : <int>,
    "min"       : <int>,
    "step"      : <float>
}
```

- **dataType**: a DataType from the above section
- **max**: the max value the attribute can be, this may be null
- **min**: the min value the attribute can be, this may be null
- **name**: the attribute name, this is used in set and get request to query the device
- **step**: the  difference between each acceptable value of the device, may be null


##### Attribute {-}

Attributes represent the different attributes of a device that can be viewed and/or changed

```
{
    "name"              : <string>,
    "isControllable"    : <boolean>,
    "parameters"        : [<AttributeParameter>]
}
```

- **name**: Name of the attribute
- **isControllable**: boolean value which specifies whether the device is to be interpreted as a sensor 
    or an output device


##### Device Type {-}

The Device type represents the different types of devices that are in the system. The device type
contains information about the manufacturer of the device the protocol the device speaks and the 
different attributes that the device has.

```
{
    "attributes"    : [<Attribute>],
    "maker"         : <string>,
    "name"          : <string>,
    "protocol"      : <string>
}
```

- **name**: the name of the type of device (WeMo Switch)
- **protocol**: specifies what adapter will be needed (Z-Wave, WeMo, etc)
- **maker**:  device manufacturer name (Samsung, Aeon Labs, etc)

##### Device {-}

A device is a representation of a device that is connected to the system and can provide input or 
be controlled

```
{
    "address"    : <string>,
    "deviceType" : <DeviceType>,
    "name"       : <string>,
    "version"    : <string>
}
```

- **address**: a unique UUID String used to identify a device
- **deviceType**: the DeviceType related to the device
- **name**: a user specified name for the device
- **version**: the device version number from the manufacturer

#### Requests {-}

This section defines the format of the request and response payloads that are understood by
the central server.

##### System Status {-}

+---------------+-------------------------------------------------------------------------------+
| Title     	| **Get Hub Status**	                                                		|
|      		 	|                                                                             	|
|       		| Return the hub status and any properties associated with the hub 				|
+---------------+-------------------------------------------------------------------------------+
| Destination  	| The message must be addressed to the hub's well known ID:						|
|				| `00000000-0000-0000-0000-000000000000`										|
+---------------+-------------------------------------------------------------------------------+
| Message 		| 																				|
| 				|		02 XX XX XX XX YY YY YY YY YY YY YY YY YY YY YY YY YY YY YY YY 			|
|				|		00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 PAYLOAD					|
|				|																				|
|				| - **XX**: Indicates the bytes of the PAYLOAD length							|
|				| - **YY**: Indicates the bytes of the sender's address 						|
|				| - **PAYLOAD**: The body of the message 										|
|				|																				|
|				|																				|
|				|			{																	|
|				|    			"get" : "status"												|
|				|			}																	|
+---------------+-------------------------------------------------------------------------------+
| Success		| Below is an example of a successful response.									|
| Response		|																				|
|				|		04 XX XX XX XX 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 			|
|				|		YY YY YY YY YY YY YY YY YY YY YY YY YY YY YY YY PAYLOAD					|
|				|																				|
|				| - **XX**: Indicates the bytes of the PAYLOAD length							|
|				| - **YY**: Indicates the bytes of the original sender's address				|
|				| -	**PAYLOAD**: The response to the status request								|
|				|																				|
|				| 			{																	|
| 				|			   	"response"	: "status",											|
| 				|			    "value"		: {													|
| 				|			    	"mode" 		:  1,											|
| 				|			        "name" 		: "Smart Hub",									|
|				|					"devices" 	: 5,											|
|				|					"version" 	: "0.2.3"										|
| 				|				}																|
| 				|			}																	|
+---------------+-------------------------------------------------------------------------------+
| Error			| Errors are returned as an error packet of type `0x00`							|
| Response		|  																				|
|				|		00 XX XX XX XX 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 			|
|				|		YY YY YY YY YY YY YY YY YY YY YY YY YY YY YY YY PAYLOAD					|
|				|																				|
|				| - **XX**: Indicates the bytes of the PAYLOAD length							|
|				| - **YY**: Indicates the bytes of the original sender's address				|
|				| -	**PAYLOAD**: The response to the status request								|
|				|																				|
|				| 			{																	|
| 				|			   	"error"	: "Invalid request"										|
| 				|			}																	|
+---------------+-------------------------------------------------------------------------------+


##### Scan Devices {-}

+---------------+-------------------------------------------------------------------------------+
| Title     	| **Start Device Discovery**                                            		|
|      		 	|                                                                             	|
|       		| Initiates a discovery sequence to find new devices on the network				|
+---------------+-------------------------------------------------------------------------------+
| Destination  	| The message must be addressed to the hub's well known ID:						|
|				| `00000000-0000-0000-0000-000000000000`										|
+---------------+-------------------------------------------------------------------------------+
| Message 		| 																				|
| 				|		02 XX XX XX XX YY YY YY YY YY YY YY YY YY YY YY YY YY YY YY YY 			|
|				|		00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 PAYLOAD					|
|				|																				|
|				| - **XX**: Indicates the bytes of the PAYLOAD length							|
|				| - **YY**: Indicates the bytes of the sender's address 						|
|				| - **PAYLOAD**: The body of the message 										|
|				|																				|
|				|			{																	|
|				|    			"action" : "discover"											|
|				|			}																	|
+---------------+-------------------------------------------------------------------------------+
| Success		| Below is an example of a successful response.									|
| Response		|																				|
|				|		04 XX XX XX XX 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 			|
|				|		YY YY YY YY YY YY YY YY YY YY YY YY YY YY YY YY PAYLOAD					|
|				|																				|
|				| - **XX**: Indicates the bytes of the PAYLOAD length							|
|				| - **YY**: Indicates the bytes of the original sender's address				|
|				| -	**PAYLOAD**: Message reports if discovery has started successfully			|
|				|																				| 
|				| 			{																	|
| 				|			   	"success"	: true,												|
| 				|			}																	|
+---------------+-------------------------------------------------------------------------------+
| Error			| Errors are returned as an error packet of type `0x00`							|
| Response		|  																				|
|				|		00 XX XX XX XX 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 			|
|				|		YY YY YY YY YY YY YY YY YY YY YY YY YY YY YY YY PAYLOAD					|
|				|																				|
|				| - **XX**: Indicates the bytes of the PAYLOAD length							|
|				| - **YY**: Indicates the bytes of the original sender's address				|
|				| -	**PAYLOAD**: The response to the status request								|
|				|																				|
|				| 			{																	|
| 				|			   	"error"	: "Discovery failed reason" 							|
| 				|			}																	|
+---------------+-------------------------------------------------------------------------------+

##### List Devices {-}

+---------------+-------------------------------------------------------------------------------+
| Title     	| **List Hub Devices**	                                                		|
|      		 	|                                                                             	|
|       		| Returns the devices that are currently connected to the hub					|
+---------------+-------------------------------------------------------------------------------+
| Destination  	| The message must be addressed to the hub's well known ID:						|
|				| `00000000-0000-0000-0000-000000000000`										|
+---------------+-------------------------------------------------------------------------------+
| Message 		| 																				|
| 				|		02 XX XX XX XX YY YY YY YY YY YY YY YY YY YY YY YY YY YY YY YY 			|
|				|		00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 PAYLOAD					|
|				|																				|
|				| - **XX**: Indicates the bytes of the PAYLOAD length							|
|				| - **YY**: Indicates the bytes of the sender's address 						|
|				| - **PAYLOAD**: The body of the message 										|
|				|																				|
|				|																				|
|				|			{																	|
|				|    			"get" : "devices"												|
|				|			}																	|
+---------------+-------------------------------------------------------------------------------+
| Success		| Below is an example of a successful response.									|
| Response		|																				|
|				|		04 XX XX XX XX 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 			|
|				|		YY YY YY YY YY YY YY YY YY YY YY YY YY YY YY YY PAYLOAD					|
|				|																				|
|				| - **XX**: Indicates the bytes of the PAYLOAD length							|
|				| - **YY**: Indicates the bytes of the original sender's address				|
|				| -	**PAYLOAD**: The response to the status request								|
|				|																				|
|				|			{																	|
|				|				"devices": [													|
|				|					{															|
|				|						"version"		: "1.2.1",								|
|				|						"name"			: "Light Sensor",						|
|				|						"address"		: "3c2538dd-64ed-4a0c-9ed3-14b2219feb11", |
|				|						"deviceType"	: {										|
|				|							"name"			: "WeMo UPnP Light Sensor",			|
|				|							"maker"			: "WeMo",							|
|				|							"protocol"		: "UPnP",							|
|				|							"attributes" 	: [									|
|				|								{												|
|				|									"name"				: "State",				|
|				|									"isControllable"	: true,					|
|				|									"parameters"		: [						|
|				|										{										|
|				|											"name"		: "Hue",				|
|				|											"value" 	: 79,					|
|				|											"dataType"	: "int",				|
|				|											"max"		: 255,					|
|				|											"min" 		: 0,					|
|				|											"step" 		: 1						|
|				|										},										|
|				|										...										|
|				|									]											|
|				|								},												|
|				|								...												|
|				|							]													|
|				|						}														|
|				|					}															|
|				|					...															|
|				|				]																|
|				|			}																	|
+---------------+-------------------------------------------------------------------------------+
| Error			| Errors are returned as an error packet of type `0x00`							|
| Response		|  																				|
|				|		00 XX XX XX XX 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 			|
|				|		YY YY YY YY YY YY YY YY YY YY YY YY YY YY YY YY PAYLOAD					|
|				|																				|
|				| - **XX**: Indicates the bytes of the PAYLOAD length							|
|				| - **YY**: Indicates the bytes of the original sender's address				|
|				| -	**PAYLOAD**: The response to the status request								|
|				|																				|
|				| 			{																	|
| 				|			   	"error"	: "Invalid request"										|
| 				|			}																	|
+---------------+-------------------------------------------------------------------------------+

##### Device Information {-}

+---------------+-------------------------------------------------------------------------------+
| Title     	| **Request Device Status**                		                            	|
|      		 	|                                                                             	|
|       		| Return the state of a device in the system									|
+---------------+-------------------------------------------------------------------------------+
| Destination  	| The message must be addressed to the device of interest						|
+---------------+-------------------------------------------------------------------------------+
| Message 		| 																				|
| 				|		02 XX XX XX XX YY YY YY YY YY YY YY YY YY YY YY YY YY YY YY YY 			|
|				|		ZZ ZZ ZZ ZZ ZZ ZZ ZZ ZZ ZZ ZZ ZZ ZZ ZZ ZZ ZZ ZZ PAYLOAD					|
|				|																				|
|				| - **XX**: Indicates the bytes of the PAYLOAD length							|
|				| - **YY**: Indicates the bytes of the sender's address 						|
| 				| - **ZZ**: Indicates the bytes of the device address							|
|				| - **PAYLOAD**: The body of the message 										|
|				|																				|
|				|			{																	|
|				|    			"get" : "state"													|
|				|			}																	|
+---------------+-------------------------------------------------------------------------------+
| Success		| Below is an example of a successful response.									|
| Response		|																				|
|				|		04 XX XX XX XX ZZ ZZ ZZ ZZ ZZ ZZ ZZ ZZ ZZ ZZ ZZ ZZ ZZ ZZ ZZ ZZ 			|
|				|		YY YY YY YY YY YY YY YY YY YY YY YY YY YY YY YY PAYLOAD					|
|				|																				|
|				| - **XX**: Indicates the bytes of the PAYLOAD length							|
|				| - **YY**: Indicates the bytes of the original sender's address				|
| 				| - **ZZ**: Indicates the bytes of the original device address					|
|				| -	**PAYLOAD**: The state of the device										|
|				|																				|			
|				|			{																	|
|				|				"version"		: "1.2.1",										|
|				|				"name"			: "Light Sensor",								|
|				|				"address"		: "3c2538dd-64ed-4a0c-9ed3-14b2219feb11",		|
|				|				"deviceType"	: {												|
|				|					"name"			: "WeMo UPnP Light Sensor",					|
|				|					"maker"			: "WeMo",									|
|				|					"protocol"		: "UPnP",									|
|				|					"attributes" 	: [											|
|				|						{														|
|				|							"name"				: "State",						|
|				|							"isControllable"	: true,							|
|				|							"parameters"		: [								|
|				|								{												|
|				|									"name"		: "Hue",						|
|				|									"value" 	: 79,							|
|				|									"dataType"	: "int",						|
|				|								},												|
|				|								...												|
|				|							]													|
|				|						},														|
|				|						...														|
|				|					]															|
|				|				}																|
|				|			}																	|
+---------------+-------------------------------------------------------------------------------+
| Error			| Errors are returned as an error packet of type `0x00`. Note: this response	|
| Response		| example originates from the hub as there is no device with the given address 	|
|				|																				|
|				|		00 XX XX XX XX 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 			|
|				|		YY YY YY YY YY YY YY YY YY YY YY YY YY YY YY YY PAYLOAD					|
|				|																				|
|				| - **XX**: Indicates the bytes of the PAYLOAD length							|
|				| - **YY**: Indicates the bytes of the original sender's address				|
|				| -	**PAYLOAD**: The response to the status request								|
|				|																				|
|				| 			{																	|
| 				|			   	"error"	: "Unknown device" 										|
| 				|			}																	|
+---------------+-------------------------------------------------------------------------------+

##### Control Device {-}

+---------------+-------------------------------------------------------------------------------+
| Title     	| **Control Device Attribute**             		                            	|
|      		 	|                                                                             	|
|       		| Changes the state of a device by passing parameters to a desired attribute	|
+---------------+-------------------------------------------------------------------------------+
| Destination  	| The message must be addressed to the device of interest						|
+---------------+-------------------------------------------------------------------------------+
| Message 		| 																				|
| 				|		02 XX XX XX XX YY YY YY YY YY YY YY YY YY YY YY YY YY YY YY YY 			|
|				|		ZZ ZZ ZZ ZZ ZZ ZZ ZZ ZZ ZZ ZZ ZZ ZZ ZZ ZZ ZZ ZZ PAYLOAD					|
|				|																				|
|				| - **XX**: Indicates the bytes of the PAYLOAD length							|
|				| - **YY**: Indicates the bytes of the sender's address 						|
| 				| - **ZZ**: Indicates the bytes of the device address							|
|				| - **PAYLOAD**: The body of the message 										|
|				|																				|
|				|			{																	|
|				|    			"set" 	: "my custom attribute"									|
|				| 				"value"	: [														|
|				|					{															|
|				|						"name" 	: "parameter 1",								|
|				|						"value" : "new value"									|
|				|					}															|
|				|					...															|
|				|				]																|
|				|			}																	|
+---------------+-------------------------------------------------------------------------------+
| Success		| Below is an example of a successful response.									|
| Response		|																				|
|				|		04 XX XX XX XX ZZ ZZ ZZ ZZ ZZ ZZ ZZ ZZ ZZ ZZ ZZ ZZ ZZ ZZ ZZ ZZ 			|
|				|		YY YY YY YY YY YY YY YY YY YY YY YY YY YY YY YY PAYLOAD					|
|				|																				|
|				| - **XX**: Indicates the bytes of the PAYLOAD length							|
|				| - **YY**: Indicates the bytes of the original sender's address				|
| 				| - **ZZ**: Indicates the bytes of the original device address					|
|				| -	**PAYLOAD**: If the device has been updated									|
|				|																				|			
|				|			{																	|
|				|				"response" 	: "my custom attribute",							|
|				| 				"success" 	: true												|
|				|			}																	|
+---------------+-------------------------------------------------------------------------------+
| Error			| Errors are returned as an error packet of type `0x00`. 						|
| Response		|																			 	|
|				|		00 XX XX XX XX ZZ ZZ ZZ ZZ ZZ ZZ ZZ ZZ ZZ ZZ ZZ ZZ ZZ ZZ ZZ ZZ			|
|				|		YY YY YY YY YY YY YY YY YY YY YY YY YY YY YY YY PAYLOAD					|
|				|																				|
|				| - **XX**: Indicates the bytes of the PAYLOAD length							|
|				| - **YY**: Indicates the bytes of the original sender's address				|
| 				| - **ZZ**: Indicates the bytes of the original device address					|
|				| -	**PAYLOAD**: The response to the control request							|
|				|																				|
|				| 			{																	|
| 				|			   	"error"	: "Bad parameter value 'parameter 1':'new value'" 		|
| 				|			}																	|
+---------------+-------------------------------------------------------------------------------+

