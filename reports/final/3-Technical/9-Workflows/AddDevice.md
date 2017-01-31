When the Z-Wave adapter starts up, it uses the OpenZWave library to initiate a Z-Wave network. When 
a Z-Wave device is first paired with the Z-Stick (which is attached to the Raspberry Pi), the network
initiated by our Z-Wave adapter receives a device object. This device object has been built by the 
OpenZWave library. An example of a such an object is shown below.

```
basic: 4
product_name: LB60Z-1 Dimmable LED Light Bulb
capabilities: {'routing': 0, 'listening': 0, 'beaming': 0}
command_classes: {0, 32, 133, 38, 39, 134, 112, 114, 115, 90, 94}
command_classes_as_string: {'COMMAND_CLASS_VERSION', 'COMMAND_CLASS_ASSOCIATION', 'COMMAND_CLASS_CONFIGURATION', 'COMMAND_CLASS_POWERLEVEL', 'COMMAND_CLASS_NO_OPERATION', 'COMMAND_CLASS_SWITCH_MULTILEVEL', 'COMMAND_CLASS_MANUFACTURER_SPECIFIC', 'COMMAND_CLASS_BASIC', 'COMMA
ND_CLASS_SWITCH_ALL', 'COMMAND_CLASS_DEVICE_RESET_LOCALLY', 'COMMAND_CLASS_ZWAVE_PLUS_INFO'}
device_type: Light Dimmer Switch
generic: 17
groups: {1: {'label': 'Lifeline'}}
neighbors: {1: 0}
product_type: 0x4754
values: 
{
	72057594093076481: {'label': 'Level', 'data': 99, 'genre': 'User', 'value_id': 72057594093076481, 'units': '', 'node_id': 3}, 
	72057594102726788: {'label': 'Test Status', 'data': 'Failed', 'genre': 'System', 'value_id': 72057594102726788, 'units': '', 'node_id': 3},
	72057594102382614: {'label': 'InstallerIcon', 'data': 1536, 'genre': 'System', 'value_id': 72057594102382614, 'units': '', 'node_id': 3}, 
	72057594101465153: {'label': 'Start Level', 'data': 0, 'genre': 'System', 'value_id': 72057594101465153, 'units': '', 'node_id': 3}, 
	72057594101481476: {'label': 'Switch All', 'data': 'On and Off Enabled', 'genre': 'System', 'value_id': 72057594101481476, 'units': '', 'node_id': 3}, 
	72057594102726673: {'label': 'Timeout', 'data': 0, 'genre': 'System', 'value_id': 72057594102726673, 'units': 'seconds', 'node_id': 3}, 
	72057594098483220: {'label': 'Dim Level Memory', 'data': 'Full Brightness', 'genre': 'Config', 'value_id': 72057594098483220, 'units': '', 'node_id': 3}, 
	72057594102726742: {'label': 'Frame Count', 'data': 0, 'genre': 'System', 'value_id': 72057594102726742, 'units': '', 'node_id': 3}, 
	72057594103037975: {'label': 'Protocol Version', 'data': '3.95', 'genre': 'System', 'value_id': 72057594103037975, 'units': '', 'node_id': 3}, 
	72057594093076504: {'label': 'Bright', 'data': False, 'genre': 'User', 'value_id': 72057594093076504, 'units': '', 'node_id': 3}, 
	72057594102726724: {'label': 'Test Powerlevel', 'data': 'Normal', 'genre': 'System', 'value_id': 72057594102726724, 'units': 'dB', 'node_id': 3}, 
	72057594102726806: {'label': 'Acked Frames', 'data': 0, 'genre': 'System', 'value_id': 72057594102726806, 'units': '', 'node_id': 3}, 
	72057594102382593: {'label': 'ZWave+ Version', 'data': 1, 'genre': 'System', 'value_id': 72057594102382593, 'units': '', 'node_id': 3}, 
	72057594102382630: {'label': 'UserIcon', 'data': 1536, 'genre': 'System', 'value_id': 72057594102382630, 'units': '', 'node_id': 3}, 
	72057594103037991: {'label': 'Application Version', 'data': '5.08', 'genre': 'System', 'value_id': 72057594103037991, 'units': '', 'node_id': 3}, 
	72057594093076520: {'label': 'Dim', 'data': False, 'genre': 'User', 'value_id': 72057594093076520, 'units': '', 'node_id': 3}, 
	72057594103037959: {'label': 'Library Version', 'data': '3', 'genre': 'System', 'value_id': 72057594103037959, 'units': '', 'node_id': 3}, 
	72057594101465136: {'label': 'Ignore Start Level', 'data': True, 'genre': 'System', 'value_id': 72057594101465136, 'units': '', 'node_id': 3}, 
	72057594102726705: {'label': 'Test Node', 'data': 0, 'genre': 'System', 'value_id': 72057594102726705, 'units': '', 'node_id': 3}, 
	72057594102726696: {'label': 'Set Powerlevel', 'data': False, 'genre': 'System', 'value_id': 72057594102726696, ' units': '', 'node_id': 3}, 
	72057594102726776: {'label': 'Report', 'data': False, 'genre': 'System', 'value_id': 72057594102726776, 'units': '', 'node_id': 3}, 
	72057594102726760: {'label': 'Test', 'data': False, 'genre': 'System', 'value_id': 72057594102726760, 'units': '', 'node_id': 3}, 
	72057594102726660: {'label': 'Powerlevel', 'data': 'Normal', 'genre': 'System', 'value_id': 72057594102726660, 'units': 'dB', 'node_id': 3}
}
node_id: 3
location:
name:
num_groups: 1
object_id: 3
outdated: True
product_id: 0x3038
product_name: LB60Z-1 Dimmable LED Light Bulb
product_type: 0x4754
query_stage: Complete
role: Always On Slave
security: 0
specific: 1
type: Light Dimmer Switch
use_cache: True
manufacturer_id: 0x014f
manufacturer_name: Linear
max_baud_rate: 40000
name:
neighbors: {1}
home_id: 4036346586
is_awake: True
is_beaming_device: True
is_failed: False
is_frequent_listening_device: False
is_info_received: True
is_listening_device: True
is_locked: False
is_ready: True
is_routing_device: True
is_security_device: False
is_sleeping: False
is_zwave_plus: True
kvals: {}
last_update: None
```

Once this ZWave object is received by the adapter, it is converted into a generic device object which
can be used internally in our system, shown below. We also set the location on the ZWave device to
a UUID we have generated so that we are able to track this device if it is ever disconnected from 
the system.

```
name: LB60Z-1 Dimmable LED Light Bulb 
DeviceType: {
                LB60Z-1 Dimmable LED Light Bulb
                protocol: zwave, 
                maker: Linear
                Attributes: 
                [
                   {
                       name: Bright, 
                       parameters:  [
                                        {
                                            name: Bright,
                                            DataType: binary, 
                                            value: False, 
                                            min 0, 
                                            max: 0, 
                                            step: None
                                         }

                                    ]
                   },
                   {
                       name: Level 
                       parameters:  [ 
                                        {
                                            name: Level, 
                                            DataType: byte, 
                                            value: 99, 
                                            min 0, 
                                            max: 99, 
                                            step: None
                                        }

                                    ]
                   },
                   {
                        name: Dim, 
                        parameters: [
                                        {
                                            name: Dim, 
                                            DataType: binary, 
                                            value: False, 
                                            min 0, 
                                            max: 0, 
                                            step: None
                                        }

                                    ]
                   }
                ]
            }
address: abb757fc-5d38-45c8-bbbc-81cf6bf29d92 
version: 4
```

Our ZWave adapter now notifies the Exchange that a device has been discovered, passing it the new
device object. From here, the device must be stored in the database, and the UI needs to be updated 
to display the new device and its information. The exchange forwards the device object to the 
database and to another adapter, which formats it properly for the UI.

The AriaAdapter is responsible for doing this formatting. In order to be properly displayed on the 
UI, the device object must be converted into a JSON string. Once this is done, a device discovered 
message is sent to the Gateway.

The purpose of the Gateway is to take messages received over a UDP socket and forward them over a 
Web socket to the user interface. *Matt insert UI knowledge in and around this area* :^)
 