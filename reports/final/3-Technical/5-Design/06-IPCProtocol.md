### IPC Protocol {#section-3-5-5}

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
| Discover    | DISC  | 0x01  |
| Request     | REQ   | 0x02  |
| Event       | EVT   | 0x03  |
| Acknowledge | ACK   | 0x04  |

#### Data Types {-}

This section defines the data structure format of data structures used in the response to requests

##### Data Type {-}
 
Data type is an enum that is used to represent the data types of device attributes. The possible 
values of this enum are:

- 'binary' 
- 'int'
- 'float' 
- 'colour'
- 'enum'
- 'time'
- 'date'
- 'string'
- 'list'

##### Attribute {-}

Attributes represent the different attributes of a device that can be viewed and/or changed

```
{
    "dataType": <DataType>,
    "max": <int>, 
    "min": <int>,
    "name": <string>,
    "step": <float>
}
```
dataType: a DataType from the above section

max: the max value the attribute can be, this may be null

min: the min value the attribute can be, this may be null

name: the attribute name, this is used in set and get request to query the device

step: the  difference between each acceptable value of the device, may be null

##### Device Type {-}

The Device type represents the different types of devices that are in the system. The device type
contains information about the manufacturer of the device the protocol the device speaks and the 
different attributes that the device has.

```
{
    "attributes":[<Attribute>],
    "isSensor": <boolean>, 
    "maker": <string>, 
    "name": <string>, 
    "protocol": <string>
}
```
name: the name of the type of device (WeMo Switch)

protocol: specifies what adapter will be needed (Z-Wave, WeMo, etc)

isSensor:  boolean value which specifies wether the device is to be interpreted as a sensor or 
a output device

maker:  device manufacturer name (Samsung, Aeon Labs, etc)

##### Device {-}

A device is a representation of a device that is connected to the system and can provide input or 
be controlled

```
{
    "address":<string>, 
    "devicetype": <DeviceType> ,
    "name": <string>, 
    "version": <string>
}
```

address: a unique UUID String used to identify a device

devicetype: the DeviceType related to the device

name: a user specified name for the device

version: the device version number from the manufacturer

#### Requests {-}

This section defines the format of the request and response payloads that are understood by 
the central server.

##### System Status {-}

Return the system status and any properties associated with the system

###### Request {-}

```json
{
    "get" : "status"

}
```

###### Response {-}

```json
{
    "response":"status",
    "value": {
                <String>:<value>, 
                ...
             }
}
```

value: attribute_name : value pairs for the device

##### Scan Devices {-}

###### Request {-}

```json
{
    "action" : "discover"
}
```

###### Response {-}

```json
{
    "success" : True | False
}
```

##### Device Information {-}

###### Request {-}

```json
{
    "action" : "about",
    "id" : "<device-uuid>"

}
```


###### Response {-}

```json
{
    <Device>
}
```

address: is a string representation of the device uuid


##### List Devices {-}

###### Request {-}

```json
{
    "get" : "devices"
}
```

###### Response {-}

```json
{
    [ 
     <Device>
    ]
}
```


##### Configure Device {-}

###### Request {-}

```json
{
    "action" : "configure"
    // Fields that need to be configured
}
```

| Field        | Description               |
| -----        | -----------               |
| Display Name | Name displayed for device |


###### Response {-}


```json
{
    "status" : "true|false",
    "error"  : "error message"
}
```

##### Control Device {-}

###### Request {-}

```json
{
    "set" : <attribute_name>,
    "value>" : <value>
}
```

attribute_name: the name of the attribute to changed
value: the value to set the attribute to


###### Response {-}

```json
{
    "response" : <attribute_name>,
    "value"  :  <value>
}
```

value: the new value that the device has fot the specified attribute

##### Query Device {-}

###### Request {-}

```json
{
    "get" : <attribute_name>
}
```


###### Response {-}

```json
{
    "response" : <attribute_name>,
    "value"  :  <value>
}
```


