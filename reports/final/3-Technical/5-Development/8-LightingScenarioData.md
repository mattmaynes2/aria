### Lighting Scenario Data {#section-lighting-data}

#### Purpose {-}

The purpose of this section is to present analysis of actual device data for the 
Smart Lighting Scenario. 

#### Devices {-}

- Aeon Labs Z-wave Multisensor 6
- LB60Z-1 Z-wave Dimmable lightbulb

#### Steps to Produce {-}

1. Motion sensor and Dimmable LED set up facing each other in empty room.
2. User enters the room
3. User turns LED on to 100% brightness
4. User decreases LED brightness to low value
5. User blocks multisensor with hand
6. User increases brightness level to 100%
7. User turns off LED from Web UI and leaves the room

#### Data {-}

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
