### IPC Protocol {#section-design-api-ipc}

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

Data type is an enum that is used to represent the data types of device attributes. Each data type
has a unique set of behaviours and should be used appropriately. Each data type is configurable with
three control parameters. The range of a data type can be controlled with a maximum (`max`) and
minimum value (`min`). Some data types that do have a range of values should only increment in a
specific sequence which can be controlled by the `step` parameter. The step of a value is the
distance between two allowed values in a continuous range. It is a requirements that the step
value is always a positive value and that the maximum value is greater than the minimum.

It should be noted that not all data types use these parameters. Some data types have pre-determined
ranges or step values which are described for each data type below.

###### Binary

The `binary` type allows for control of a device from an 'On' and 'Off' state. These states are
represented by 1 and 0 respectively. These are the only two values permitted by this data type.

###### Byte

The `byte` data type is an integer value with the range 0 to 255. This data type can be used to
set a device in a specific mode or discrete value within this range. This data type ignores the
max, min values of the data range as it is assumed the range is 0 to 255. The step value is
respected by this data type but must be an integer value less than 255.

###### Integer

The `int` data type allows for a range of values from -2^31 to 2^31 - 1. This is appropriate for
values that need to be discrete but must satisfy a specific range. All of the data types are
respected by this data type.

###### Float

The `float` data type allows for a continuous value input to a device. This data type is
represented by an IEEE-754 floating point number and the associated range. The maximum and
minimum values for this data type should be integer values. The step for this data type can
be a float value that is less that the maximum float value.

###### Color

A `color` data type refers to an RGB value. The data type is encoded as a 4-byte integer value
where each byte represents a RGB value. The last byte is currently not used but is reserved as
an alpha value if the requirement arises. For example, the value for white (`#FFFFFF`) would be
encoded as `0xFF 0xFF 0xFF 0x00` or 4294967040 decimal.

###### Enumeration

An `enum` data type is used to represent a set of pre-determine values in a group. The values of
the enumeration must be encoded with the data type in a special `values` field which can be an
array of strings representing the enumerated values. The `value` field associated with an
enumeration field will represent the zero based index of the value in the values array.

###### Time

The `time` data type is a millisecond representation of a time interval. The value of this data
type is a millisecond value as an integer. The maximum and minimum parameters to this data type
will be used to limit the range of time available. The step can also be used but must be an
integer value.

###### Date

The `date` data type is a day representation of a time interval. The value of this data type is
a day offset represented as an integer. All of the data type parameters can be used with this data
type but they must be integer values.

###### String

The `string` data type is an open ended input which is represented by an arbitrary character
sequence. The maximum and minimum parameters for this data type can be used to limit the length
of the character sequence. The step parameter has no impact with this data type.


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
- **isControllable**: boolean value which specifies whether the device is to be interpreted as a 
	sensor or an output device


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
|				|						"version"	  : "1.2.1",								|
|				|						"name"		  : "Light Sensor",							|
|				|						"address"	  : "3c2538dd-64ed-4a0c-9ed3-14b2219feb11", |
|				|						"deviceType"  : {										|
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
|				|    			"get" : "status"												|
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
|				|    			"set" 	: "attribute name"	    								|
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
|				|		03 XX XX XX XX ZZ ZZ ZZ ZZ ZZ ZZ ZZ ZZ ZZ ZZ ZZ ZZ ZZ ZZ ZZ ZZ 			|
|				|		YY YY YY YY YY YY YY YY YY YY YY YY YY YY YY YY PAYLOAD					|
|				|																				|
|				| - **XX**: Indicates the bytes of the PAYLOAD length							|
|				| - **YY**: Indicates the bytes of the original sender's address				|
| 				| - **ZZ**: Indicates the bytes of the original device address					|
|				| -	**PAYLOAD**: If the device has been updated									|
|				|																				|			
|				|			{																	|
|				|				"response" 	: "attribute name",		        					|
|				| 				"value" 	: {													|
|				|					"device"		: "Temperature Sensor",						|
|				|					"deviceType"	: "ZigBee Temperature Sensor",				|
|				|					"attribute"		: {											|
|				|						"name" 			: "State",								|
|				|						"parameters"	: [										|
|				|							{													|
|				|								"name"		: "State",							|
|				|								"value"		: 30,								|
|				|								"dataType"	: "float"							|
|				|							}													|
|				|							... 												|
|				|						]														|
|				|					}															|
| 				|				}																|
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

