### J-3 Gateway REST API {- #J-3}

##### General {-}

The gateway interface provides a public interface for controlling the Aria system using HTTP.
The gateway uses a REST protocol for requesting or controlling static data about the system.
For dynamic data, the gateway uses websocket messages. Below is the public REST API for the
gateway. To see the available events over websockets
[see gateway websocket events](#J-4).

#### Endpoint Documentation {-}

##### Discovery {-}

+---------------+-------------------------------------------------------------------------------+
| Title     	| **Start Device Discovery**	                                                |
|      		 	|                                                                             	|
|       		| This method initiates the discovery sequence for all adapters in the central 	|
|       		| hub. The return from this call will indicate if the process has started but	|
|       		| not if any devices have yet been discovered. All device discoveries will be	|
| 				| returned over websocket messages 												|
|				| ([see device discovered](#section-design-api-ws-discovered)) for more details.|
+---------------+-------------------------------------------------------------------------------+
| URL         	| `/hub/discover` 																|
+---------------+-------------------------------------------------------------------------------+
| Method		| **GET**																		|
+---------------+-------------------------------------------------------------------------------+
| URL Params	| **None**																		|
+---------------+-------------------------------------------------------------------------------+
| Data Params	| **None** 																		|
+---------------+-------------------------------------------------------------------------------+
| Success		| **Example:** <br/>															|
| Response		| **Code:** `200` <br/>															|
| 				| **Content:**  `{ }` <br/>														|
+---------------+-------------------------------------------------------------------------------+
| Error			| **Example:** 	<br/>															|
| Response		| **Code:** `500 Internal Server Error` <br/>									|
| 				| **Content:**  `{ error : "Unable to initiate discovery" }` <br/>				|
+---------------+-------------------------------------------------------------------------------+
| Sample Call	| `curl -X GET http://localhost:8080/hub/discover`								|
+---------------+-------------------------------------------------------------------------------+

##### Hub State {-}

+---------------+-------------------------------------------------------------------------------+
| Title     	| **Get Hub State**	                                               				|
|      		 	|                                                                             	|
|       		| Returns the current state of the hub. This will return the mode, number of 	|
| 				| connected devices and version of the hub.										| 
+---------------+-------------------------------------------------------------------------------+
| URL         	| `/hub/state` 																	|
+---------------+-------------------------------------------------------------------------------+
| Method		| `GET`																			|
+---------------+-------------------------------------------------------------------------------+
| URL Params	| **None**																		|
+---------------+-------------------------------------------------------------------------------+
| Data Params	| **None** 																		|
+---------------+-------------------------------------------------------------------------------+
| Success		| **Example:** <br/>															|
| Response		| **Code:** `200` <br/>															|
| 				| **Content:** <br/>															|
|				|																				|
| 				| 		{																		|
| 				|			"version" 	: "1.0.0", 												|
| 				|		 	"mode" 		: 1,													|
| 				|		 	"name" 		: "Smart Hub", 											|
| 				|		 	"devices" 	: 8 													|
| 				|		}																		|
+---------------+-------------------------------------------------------------------------------+
| Error			| **Example:** 	<br/>															|
| Response		| **Code:** `400 Bad Request` <br/>												|
| 				| **Content:**  `{ error : "Invalid Request" }` <br/>							|
+---------------+-------------------------------------------------------------------------------+
| Sample Call	| `curl -X GET http://localhost:8080/hub/state`		 							|
+---------------+-------------------------------------------------------------------------------+

##### Hub Mode {-}

+---------------+-------------------------------------------------------------------------------+
| Title     	| **Get Hub Mode**	                                               				|
|      		 	|                                                                             	|
|       		| Returns the mode of the hub													| 
+---------------+-------------------------------------------------------------------------------+
| URL         	| `/hub/mode` 																	|
+---------------+-------------------------------------------------------------------------------+
| Method		| `GET`																			|
+---------------+-------------------------------------------------------------------------------+
| URL Params	| **None**																		|
+---------------+-------------------------------------------------------------------------------+
| Data Params	| **None** 																		|
+---------------+-------------------------------------------------------------------------------+
| Success		| **Example:** <br/>															|
| Response		| **Code:** `200` <br/>															|
| 				| **Content:** `{ "mode" : 1 }` <br/>											|
+---------------+-------------------------------------------------------------------------------+
| Error			| **Example:** 	<br/>															|
| Response		| **Code:** `400 Bad Request` <br/>												|
| 				| **Content:**  `{ error : "Invalid request" }` <br/>							|
+---------------+-------------------------------------------------------------------------------+
| Sample Call	| `curl -X GET http://localhost:8080/hub/mode`		 							|
+---------------+-------------------------------------------------------------------------------+

+---------------+-------------------------------------------------------------------------------+
| Title     	| **Set Hub Mode**	                                               				|
|      		 	|                                                                             	|
|       		| Update the mode of the hub													| 
+---------------+-------------------------------------------------------------------------------+
| URL         	| `/hub/mode` 																	|
+---------------+-------------------------------------------------------------------------------+
| Method		| `POST`																		|
+---------------+-------------------------------------------------------------------------------+
| URL Params	| **None**																		|
+---------------+-------------------------------------------------------------------------------+
| Data Params	| - **mode**: The new mode of the hub (one of 0 = Standby, 1 = Normal, 			|
| 				| 	2 = Learning )																|
| 				| 																				|  
|				| **Example:** Set mode to *Learning*<br/>										|
| 				| **Content:** `{ "mode" : 2 }` <br/>											|
+---------------+-------------------------------------------------------------------------------+
| Success		| **Example:** <br/>															|
| Response		| **Code:** `200` <br/>															|
| 				| **Content:** `{ "mode" : 2 }` <br/>											|
+---------------+-------------------------------------------------------------------------------+
| Error			| **Example:** 	<br/>															|
| Response		| **Code:** `400 Bad Request` <br/>												|
| 				| **Content:**  `{ error : "Invalid mode" }` <br/>								|
+---------------+-------------------------------------------------------------------------------+
| Sample Call	| **Example:** Set the mode to *Normal*											|
| 				|																				|
| 				|		curl -X POST http://localhost:8080/hub/mode \							|
| 				|  			-H 'Content-Type: application/json' \								|
| 				| 			--data '{ "mode" : 1}'												|
+---------------+-------------------------------------------------------------------------------+


##### Event Log {-}

+---------------+-------------------------------------------------------------------------------+
| Title     	| **Get Event Log**	                                               				|
|      		 	|                                                                             	|
|       		| Returns an event window from the hub of the requested window in reverse order |
| 				| (ensuring that the most recent event is first). 								|
+---------------+-------------------------------------------------------------------------------+
| URL         	| `/hub/events` 																|
+---------------+-------------------------------------------------------------------------------+
| Method		| `POST`																		|
+---------------+-------------------------------------------------------------------------------+
| URL Params	| **None**																		|
+---------------+-------------------------------------------------------------------------------+
| Data Params	| - **start**: The index of the record to start at (0 indicates the most		|
| 				| 	recent record).																|
| 				| - **count**: The number of records to include in the window 					|
| 				| 																				|  
|				| **Example:** Retrieve the last 10 events <br/>								|
| 				| **Content:** <br/>															|
|				|																				|
|				|		{																		|
| 				| 			"start" : 0,														|
| 				| 			"count" : 10														|
| 				| 		}																		|
+---------------+-------------------------------------------------------------------------------+
| Success		| Upon successful response, the requested records will be returned. The records	|
| Response		| will be ordered from most recent to least recent.								|
|				|																				|
|				| **Example:** <br/>															|
| 				| **Code:** `200` <br/>															|
| 				| **Content:** <br/>															|
|				|																				|
|				|		{																		|
| 				| 			"records" : [														|
| 				| 				{																|
|				|					"index"			: 10,										|
|				|					"timestamp"		: 1480262533722,							|
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
|				|				...																|
| 				| 			]																	|
| 				| 		}																		|
+---------------+-------------------------------------------------------------------------------+
| Error			| **Example:** <br/>															|
| Response		| **Code:** `500 Internal Server Error` <br/>									|
| 				| **Content:**  `{ error : "Invalid event window" }` <br/>						|
+---------------+-------------------------------------------------------------------------------+
| Sample Call	| **Example:** Retrieve a window of 10 records starting after 10				|
| 				|																				|
| 				|		curl -X POST http://localhost:8080/hub/events \							|
| 				|  			-H 'Content-Type: application/json' \								|
| 				| 			--data '{ "start" : 10, "count" : 10 }'	 							|
+---------------+-------------------------------------------------------------------------------+

##### Device List {-}

+---------------+-------------------------------------------------------------------------------+
| Title     	| **Get Devices**                                        						|
|      		 	|                                                                             	|
|       		| Returns a listing of all devices in the system								| 
+---------------+-------------------------------------------------------------------------------+
| URL         	| `/device/list`																|
+---------------+-------------------------------------------------------------------------------+
| Method		| `GET`																			|
+---------------+-------------------------------------------------------------------------------+
| URL Params	| **None**																		|
+---------------+-------------------------------------------------------------------------------+
| Data Params	| **None** 																		|
+---------------+-------------------------------------------------------------------------------+
| Success		| Upon successful response, all devices will be returned.						|
| Response 		|																				|
|				| **Example:** <br/>															|
| 				| **Code:** `200` <br/>															|
| 				| **Content:** <br/>															|
|				|																				|
|				|		{																		|
|				|			"devices": [														|
|				|				{																|
|				|					"version"		: "1.2.1",									|
|				|					"name"			: "Light Sensor",							|
|				|					"address"		: "3c2538dd-64ed-4a0c-9ed3-14b2219feb11",	|
|				|					"deviceType"	: {											|
|				|						"name"			: "WeMo UPnP Light Sensor",				|
|				|						"maker"			: "WeMo",								|
|				|						"protocol"		: "UPnP",								|
|				|						"attributes" 	: [										|
|				|							{													|
|				|								"name"				: "State",					|
|				|								"isControllable"	: true,						|
|				|								"parameters"		: [							|
|				|									{											|
|				|										"name"		: "Hue",					|
|				|										"value" 	: 79,						|
|				|										"dataType"	: "int",					|
|				|										"max"		: 255,						|
|				|										"min" 		: 0,						|
|				|										"step" 		: 1							|
|				|									},											|
|				|									...											|
|				|								]												|
|				|							},													|
|				|							...													|
|				|						]														|
|				|					}															|
|				|				}																|
|				|				...																|
|				|			]																	|
|				|		}																		|
+---------------+-------------------------------------------------------------------------------+
| Error			| **Example:** 	<br/>															|
| Response		| **Code:** `500 Internal Server Error` <br/>									|
| 				| **Content:**  `{ error : "Failed request" }` <br/>							|
+---------------+-------------------------------------------------------------------------------+
| Sample Call	| `curl -X GET http://localhost:8080/device/list`		 						|
+---------------+-------------------------------------------------------------------------------+

##### Device Events {-}

+---------------+-------------------------------------------------------------------------------+
| Title     	| **Get Device Event Log**	                                      				|
|      		 	|                                                                             	|
|       		| Returns an event window of logs from a specific device in reverse order 		|
| 				| (ensuring that the most recent event is first). 								|
+---------------+-------------------------------------------------------------------------------+
| URL         	| `/device/:id/events` 															|
+---------------+-------------------------------------------------------------------------------+
| Method		| `POST`																		|
+---------------+-------------------------------------------------------------------------------+
| URL Params	| - **id**: The id of the device to request the logs for 						|
|				| 	(ex. `3c2538dd-64ed-4a0c-9ed3-14b2219feb11`) 								|
+---------------+-------------------------------------------------------------------------------+
| Data Params	| - **start**: The index of the record to start at (0 indicates the most		|
| 				| 	recent record).																|
| 				| - **count**: The number of records to include in the window 					|
| 				| 																				|  
|				| **Example:** Retrieve the last 10 events <br/>								|
| 				| **Content:** <br/>															|
|				|																				|
|				|		{																		|
| 				| 			"start" : 0,														|
| 				| 			"count" : 10														|
| 				| 		}																		|
+---------------+-------------------------------------------------------------------------------+
| Success		| Upon successful response, the requested records will be returned. The records	|
| Response		| will be ordered from most recent to least recent.								|
|				|																				|
|				| **Example:** <br/>															|
| 				| **Code:** `200` <br/>															|
| 				| **Content:** <br/>															|
|				|																				|
|				|		{																		|
|				|			"total"		: 100,													|
|				|			"records"	: [														|
|				|				{																|
|				|					"index" 		: 10,										|
|				|					"timestamp" 	: 1480256989762,							|
|				|					"device"		: "Light Sensor",							|
|				|					"deviceType"	: "Aeon Labs UPnP Light Sensor",			|
|				|					"attribute"		: {											|
|				|						"name"			: "State",								|
|				|						"parameters"	: [										|
|				|							{													|
|				|								"name"		: "State",							|
|				|								"value"		: 69,								|
|				|								"dataType"	: "time",							|
|				|							}													|
|				|							...													|
|				|						]														|
|				|					}															|
|				|				}																|
|				|				...																|
|				|			]																	|
|				|		}																		|
+---------------+-------------------------------------------------------------------------------+
| Error			| **Example:** <br/>															|
| Response		| **Code:** `400 Bad Request` <br/>												|
| 				| **Content:**  `{ error : "Unknown device" }` <br/>							|
| 				| OR <br/>																		|
|				| **Example:** <br/>															|
| 				| **Code:** `500 Internal Server Error` <br/>									|
| 				| **Content:**  `{ error : "Invalid event window" }` <br/>						|
+---------------+-------------------------------------------------------------------------------+
| Sample Call	| **Example:** Retrieve a window of 10 records starting after 10 for device		|
| 				| 	with id `3c2538dd-64ed-4a0c-9ed3-14b2219feb11`								|
| 				|																				|
| 				|		curl http://localhost:8080/device/3c2538dd-64ed-4a0c-9ed3-14b2219feb11/events \	|
| 				|  			 -X POST -H 'Content-Type: application/json' \						|
| 				| 			--data '{ "start" : 10, "count" : 10 }'	 							|
+---------------+-------------------------------------------------------------------------------+

##### Device Values {-}

+---------------+-------------------------------------------------------------------------------+
| Title     	| **Set Device Attribute**                                     				    |
|      		 	|                                                                             	|
|       		| Sets the value of an attribute of a device							        |
+---------------+-------------------------------------------------------------------------------+
| URL         	| `/device/:id/setAttribute` 													|
+---------------+-------------------------------------------------------------------------------+
| Method		| `POST`																		|
+---------------+-------------------------------------------------------------------------------+
| URL Params	| - **id**: The id of the device to set the attribute for 						|
|				| 	(ex. `3c2538dd-64ed-4a0c-9ed3-14b2219feb11`) 								|
+---------------+-------------------------------------------------------------------------------+
| Data Params	| - **name**: The name of the attribute to set									|
| 				| - **value**: A list of parameters and their values for the attribute          |
| 				| 																				|  
|				| **Example:** Set the brightness of a light <br/>								|
| 				| **Content:** <br/>															|
|				|																				|
|				| 		{																		|
| 				| 			"name" : "brightness",												|
| 				| 			"value" : [                                                         |
|               |     			{ "naame" : "level", "value" : 50 }                             |
|               |               ...             	    				                        |
|               |            ]                                                                  |
| 				| 		}																		|
+---------------+-------------------------------------------------------------------------------+
| Success		| Upon successful response, value of the updated attribute will be returned  	|
| Response		| 								                                                |
|				| **Example** <br/>                                                             |
|               |                                                                               |
|               |       {																        |
|				|			"response" 	: "brightness",							                |
|				|			"device"		: "Light Bulb", 							        |
|				|			"deviceType"	: "Aeotec Dimmable LED",        			        |
|				|			"attribute"		: {											        |
|				|				"name"			: "brightness", 						        |
|				|				"parameters"	: [										        |
|				|					{													        |
|				|						"name"		: "level",							        |
|				|						"value"		: 50,								        |
|				|						"dataType"	: "byte",							        |
|				|					}													        |
|				|					...													        |
|				|				]														        |
|				|		}												    			        |
|				|																		        |
|               |       																        |
+---------------+-------------------------------------------------------------------------------+
| Error			| **Example:** <br/>															|
| Response		| **Code:** `400 Bad Request` <br/>											    |
| 				| **Content:**  `{ error : "Unknown device" }` <br/>							|
| 				| OR <br/>																		|
|				| **Example:** <br/>															|
| 				| **Code:** `500 Internal Server Error` <br/>									|
| 				| **Content:**  `{ error : "Invalid data format" }` <br/>						|
+---------------+-------------------------------------------------------------------------------+
| Sample Call	| **Example:** Set the brightness value of device                        		|
| 				| 	with id `3c2538dd-64ed-4a0c-9ed3-14b2219feb11`								|
| 				|																				|
| 				|		curl http://localhost:8080/device/3c2538dd-64ed-4a0c-9ed3-14b2219feb11/setAttribute \	|
| 				|  			 -X POST -H 'Content-Type: application/json' \						|
| 				| 			--data '{ "name" : "brightness", "value" : ["level" : 50]  }'    	|
+---------------+-------------------------------------------------------------------------------+

##### Add Behaviour {-}

+---------------+-------------------------------------------------------------------------------+
| Title     	| **Add Behaviour**	                                                            |
|      		 	|                                                                             	|
|       		| This method creates a new behaviour that can be trained.                      |
+---------------+-------------------------------------------------------------------------------+
| URL         	| `/hub/training/behaviour` 													|
+---------------+-------------------------------------------------------------------------------+
| Method		| **POST**																		|
+---------------+-------------------------------------------------------------------------------+
| URL Params	| **None**																		|
+---------------+-------------------------------------------------------------------------------+
| Data Params	| - **name**: The name to give to the new behaviour 							|
| 				| 																				| 
|               | **Example** <br/>                                                             |
|               | 		                                                                        |
|               | 		{                                                                       |
|               |        		"name" : "Turn lightbulb on"                                    |
|               |		}                                                                       |
+---------------+-------------------------------------------------------------------------------+
| Success		| **Example:** <br/>															|
| Response		| **Code:** `200` <br/>															|
| 				| **Content:**  `{ "id" : < integer >}` <br/>   								|
+---------------+-------------------------------------------------------------------------------+
| Error			| **Example:** 	<br/>															|
| Response		| **Code:** `500 Internal Server Error` <br/>									|
| 				| **Content:**  `{ error : "Failed to add behaviour" }` <br/>  					|
+---------------+-------------------------------------------------------------------------------+

##### List Behaviours {-}

+---------------+-------------------------------------------------------------------------------+
| Title     	| **List Behaviours**	                                                        |
|      		 	|                                                                             	|
|       		| This method returns a paged list of existing behaviours.                      |
+---------------+-------------------------------------------------------------------------------+
| URL         	| `/hub/training/behaviours` 											        |
+---------------+-------------------------------------------------------------------------------+
| Method		| **GET**																		|
+---------------+-------------------------------------------------------------------------------+
| URL Params	| **None**																		|
+---------------+-------------------------------------------------------------------------------+
| Data Params	| - **start**: The id of the behaviour to start from                        	|
|               | - **count**: The number of records to return                                  |
| 				| 																				| 
|               | **Example** <br/>         													|
|               | 		                                                                        |
|               | 		{                                                               		|
|               | 		    "start" : 5                                                 		|
|               | 		    "count" : 15                                                		|
|               | 		}                                                               		|
+---------------+-------------------------------------------------------------------------------+
| Success		| **Example:** <br/>															|
| Response		| **Code:** `200` <br/>															|
| 				| **Content:**  																|
| 				| 																				|
| 				| 		{																		|	
|               |       	"records": [{                                               		|
|               |           	"id" 		    : 1 ,                                       	    |
|               |           	"name"		    : "My Behaviour",                              	    |
|               |           	"createdDate"	: 1380269867612,                     			    |
|               |           	"lastUpdated"	: 1480256989762,                     			    |
|               |           	"active"     	: false                            		            |
|               |				}                                                         	 	|
|               |               ...                                                          	|
|               |        	]														    		|
|               |		}               														|
|				|																		        |
|               |       																        |
+---------------+-------------------------------------------------------------------------------+
| Error			| **Example:** 	<br/>															|
| Response		| **Code:** `500 Internal Server Error` <br/>									|
| 				| **Content:**  `{ error : "Could not fetch behaviours" }` <br/>				|
+---------------+-------------------------------------------------------------------------------+


##### List Training Sessions {-}

+---------------+-------------------------------------------------------------------------------+
| Title     	| **List Training Sessions**                                                    |
|      		 	|                                                                             	|
|       		| This method returns a paged list of existing training sessions.               |
+---------------+-------------------------------------------------------------------------------+
| URL         	| `/hub/training/sessions` 														|
+---------------+-------------------------------------------------------------------------------+
| Method		| **GET**																		|
+---------------+-------------------------------------------------------------------------------+
| URL Params	| **None**																		|
+---------------+-------------------------------------------------------------------------------+
| Data Params	| - **start**: The id of the session to start from                          	|
|               | - **count**: The number of records to return                                  |
| 				| 																				| 
|               | **Example** <br/>																|
| 				|																		        |
|               |		{                                                               		|
|               |		    "start" : 5                                                 		|
|               |		    "count" : 15                                                		|
|               |		}                                                               		|
+---------------+-------------------------------------------------------------------------------+
| Success		| **Example:** <br/>															|
| Response		| **Code:** `200` <br/>															|
| 				| **Content:**  																|
| 				| 																				|
| 				| 		{																		|	
|               |       	"records": [{                                               		|
|               |           	"id" 		    : 1 ,                                       	    |
|               |           	"name"		    : "My Session",                              	    |
|               |           	"createdDate"   : 1380269867612,                     			    |
|               |           	"active"     	: false                            		            |
|               |				}                                                       		|
|               |               ...                                                          	|
|               |        	]														    		|
|               |		}               														|
|				|																		        |
|               |       																        |
+---------------+-------------------------------------------------------------------------------+
| Error			| **Example:** 	<br/>															|
| Response		| **Code:** `500 Internal Server Error` <br/>									|
| 				| **Content:**  `{ error : "Could not fetch training sessions" }` <br/>    		|
+---------------+-------------------------------------------------------------------------------+

##### Add Training Session {-}

+---------------+-------------------------------------------------------------------------------+
| Title     	| **Add Training Session**                                                      |
|      		 	|                                                                             	|
|       		| This method creates a new training session for a behaviour                    |
+---------------+-------------------------------------------------------------------------------+
| URL         	| `/hub/training/session` 													    |
+---------------+-------------------------------------------------------------------------------+
| Method		| **POST**																		|
+---------------+-------------------------------------------------------------------------------+
| URL Params	| **None**																		|
+---------------+-------------------------------------------------------------------------------+
| Data Params	| - **name**: The name to give to the training session							|
|               | - **behaviourId**: The id of the behaviour to associate with the session      |
| 				| 																				| 
|               | **Example** <br/>                                                             |
|               | 		        																|
| 				| 			{                                                                   |
|               |               "name" 			: "Wednesday Session",                          |
|               |           	"behaviourId"	: 2                                          	|
|               |           }                                                               	|
+---------------+-------------------------------------------------------------------------------+
| Success		| **Example:** <br/>															|
| Response		| **Code:** `200` <br/>															|
| 				| **Content:**  `{ "id" : < integer >}` <br/>   								|
+---------------+-------------------------------------------------------------------------------+
| Error			| **Example:** 	<br/>														    |
| Response		| **Code:** `500 Internal Server Error` <br/>									|
| 				| **Content:**  `{ error : "Failed to add session" }` <br/>     				|
+---------------+-------------------------------------------------------------------------------+

##### Start Training Session {-}

+---------------+-------------------------------------------------------------------------------+
| Title     	| **Start Training Session**                                                    |
|      		 	|                                                                             	|
|       		| This method activates a training session. New events and user requests will   |
|               | be associated with the training session                                       |
+---------------+-------------------------------------------------------------------------------+
| URL         	| `/hub/training/session/<id>/start` 											|
+---------------+-------------------------------------------------------------------------------+
| Method		| **POST**																		|
+---------------+-------------------------------------------------------------------------------+
| URL Params	| - **id**: The id of the training session to start 							|
+---------------+-------------------------------------------------------------------------------+
| Data Params	| **none**                                          							|
+---------------+-------------------------------------------------------------------------------+
| Success		| **Example:** <br/>															|
| Response		| **Code:** `200` <br/>															|
| 				| **Content:**  `{ }` <br/>   	                    							|
+---------------+-------------------------------------------------------------------------------+
| Error			| **Example:** 	<br/>													     	|
| Response		| **Code:** `500 Internal Server Error` <br/>									|
| 				| **Content:**  `{ error : "Failed to add session" }` <br/>     				|
+---------------+-------------------------------------------------------------------------------+

##### Stop Training Session {-}

+---------------+-------------------------------------------------------------------------------+
| Title     	| **Stop Training Session**                                                     |
|      		 	|                                                                             	|
|       		| This method deactivates an active training session. New events and requests   |
|               | will no longer be associated with this training session.                      |
+---------------+-------------------------------------------------------------------------------+
| URL         	| `hub/training/session/<id>/stop` 											    |
+---------------+-------------------------------------------------------------------------------+
| Method		| **POST**																		|
+---------------+-------------------------------------------------------------------------------+
| URL Params	| - **id**: The id of the training session to stop  							|
+---------------+-------------------------------------------------------------------------------+
| Data Params	| **none**                                          							|
+---------------+-------------------------------------------------------------------------------+
| Success		| **Example:** <br/>															|
| Response		| **Code:** `200` <br/>															|
| 				| **Content:**  `{ }` <br/>   	                    							|
+---------------+-------------------------------------------------------------------------------+
| Error			| **Example:** 	<br/>														    |
| Response		| **Code:** `500 Internal Server Error` <br/>								 	|
| 				| **Content:**  `{ error : "Failed to add session" }` <br/>     				|
|               | OR <br/>	                                                                    |
|               | **Example:** 	<br/>														    |
|               | **Code:** `400 Bad Request` <br/>									            |
|               | **Content:**  `{ error : "Training session is not active" }` <br/>     		|
+---------------+-------------------------------------------------------------------------------+

