### TV Automation

> Author: Peter Mark & Matthew Maynes <br/>
> Editor: Peter Mark <br/>
> Updated: October 26, 2016 <br/>

#### Background {-}

Automation of a smart home should go beyond simple tasks and make it easy to stay on top of a busy
schedule. Your favourite TV show is on every week at the same time but your schedule changes from
week to week. The smart home system should recognize that this channel is on at the same time
each week and that it is a show of interest. If one week you cannot make it to watch the show, you
should not be bothered to have to set up the personal recording device, the smart home system
should record the show for you.

#### System Interaction {-}

The automation system will have to interact with a smart TV in order to communicate the channel
information of the TV. The system will also need to have access to a personal video recording
device.

To train the system to record a show, the user could watch a show one week and then record it the
next week. The user could teach the system that recoding should happen when they are not present
by setting the system to record when they are not in the room. If there are motion sensors then
the system could detect the user's presence.


#### System Requirements {-}

To be able to determine if the user is present in the home, the system will need sensors for motion.
 The following is a list of sensors that will be needed for this scenario.

| Sensor        | Usage                                         |
| ------------- | --------------------------------------------- |
| Motion Sensor | Will provide information about home occupancy |


The system will also need to be able to communicate to a smart TV and digital video recording
device for recording TV shows. The following smart devices will be needed to control TV channels
and record TV shows.

| Device         | Usage                                                                        |
| -------------- | ---------------------------------------------------------------------------- |
| Smart TV       | TV that can communication channel information and can be controlled remotely |
| Video Recorder | Recorder for capturing the user's TV show                                    |

For this scenario to be feasible, there would need to be several motion sensors connected across the
home. The input received from these motion sensors (the input being interpreted as binary input 
for movement or no movement) would be used to determine if people were present at the home. If the
motion sensors determine that there are people in the home, then the hub would instruct the Smart
TV to turn on to the appropriate channel. Otherwise the hub would instruct the Video Recorder to 
beign recording the desired show.

Our research has concluded that there are no feasible options for Smart TVs or Video Recorder 
devices that are Z-Wave compatible, making this scenario an infeasible option for implementation in 
our project. However, the scenario demonstrates the potential learning capibilities of the system, 
and could be a stretch goal for future developers. If our system could be expanded to include other
communication APIs, such as the Samsung SmartHome, then Smart TV devices would become available and
the scenario could be implemented.

