### Lighting Scenario Data {#section-lighting-data}

#### Purpose
The purpose of this section is to present analysis of actual device data for the 
Smart Lighting Scenario. 

#### Devices
- Aeon Labs Z-wave Multisensor 6
- LB60Z-1 Z-wave Dimmable lightbulb

#### Analysis 
TODO

#### Data
TODO: MOVE TO APPENDIX

<style>
table, th,td{
border:1px solid black;

}
table{
border-collapse:collapse;
width:100%;
cellspacing:0;
cellpadding:0;
}

tr{
text-align:center;
}
</style>
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
<TH>source</TH>
<TH>name</TH>
<TH>value</TH>
<TH>request_id</TH>
<TH>request_time</TH>
</TR>
<TR><TD>1</TD>
<TD>2017-02-01 03:57:06</TD>
<TD>Ultraviolet</TD>
<TD>0.0</TD>
<TD></TD>
<TD></TD>
<TD></TD>

</TR>
<TR><TD>2</TD>
<TD>2017-02-01 03:57:11</TD>
<TD>Temperature</TD>
<TD>67.5</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>3</TD>
<TD>2017-02-01 03:57:11</TD>
<TD>Relative Humidity</TD>
<TD>29.0</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>4</TD>
<TD>2017-02-01 03:57:12</TD>
<TD>Battery Level</TD>
<TD>100</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>5</TD>
<TD>2017-02-01 03:57:12</TD>

<TD>Luminance</TD>
<TD>0.0</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>6</TD>
<TD>2017-02-01 03:57:12</TD>

<TD>Ultraviolet</TD>
<TD>0.0</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>7</TD>
<TD>2017-02-01 03:57:17</TD>

<TD>Temperature</TD>
<TD>67.5</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>8</TD>
<TD>2017-02-01 03:57:18</TD>

<TD>Relative Humidity</TD>
<TD>29.0</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>9</TD>
<TD>2017-02-01 03:57:18</TD>

<TD>Battery Level</TD>
<TD>100</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>10</TD>
<TD>2017-02-01 03:57:19</TD>

<TD>Luminance</TD>
<TD>0.0</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>11</TD>
<TD>2017-02-01 03:57:19</TD>

<TD>Ultraviolet</TD>
<TD>0.0</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>12</TD>
<TD>2017-02-01 03:57:24</TD>

<TD>Temperature</TD>
<TD>67.5</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>13</TD>
<TD>2017-02-01 03:57:24</TD>

<TD>Relative Humidity</TD>
<TD>29.0</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>14</TD>
<TD>2017-02-01 03:57:25</TD>

<TD>Battery Level</TD>
<TD>100</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>15</TD>
<TD>2017-02-01 03:57:25</TD>

<TD>Luminance</TD>
<TD>0.0</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>16</TD>
<TD>2017-02-01 03:57:25</TD>

<TD>Ultraviolet</TD>
<TD>0.0</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>17</TD>
<TD>2017-02-01 03:57:26</TD>

<TD>Sensor</TD>
<TD>1</TD>
<TD></TD>
<TD></TD>
<TD></TD>

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
<TD></TD>

<TR><TD>20</TD>
<TD>2017-02-01 03:57:27</TD>

<TD>Alarm Level</TD>
<TD>0</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>21</TD>
<TD>2017-02-01 03:57:27</TD>

<TD>SourceNodeId</TD>
<TD>0</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>22</TD>
<TD>2017-02-01 03:57:27</TD>

<TD>Burglar</TD>
<TD>8</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>23</TD>
<TD>2017-02-01 03:57:30</TD>

<TD>Temperature</TD>
<TD>67.5</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>24</TD>
<TD>2017-02-01 03:57:31</TD>

<TD>Relative Humidity</TD>
<TD>29.0</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>25</TD>
<TD>2017-02-01 03:57:32</TD>

<TD>Battery Level</TD>
<TD>100</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>26</TD>
<TD>2017-02-01 03:57:32</TD>

<TD>Luminance</TD>
<TD>4.0</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>27</TD>
<TD>2017-02-01 03:57:32</TD>

<TD>Ultraviolet</TD>
<TD>0.0</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>28</TD>
<TD>2017-02-01 03:57:37</TD>

<TD>Temperature</TD>
<TD>67.5999984741211</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>29</TD>
<TD>2017-02-01 03:57:37</TD>

<TD>Relative Humidity</TD>
<TD>29.0</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>30</TD>
<TD>2017-02-01 03:57:38</TD>

<TD>Battery Level</TD>
<TD>100</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>31</TD>
<TD>2017-02-01 03:57:38</TD>

<TD>Luminance</TD>
<TD>4.0</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>32</TD>
<TD>2017-02-01 03:57:38</TD>

<TD>Ultraviolet</TD>
<TD>0.0</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>33</TD>
<TD>2017-02-01 03:57:43</TD>

<TD>Temperature</TD>
<TD>67.5</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>34</TD>
<TD>2017-02-01 03:57:44</TD>

<TD>Relative Humidity</TD>
<TD>29.0</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>35</TD>
<TD>2017-02-01 03:57:45</TD>

<TD>Battery Level</TD>
<TD>100</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>36</TD>
<TD>2017-02-01 03:57:45</TD>

<TD>Luminance</TD>
<TD>4.0</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>37</TD>
<TD>2017-02-01 03:57:45</TD>

<TD>Ultraviolet</TD>
<TD>0.0</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>38</TD>
<TD>2017-02-01 03:57:49</TD>

<TD>Level</TD>
<TD>36</TD>
<TD>2</TD>
<TD>2017-02-01 03:57:49</TD>


</TR>
<TR><TD>39</TD>
<TD>2017-02-01 03:57:50</TD>

<TD>Temperature</TD>
<TD>67.5999984741211</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>40</TD>
<TD>2017-02-01 03:57:50</TD>

<TD>Relative Humidity</TD>
<TD>29.0</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>41</TD>
<TD>2017-02-01 03:57:51</TD>

<TD>Battery Level</TD>
<TD>100</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>42</TD>
<TD>2017-02-01 03:57:51</TD>

<TD>Luminance</TD>
<TD>1.0</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>43</TD>
<TD>2017-02-01 03:57:51</TD>

<TD>Level</TD>
<TD>98</TD>
<TD>3</TD>
<TD>2017-02-01 03:57:51</TD>


</TR>
<TR><TD>44</TD>
<TD>2017-02-01 03:57:51</TD>

<TD>Ultraviolet</TD>
<TD>0.0</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>45</TD>
<TD>2017-02-01 03:57:57</TD>

<TD>Temperature</TD>
<TD>67.5999984741211</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>46</TD>
<TD>2017-02-01 03:57:57</TD>

<TD>Relative Humidity</TD>
<TD>29.0</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>47</TD>
<TD>2017-02-01 03:57:58</TD>

<TD>Battery Level</TD>
<TD>100</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>48</TD>
<TD>2017-02-01 03:57:58</TD>

<TD>Luminance</TD>
<TD>4.0</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>49</TD>
<TD>2017-02-01 03:57:58</TD>

<TD>Ultraviolet</TD>
<TD>0.0</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>50</TD>
<TD>2017-02-01 03:58:03</TD>

<TD>Temperature</TD>
<TD>67.5999984741211</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>51</TD>
<TD>2017-02-01 03:58:03</TD>

<TD>Relative Humidity</TD>
<TD>29.0</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>52</TD>
<TD>2017-02-01 03:58:04</TD>

<TD>Battery Level</TD>
<TD>100</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>53</TD>
<TD>2017-02-01 03:58:04</TD>

<TD>Luminance</TD>
<TD>4.0</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>54</TD>
<TD>2017-02-01 03:58:04</TD>

<TD>Ultraviolet</TD>
<TD>0.0</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>55</TD>
<TD>2017-02-01 03:58:09</TD>

<TD>Level</TD>
<TD>0</TD>
<TD>4</TD>
<TD>2017-02-01 03:58:09</TD>


</TR>
<TR><TD>56</TD>
<TD>2017-02-01 03:58:10</TD>

<TD>Temperature</TD>
<TD>67.5999984741211</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>57</TD>
<TD>2017-02-01 03:58:10</TD>

<TD>Relative Humidity</TD>
<TD>29.0</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>58</TD>
<TD>2017-02-01 03:58:11</TD>

<TD>Battery Level</TD>
<TD>100</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>59</TD>
<TD>2017-02-01 03:58:11</TD>

<TD>Luminance</TD>
<TD>4.0</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>60</TD>
<TD>2017-02-01 03:58:11</TD>

<TD>Ultraviolet</TD>
<TD>0.0</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>61</TD>
<TD>2017-02-01 03:58:16</TD>

<TD>Temperature</TD>
<TD>67.5999984741211</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>62</TD>
<TD>2017-02-01 03:58:17</TD>

<TD>Relative Humidity</TD>
<TD>29.0</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>63</TD>
<TD>2017-02-01 03:58:17</TD>

<TD>Battery Level</TD>
<TD>100</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>64</TD>
<TD>2017-02-01 03:58:17</TD>

<TD>Luminance</TD>
<TD>0.0</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>65</TD>
<TD>2017-02-01 03:58:18</TD>

<TD>Ultraviolet</TD>
<TD>0.0</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>66</TD>
<TD>2017-02-01 03:58:23</TD>

<TD>Temperature</TD>
<TD>67.5</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>67</TD>
<TD>2017-02-01 03:58:23</TD>

<TD>Relative Humidity</TD>
<TD>29.0</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>68</TD>
<TD>2017-02-01 03:58:24</TD>

<TD>Battery Level</TD>
<TD>100</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>69</TD>
<TD>2017-02-01 03:58:24</TD>

<TD>Luminance</TD>
<TD>0.0</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>70</TD>
<TD>2017-02-01 03:58:24</TD>

<TD>Ultraviolet</TD>
<TD>0.0</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>71</TD>
<TD>2017-02-01 03:58:29</TD>

<TD>Temperature</TD>
<TD>67.5999984741211</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>72</TD>
<TD>2017-02-01 03:58:30</TD>

<TD>Relative Humidity</TD>
<TD>29.0</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>73</TD>
<TD>2017-02-01 03:58:30</TD>

<TD>Battery Level</TD>
<TD>100</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>74</TD>
<TD>2017-02-01 03:58:30</TD>

<TD>Luminance</TD>
<TD>0.0</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>75</TD>
<TD>2017-02-01 03:58:31</TD>

<TD>Ultraviolet</TD>
<TD>0.0</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>76</TD>
<TD>2017-02-01 03:58:36</TD>

<TD>Temperature</TD>
<TD>67.5999984741211</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>77</TD>
<TD>2017-02-01 03:58:36</TD>

<TD>Relative Humidity</TD>
<TD>29.0</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>78</TD>
<TD>2017-02-01 03:58:37</TD>

<TD>Battery Level</TD>
<TD>100</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>79</TD>
<TD>2017-02-01 03:58:37</TD>

<TD>Luminance</TD>
<TD>0.0</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>80</TD>
<TD>2017-02-01 03:58:37</TD>

<TD>Ultraviolet</TD>
<TD>0.0</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>81</TD>
<TD>2017-02-01 03:58:42</TD>

<TD>Temperature</TD>
<TD>67.5999984741211</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>82</TD>
<TD>2017-02-01 03:58:43</TD>

<TD>Relative Humidity</TD>
<TD>29.0</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>83</TD>
<TD>2017-02-01 03:58:43</TD>

<TD>Battery Level</TD>
<TD>100</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>84</TD>
<TD>2017-02-01 03:58:44</TD>

<TD>Luminance</TD>
<TD>0.0</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>85</TD>
<TD>2017-02-01 03:58:44</TD>

<TD>Ultraviolet</TD>
<TD>0.0</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>86</TD>
<TD>2017-02-01 03:58:49</TD>

<TD>Temperature</TD>
<TD>67.5999984741211</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>87</TD>
<TD>2017-02-01 03:58:49</TD>

<TD>Relative Humidity</TD>
<TD>29.0</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>88</TD>
<TD>2017-02-01 03:58:50</TD>

<TD>Battery Level</TD>
<TD>100</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>89</TD>
<TD>2017-02-01 03:58:50</TD>

<TD>Luminance</TD>
<TD>0.0</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>90</TD>
<TD>2017-02-01 03:58:50</TD>

<TD>Ultraviolet</TD>
<TD>0.0</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>91</TD>
<TD>2017-02-01 03:58:55</TD>

<TD>Temperature</TD>
<TD>67.5</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>92</TD>
<TD>2017-02-01 03:58:56</TD>

<TD>Relative Humidity</TD>
<TD>29.0</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>93</TD>
<TD>2017-02-01 03:58:57</TD>

<TD>Battery Level</TD>
<TD>100</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>94</TD>
<TD>2017-02-01 03:58:57</TD>

<TD>Luminance</TD>
<TD>0.0</TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TR><TD>95</TD>
<TD>2017-02-01 03:58:57</TD>

<TD>Ultraviolet</TD>
<TD>0.0</TD>
<TD></TD>
<TD></TD>
<TD></TD>

</table>