### Gateway Websocket Protocol {#section-design-api-ws}

##### General {-}

This websocket protocol provides push events for clients listening to the gateway events. These
events notify when a device has been added or an event has occurred. They can be used to observe
the system. Currently there is no plan for adding push back over the sockets for dynamic control.

#### Endpoint Documentation {-}

##### Device Discovered {- #section-design-api-ws-discovered}

+---------------+-------------------------------------------------------------------------------+
| Title     	| **Event: Device Discovered**	                                                |
|      		 	|                                                                             	|
|       		| Triggered when the hub discovers a new device in the network. This event		|
| 				| typically follows a request for discovery but can be manually initiated 		|
| 				| by adding a device to the network.											|
+---------------+-------------------------------------------------------------------------------+
| Event Name  	| `device.discovered` 															|
+---------------+-------------------------------------------------------------------------------+
| Data Params	| The callback value will be the device that is to be added.					|
|				|																				|
|				| **Example**:																	|
|				|																				|
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
|				|									"max"		: 255,							|
|				|									"min" 		: 0,							|
|				|									"step" 		: 1								|
|				|								},												|
|				|								...												|
|				|							]													|
|				|						},														|
|				|						...														|
|				|					]															|
|				|				}																|
|				|			}																	|
+---------------+-------------------------------------------------------------------------------+

##### Device Event {- #section-design-api-ws-event}

+---------------+-------------------------------------------------------------------------------+
| Title     	| **Event: Device Event**	                                               		|
|      		 	|                                                                             	|
|       		| Triggered any time a device changes state through the change in a parameter	|
|				| value																			|
+---------------+-------------------------------------------------------------------------------+
| Event Name  	| `device.event` 																|
+---------------+-------------------------------------------------------------------------------+
| Data Params	| The callback value will be the device that is to be added.					|
|				|																				|
|				| **Example**:																	|
|				|																				|
|				|			{																	|
|				|				"timestamp" 	: 1480256989762,								|
|				|				"device"		: "Light Sensor",								|
|				|				"deviceType"	: "Aeon Labs UPnP Light Sensor",				|
|				|				"attribute"		: {												|
|				|					"name"			: "State",									|
|				|					"parameters"	: [											|
|				|						{														|
|				|							"name"		: "State",								|
|				|							"value"		: 69,									|
|				|							"dataType"	: "time",								|
|				|						}														|
|				|						...														|
|				|					]															|
|				|				}																|
|				|			}																	|
+---------------+-------------------------------------------------------------------------------+

