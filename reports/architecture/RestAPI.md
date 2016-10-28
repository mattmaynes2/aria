# REST API

`GET /devices/list`

Get a list of devices that have been added to the smart home network.

---

`GET /devices/<id>/info`

Get details about a device.

---

`GET /devices/<id>/state`

Get information about the current state of a device

---

`PUT /devices/</id>/state`

Set the state of a device

---

`POST /devices/discover`

Detect new devices in the vicinity of the smart home network

---

`GET /devices/new`

Get a list of devices which have been detected since the last call to `/devices/discover`

---

`POST /devices/add`

Add a newly detected device to the smart home network

---

`GET /system/state`

Get information about the current state of the automation system

---

`PUT /system/state`

Set the state of the automation system

