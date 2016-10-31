# 5. Device Protocol

This is a two level protocol. Messages are sent from the central server to a translation layer
that converts the message into the device specific format. The intermediate layer will be
consistent for all devices. The device handlers will need to support the basic API layer
that is consistent for all devices but can implement it differently for any device.

The first level of the protocol is defined as the interaction between the communication server
and the device handlers. This protocol is called the common communication protocol (CCP). The
second level of the protocol is device specific and is the responsibility of the device handler.
This layer of the protocol is termed the device communication protocol (DCP). 



#### Message Protocol

Messages have to be sent between all components in the smart home system. The smart home system
uses UDP to send messages. The following is the encoding structure for all messages
sent in the system. It is assumed that all data in the payload field is JSON encoded unless the
message type indicates otherwise.

##### General Message Structure

```
+--------+---------+----------+-------------+--------------+
|  type  |   size  |  sender  | destination |   payload    |
+--------+---------+----------+-------------+--------------+
| 1 byte | 4 bytes | 16 bytes |  16 bytes   | 'size' bytes |
+--------+---------+----------+-------------+--------------+
```

##### Message Types

| Name        | Type  | Value |
| -----       | ----- | ----- |
| Error       | ERR   | 0x00  |
| Discover    | DISC  | 0x01  |
| Request     | REQ   | 0x02  |
| Event       | EVT   | 0x03  |
| Acknowledge | ACK   | 0x04  |

## Common Communication Protocol

This interface communicates directly to the communication hub. It must know how to convert
between the CCP and DCP. The following methods must be defined.

#### Setup

This method will be required to setup the device handler.

```
setup (listener: Listener)
```

#### Discover

```
discover ()
```

#### Send

Send is responsible for the reliable transmission of data between the central hub and the
desired smart device.

```
send (deivce : Device, message :  Message)
```


#### Teardown

```
teardown ()
```


### Notifications


#### New Device

```
discovered (device: Device)
```


#### Message

```
message (device: Device, message: Message)
```


## Device Communication Protocol

Messages are passed using the general message structure and are byte encoded. The payload
of the message

```
+--------+---------+----------+-------------+--------------+
|  type  |   size  |  sender  | destination |   payload    |
+--------+---------+----------+-------------+--------------+
| 1 byte | 4 bytes | 16 bytes |  16 bytes   | 'size' bytes |
+--------+---------+----------+-------------+--------------+
```

### Device Status

Return the device status and any properties associated with that device

##### Request

```json
{
    "action" : "status"

}
```

##### Response

```json
{
    "active" : true|false
    ...
}
```

### Device Information

##### Request

```json
{
    "action" : "about"

}
```


##### Response


```json
{
    "maker"     : "string",
    "protocol"  : "string",
    "version"   : "number",
    "name"      : "name"
}
```

### Configure Device

##### Request

```json
{
    "action" : "configure"
    ...
    // Fields that need to be configured
}
```

| Field        | Description               |
| -----        | -----------               |
| Display Name | Name displayed for device |


### Response

Response is status of update. True indicates success, false indicates failure

```json
{
    "status" : true|false
    "error"  : "error message"
}
```


