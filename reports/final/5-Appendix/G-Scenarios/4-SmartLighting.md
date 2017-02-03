### G-4 Effortless Home Lighting {- #G-4}

#### Sample Sequence {-}

###### Setup {-}

The home is setup with a PIR in the home owner's office (PIROffice), a light sensor in the office 
(LightOffice), and dimmable smart lights in the office (SmartLights).

###### Training Sequence {-}

The user enters their office at 2:30:00 PM on Wednesday afternoon. PIROffice sends a motion detected 
message to the hub. The hub logs that PIROffice detected motion at 2:30:00 PM. It is a sunny afternoon,
so the home owner does not turn on the lights. The owner continues working uninterrupted until 
7:45:00 PM, when the sun begins to set. The hub logs that LightOffice is reading a lower value due to
the drop in light in the office. The owner turns the lights on dimly, to maintain the previous light
level of the room, causing the hub to log that SmartLights turned on. As the light level of the room
continues to drop in the room, the owner continues to raise the brightness of the lights. The hub
continues to log this interaction. Eventually, it is dark outside and the lights are at full 
brightness in the room. 

When the owner is done working, they get up, turn off the lights, and leave the room. The hub logs
that PIROffice detected motion at 9:00:00, and logs that SmartLights turned off at 9:00:03.
  

##### Alternate Sequences {-}

The light level of a room will not always be the same at a given time of day. The owner could enter
their office at 2:30:00 PM on Wednesday afternoon, and turn the lights on immediately because it is
rainy outside. The hub would log motion detected by PIROffice at 2:30:00, and then the value of
LightOffice increasing to the desired value immediately following. This sequence would end the same
way as the primary training sequence. 

##### Expected Inputs {-}

The logs for the training scenario would look like the following:
PIROffice = 0 when there is no motion detected, 1 when it is detecting motion
```
Initial Sensor States
LightOffice: 10
SmartLights: 0
PIROffice: 0
```
```
2016-11-06 14:30:00 [Sensor Update] PIROffice: 1
2016-11-06 19:39:00 [Sensor Update] LightOffice: 9
2016-11-06 19:42:00 [Sensor Update] LightOffice: 8
2016-11-06 19:45:00 [Sensor Update] LightOffice: 7
2016-11-06 19:45:10 [User Action]   SmartLights: 3
2016-11-06 19:45:12 [Sensor Update] LightOffice: 10
2016-11-06 19:48:00 [Sensor Update] LightOffice: 9
2016-11-06 19:51:00 [Sensor Update] LightOffice: 8
2016-11-06 19:55:00 [Sensor Update] LightOffice: 7
2016-11-06 19:55:10 [User Action]   SmartLights: 6
2016-11-06 19:55:12 [Sensor Update] LightOffice: 10
2016-11-06 19:58:00 [Sensor Update] LightOffice: 9
2016-11-06 20:01:00 [Sensor Update] LightOffice: 8
2016-11-06 20:05:00 [Sensor Update] LightOffice: 7
2016-11-06 20:05:10 [User Action]   SmartLights: 10
2016-11-06 20:05:12 [Sensor Update] LightOffice: 10
2016-11-06 21:00:00 [Sensor Update] PIROffice: 1
2016-11-06 21:00:07 [User Action]   SmartLights: 0
2016-11-06 21:00:08 [Sensor Update] LightOffice: 0
```

The alternate sequence could look like this:

```
Initial Sensor States
LightOffice: 0
SmartLights: 0
PIROffice: 0
```
```
2016-11-06 14:30:00 [Sensor Update] PIROffice: 1
2016-11-06 14:30:03 [User Action]   SmartLights: 10
2016-11-06 14:30:06 [Sensor Update] LightOffice: 10
2016-11-06 21:00:00 [Sensor Update] PIROffice: 1
2016-11-06 21:00:07 [User Action]   SmartLights: 0
2016-11-06 21:00:08 [Sensor Update] LightOffice: 0
```

##### Expected Behaviour {-}

From the logs the Aria system should be able to tell that the desired light level of the owners 
office when occupied is 10. The system should automatically adjust the brightness level of the Smart
Lights to achieve this level of brightness while the home owner is in the office. Upon the owner
leaving the office, the system should recognize that the lights must be turned off. 

##### Sensor and Device Correlation {-}

The graphs below depict the relationships between the light sensor, the motion sensor, and the smart
light brightness level in multiple different scenarios. The goal of these graphs is to illustrate
how the machine learning can interpret the sensor data to achieve the required functionality. The
first relationship that the machine learning will need to recognize is the correlation between the PIR
detecting motion and the lights being turned on. When no motion is detected, the light level detected
by the LightOffice sensor is allowed to decrease to 0 without the lights being turned on.

Now that the system understands the relationship between no motion being detected and lights staying
off, it needs to determine when it is appropriate to turn lights on when motion is detected. This is
the relationship between the LightOffice sensor and the SmartLights brightness level. The first time
the SmartLights are turned on by the homeowner is when the level of light detected by the LightOffice
sensor falls below a certain level. The lights are turned on enough to maintain the level of
brightness observed before it started decreasing. As the light levels continue to drop, the
SmartLights brightness continues to rise in compensation. The threshold use to determine when the
lights turn on is something that will be determined by how dark the homeowner allows the room to get
before turning on the lights when training. The falling-rising pattern of the light level concludes
when the SmartLights are at maximum brightness or when the light sensor is at a consistent level.

The final decision the system has to make is when it is appropriate to turn off the office lights.
In the training scenario, the home owner turns the light off when leaving the room. The motion
sensor stops being triggered around the same time that motion is no longer being detected. This has
the potential to raise issues for the learning. For example, if the home owner is stationary for a
short period of time in the room, the lights should not turn off. As well, if a new person enters
the room and then leaves shortly after, the lights should not turn off. This is why the "Time Since
Last Motion" (TSLM) variable is present. It is simply a timer that resets any time the motion sensor
detects motion. Having this variable allows the absence of motion to be a value that is submitted
to the machine learning algorithm. When the system is performing this scenario, the lights will
likely remain on for a period of time after the homeowner leaves the room until the TSLM variable
reaches a certain threshold. This threshold will be dependent on the sensitivity of the motion
sensor. The more sensitive the sensor is to motion, the smaller the threshold will be. The reason
for this is that if the sensor can detect motion such as the homeowners head moving while they are
sitting at a computer typing, it will be easier to determine that they are still in the room. If
the sensor is only able to notice large movement, this has the potential to lead to an
inconvenience to the user in the form of the lights turning off while they are still present in
the room. They would need to make a big enough motion to trigger the motion sensor, thereby
turning on the lights and resetting the TSLM variable.

##### Graphs {-}

![](./images/Scenario-NoActivity.png)

![](./images/Scenario-OfficeActivity.png)

##### Feature Extraction {-}

- Time Since Last Motion

The length of time since motion had been last detected my the PIR. If no motion is detected for a 
long period of time, then the learning could interpret it as there being no occupancy in the room. 
This could be determined by using a counter on an interval. Whenever a message is received, this
counter would be reset. If the counter reaches a certain amount of time then a message is logged 
saying no motion is detected. This feature alone is not sufficient to determine if there is a person
in the room, as they could remain still for a long amount of time. Knowing the occupancy of the room
would solve this issue. 

- Occupancy of the Room

Having a system know the occupancy of a room is not a trivial task, and is one that this scenario is
not currently equipped to be able to do. A possible solution would be to have a double break beam
on a doorway. While not perfect, this would provide a reasonably accurate count of people entering
and leaving a room. The occupancy of a room can be extracted from this data. 

- Light Level Trend

Light sensors are generally noisy and will provide many samples over a short period of time. In
order to have a more accurate representation of the state of the light in the room, the sensor
reading's could be averaged to get a general state. This average value can then be compared to
previous averages of the lights value to get the trend of the light in the room. This can be
used to indicate if the light in the room is increasing or decreasing.

- Time of Day

The time of day will be relevant when determining the light information as it can help indicate
the daylight available. It is likely that at the same time each day, the lights will be in the
same state as the day before. Using the time of day can provide a good indication of the
light levels that will be desired in the room.

#### Lighting Scenario Data {-}

The purpose of this section is to present analysis of actual device data for the 
Smart Lighting Scenario. 

##### Devices {-}

- Aeon Labs Z-wave Multisensor 6
- LB60Z-1 Z-wave Dimmable lightbulb

##### Steps to Produce {-}

1. Motion sensor and Dimmable LED set up facing each other in empty room.
2. User enters the room
3. User turns LED on to 100% brightness
4. User decreases LED brightness to low value
5. User blocks multisensor with hand
6. User increases brightness level to 100%
7. User turns off LED from Web UI and leaves the room

##### Data {-}

<pre>SELECT event_id, 
       e.timestamp, 
       e.source, 
       p.NAME, 
       pc.value, 
       e.request_id, 
       r.timestamp AS request_time, 
       r.source, 
       r.receiver 
FROM   parameter_change pc 
       JOIN event e 
         ON e.id = pc.event_id 
       JOIN parameter p 
         ON p.id = pc.parameter 
       LEFT JOIN request r 
              ON e.request_id = r.id </pre>
<table>
<TR><TH>event_id</TH>
<TH>timestamp</TH>
<TH>name</TH>
<TH>value</TH>
<TH>request_id</TH>
<TH>request_time</TH>
</TR>

<TR><TD>5</TD>
<TD>2017-02-01 03:57:12</TD>
<TD>Luminance</TD>
<TD>0.0</TD>
<TD></TD>
<TD></TD>

</TR>
<TR><TD>10</TD>
<TD>2017-02-01 03:57:19</TD>

<TD>Luminance</TD>
<TD>0.0</TD>
<TD></TD>
<TD></TD>

</TR>

<TR><TD>15</TD>
<TD>2017-02-01 03:57:25</TD>
<TD>Luminance</TD>
<TD>0.0</TD>

<TD></TD>
<TD></TD>
</TR>

<TR><TD>17</TD>
<TD>2017-02-01 03:57:26</TD>
<TD>Motion</TD>
<TD>1</TD>

<TD></TD>
<TD></TD>
</TR>

<TR><TD>18</TD>
<TD>2017-02-01 03:57:27</TD>

<TD>Level</TD>
<TD>99</TD>
<TD>1</TD>
<TD>2017-02-01 03:57:26</TD>


</TR>
<TR><TD>19</TD>
<TD>2017-02-01 03:57:27</TD>

<TD>Alarm Type</TD>
<TD>0</TD>

<TD></TD>
<TD></TD>
</TR>
<TR><TD>20</TD>
<TD>2017-02-01 03:57:27</TD>

<TD>Alarm Level</TD>
<TD>0</TD>

<TD></TD>
<TD></TD>
</TR>

<TR><TD>22</TD>
<TD>2017-02-01 03:57:27</TD>

<TD>Burglar</TD>
<TD>8</TD>

<TD></TD>
<TD></TD>
</TR>

<TR><TD>26</TD>
<TD>2017-02-01 03:57:32</TD>

<TD>Luminance</TD>
<TD>4.0</TD>

<TD></TD>
<TD></TD>
</TR>

<TR><TD>31</TD>
<TD>2017-02-01 03:57:38</TD>

<TD>Luminance</TD>
<TD>4.0</TD>

<TD></TD>
<TD></TD>
</TR>
<TR><TD>36</TD>
<TD>2017-02-01 03:57:45</TD>

<TD>Luminance</TD>
<TD>4.0</TD>

<TD></TD>
<TD></TD>
</TR>

<TR><TD>38</TD>
<TD>2017-02-01 03:57:49</TD>

<TD>Level</TD>
<TD>36</TD>
<TD>2</TD>
<TD>2017-02-01 03:57:49</TD>


</TR>

<TR><TD>42</TD>
<TD>2017-02-01 03:57:51</TD>

<TD>Luminance</TD>
<TD>1.0</TD>

<TD></TD>
<TD></TD>
</TR>
<TR><TD>43</TD>
<TD>2017-02-01 03:57:51</TD>

<TD>Level</TD>
<TD>98</TD>
<TD>3</TD>
<TD>2017-02-01 03:57:51</TD>


</TR>

<TR><TD>48</TD>
<TD>2017-02-01 03:57:58</TD>

<TD>Luminance</TD>
<TD>4.0</TD>

<TD></TD>
<TD></TD>
</TR>

<TR><TD>53</TD>
<TD>2017-02-01 03:58:04</TD>

<TD>Luminance</TD>
<TD>4.0</TD>

<TD></TD>
<TD></TD>
</TR>

<TR><TD>55</TD>
<TD>2017-02-01 03:58:09</TD>

<TD>Level</TD>
<TD>0</TD>
<TD>4</TD>
<TD>2017-02-01 03:58:09</TD>


</TR>

<TR><TD>59</TD>
<TD>2017-02-01 03:58:11</TD>

<TD>Luminance</TD>
<TD>4.0</TD>

<TD></TD>
<TD></TD>
</TR>

<TR><TD>64</TD>
<TD>2017-02-01 03:58:17</TD>

<TD>Luminance</TD>
<TD>0.0</TD>

<TD></TD>
<TD></TD>
</TR>

<TR><TD>69</TD>
<TD>2017-02-01 03:58:24</TD>

<TD>Luminance</TD>
<TD>0.0</TD>

<TD></TD>
<TD></TD>
</TR>
<TR><TD>74</TD>
<TD>2017-02-01 03:58:30</TD>

<TD>Luminance</TD>
<TD>0.0</TD>

<TD></TD>
<TD></TD>
</TR>

<TR><TD>79</TD>
<TD>2017-02-01 03:58:37</TD>

<TD>Luminance</TD>
<TD>0.0</TD>

<TD></TD>
<TD></TD>
</TR>

<TR><TD>84</TD>
<TD>2017-02-01 03:58:44</TD>

<TD>Luminance</TD>
<TD>0.0</TD>

<TD></TD>
<TD></TD>
</TR>

<TR><TD>89</TD>
<TD>2017-02-01 03:58:50</TD>

<TD>Luminance</TD>
<TD>0.0</TD>

<TD></TD>
<TD></TD>
</TR>

<TR><TD>94</TD>
<TD>2017-02-01 03:58:57</TD>

<TD>Luminance</TD>
<TD>0.0</TD>

<TD></TD>
<TD></TD>
</TR>

</table>

