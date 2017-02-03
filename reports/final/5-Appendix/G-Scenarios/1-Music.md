### G-1 Music Automation {- #G-1}

#### Sample Sequence {-}

###### Setup {-}

The home's main entrance is equipped with two break-beam motion sensors in series. The devices are
configured so that they provide an estimate of the number of people in the house (OccupancyCount).
Each of the main rooms contains an audio sensor (DenAudio, BasementAudio), and a sound system 
(DenSpeakers, BasementSpeakers). Each room also contains a motion sensor 
(DenMotion, BasementMotion). The basement is also set up with a strip of coloured smart lights.

###### Training Sequence {-}

With their central hub in training mode, the homeowner arrives at the house with a car full of 
people. As each person enters the home, the motion sensors at the door notify the central hub that
the number of people in the house is increasing. The party moves into the den and turns on some music. 
DenMotion reports the activity in the den to the central hub. The homeowner lowers the thermostat
temperature so that the increased number of visitors doesn't make the house uncomfortable.
As the level of conversation increases in the den, the homeowner decides to turn down the music to 
avoid noise complaints from the neighbour. Throughout the party, DenAudio reports changes in noise 
level to the central hub. When the homeowner changes the volume of the den speakers, DenSpeaker 
reports the change in its output to the central hub.

After an hour, half of the party moves to the basement to play some Scrabble. BasementMotion reports
the new activity in the basement to the central hub. The Scrabble players decide to turn on some 
music to get everyone in the mood. BasementSpeakers reports the change in its state to the central 
hub. The homeowner decides to show off his light strips to his friends, and sets them to a dim red
colour to enhance the party ambiance. The light strips report their colour and brightness level to 
the central hub (BasementLightStrip).

At the end of the night, everyone goes home. All music in the house turns off, the basement 
lightstrips turn off, and the thermostat is returned to its normal setting.

##### Expected Inputs {-}

The log for this scenario is shown below. This log demonstrates the interactions that would
be logged. 

```
2017-01-01 19:00:00 OccupancyCount: 1
2017-01-01 19:00:01 OccupancyCount: 2
2017-01-01 19:00:02 OccupancyCount: 3
2017-01-01 19:00:03 OccupancyCount: 4
...
2017-01-01 19:05:00 OccupancyCount: 10
2017-01-01 19:06:50 MotionDen: Motion Detected
2017-01-01 19:10:00 DenAudio: Sound level 100
2017-01-01 19:10:30 DenSpeakers: Volume 80%
2017-01-01 19:11:00 DenAudio: Sound level 95
2017-01-01 19:11:15 Thermostat: Temperature 17 C
2017-01-01 19:11:30 DenAudio: Sound level 100
...
2017-01-01 20:00:30 DenAudio: Sound level 200
2017-01-01 20:05:00 DenSpeakeк: Volume 70%
2017-01-01 20:05:30 DenAudio: Sound level 150
...
2017-01-01 20:29:50 MotionBasement: Motion Detected
2017-01-01 20:29:55 BasementSpeaker: Volume 60%
2017-01-01 20:30:00 BasementLightStrips: Colour red
2017-01-01 20:30:00 BasementLightStrips: Brightness 50%
...

2017-01-02 01:00:00 OccupancyCount: 2
2017-01-02 01:02:00 BasementMotion: No activity
2017-01-02 01:03:10 DenMotion: No activity
2017-01-02 01:03:15 DenAudio: Sound level 10
2017-01-02 01:03:16 BasementSpeaker: Volume 0%
2017-01-02 01:03:17 BasementLightStrips: Off
2017-01-02 01:03:18 DenSpeaker: Volume 0%
2017-01-02 01:05:00 Thermostat: 20 C
...
```

##### Expected Behaviour {-}

The next time the homeowner has a Scrabble party, 10 guests arrive at the home. After they step
through the door and motion is detected in the den, the den sound system turns on and adjusts its
volume to an appropriate level. The thermostat lowers the temperature of the room to 20 degrees. 
The system continues to adjust the volume of the sound system to 
match the amount of noise detected in the room.

A group of the partygoers decide to move down to the basement for their game. When motion is 
detected in the basement, the system turns on the lightstrips to a dim red colour and turns the 
basement sound system on.

After everyone leaves for the night, BasementLightStrips, BasementSpeaker, and DenSpeakers turn off.
Thermostat is re-adjusted to the temperature before the party began.
