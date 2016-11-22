### Database Interface Specification

#### Storing Events {-}

Events messages have the format

```
{ 
    "response" : <attribute>, 
    "value" : <value>
}
```

attribute: a field in a device
value: value of the attribute

All events are stored in the event table. Any event from a non sensor device is related to a user
action/request. If there was no request message sent to a non sensor device and an event is received
a request message is created for that event as this was a physical user action. Requests are stored
in the request table

The request message has the form

```
{
    "set" : <attribute>
    "value" : <value> 
}
```

attribute: a field in a device
value: value of to set the attribute to

All request messages that have the destination as the hub i.e. address is all 0's will not be 
stored in the event table as they are assumed to have no impact on the state of any devices in 
the system

#### Query Messages {-}

There are two different messages that can be used to request a list of events from the hub. In this
context events refer to rows from both the event and the request tables. The two types of requests
are **event window** and **device events**.

##### Event Window {-}

return a list of events from the hub for all devices

###### Request {-}

```
{
    "get":"eventWindow", 
    "start": <int>, 
    "count":<int>,
    "ignore":[<string>]
}
```


start: is the index to start at 0 is the most recent message 

count: number of records to return
ignore: A list of device UUID strings that should be ignored when getting events

###### Response {-}

``` 
{
    "response":"eventWindow", 
    "value": {
                "total": <int>,
                "records":  [
                                "timestamp": <Time String 'yyyy-MM-dd HH:mm:ss.SSS'>
                                "device": <String>
                                "source": <String>
                                "attribute": <String>
                                "value": <?>
                                "datatype":<String>
                                "index": <int>
                            ]
             }
}
```

total: total number of records returned 

records: a list of records

timestamp: timestamp of event

device: the device name

source: the device uuid String

value: the value of the event

datatype: datatype of the value

index: the index of the record

#### Device events {-}

return a list of events for a specific device

##### Request {-}

```
{
    "get": "deviceEvents",
    "id": <String>, 
    "start": <int>, 
    "count": <int>
}
```

return n events for a device starting at an index

id: device uuid string
start: is the index to start at 0 is the most recent message 
count: number of records to return


##### Response {-}

``` 
{
    "response":"deviceEvents", 
    "value": <same as eventWindow>
}
```

