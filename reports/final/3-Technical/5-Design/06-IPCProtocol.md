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

#### Requests

This section defines the format of the request and response payloads that are understood by 
the central server.

##### System Status {-}

Return the system status and any properties associated with the system

###### Request {-}

```json
{
    "action" : "status"

}
```

###### Response {-}

```json
{
    "active" : "true|false"
    // ...
}
```
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

##### List Devices {-}

###### Request {-}

```json
{
    "action" : "list_devices"
}
```

###### Response {-}

```json
{
    [
        //device specific objects
    ]
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
    "maker"     : "string",
    "protocol"  : "string",
    "version"   : "number",
    "name"      : "name"
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


