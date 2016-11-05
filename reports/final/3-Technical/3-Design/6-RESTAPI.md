### REST API

> Author: Cameron Blanchard <br/>
> Updated: October 28, 2016 <br/>

The HTTP gateway component exposes some REST endpoints. The gateway allows system components
which can only communicate over HTTP to interact with any device in the system using a 
datagram protocol (see section 5 - Device Protocol). 

REST API Design Goals:

- In order to ensure the system is extensible and to ease testing, The REST API should not change
 when new capabilities are added to the communication hub. The REST API strictly translates 
 messages from HTTP to the Common Communication Protocol, with no interpretation of the requests
 and responses. 

`GET /system/state`

Get information about the current state of the automation system
Returns a JSON object.

`POST /request`

Send a request to the communication hub 

Content-Type header should be `application/json`
The body of the request should contain a JSON object. The object will be forwarded to the
communication hub as the payload of a type 3 message.

`POST /devices/<id>/request`

Send a request to a a device in the automation network.
Content-Type header should be `application/json`
The body of the request should contain aa JSON object. The object will be forwarded to the 
device identified by <id> as a type 3 message.

