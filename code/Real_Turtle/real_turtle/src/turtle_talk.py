#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from sound_play.libsoundplay import SoundClient
import sys
# Create the sound client object
soundhandle = SoundClient()

def turtle_talk():
    rospy.init_node('turtle_talk')
    soundhandle.say("Please select boundry points", "voice_kal_diphone")
    rospy.sleep(2)

def callback(bin_value):
       soundhandle.say("bin detected", "voice_kal_diphone")
       rospy.sleep(2)
       soundhandle.stopAll()

def listener():

    rospy.Subscriber("turtle_link", String, callback)
    #soundhandle.stopAll()
    #rospy.spin() 

if __name__=="__main__":
    try:
        turtle_talk()
        listener()

    except rospy.ROSInterruptException:
        rospy.loginfo("Talking error.")
