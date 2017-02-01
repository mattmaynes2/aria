### E-1 WeMo {- #E-1}

#### Description {-}

WeMo is a line of smart devices made by Belkin. WeMo devices can be controlled over a WiFi connection
using a smartphone app.

#### Available Devices {-}

1. Light switch
 - On/Off

2. Outlet switch
 - On/Off

3. Camera
 - On/Off
 - Motion detection

4. LED lights
 - On/Off
 - Dimming

5. Slow Cooker
 - On/Off
 - Temperature Control

6. Coffeemaker
 - On/Off
 - Brew status
 - Change filter

7. Air Purifier
 - Fan speed
 - Ionizing On/Off
 - Filter life
 
8. Humidifier 
 - Humidity level
 - Water status
 - Filter status

9. Heater
 - On/Off
 - Temperature
 - Power level

#### Technical Overview {-}

##### Communication Protocol {-}

WeMo only supports WiFi for communicating with devices. No central hub is required in order to 
control WeMo devices, each device connects to a WiFi network directly.

WeMo uses Universal Plug And Play (UPnP) protocol for discovery and operating the devices.

##### Developing with WeMo {-}

- *ouimeaux* is an Open source python API for controlling WeMo devices.
- WeMo devices can be controlled using UPnP. This allows us to implement one protocol and comunicate
 with all WeMo devices as well as any other smart devices from other vendors that use UPnP.

#### Research Criteria {-}

All WeMo Devices

| Inputs | Outputs | Developer Support | Protocol | API Restrictions    |
| ------ | ------- | ----------------- | -------- | ----------------    |
| On/Off | On/Off  | ouimeaux library  | WiFi     | Local Only          |
|        |         |                   | UPnP     | We need to Write it |

