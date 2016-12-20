#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from sound_play.libsoundplay import SoundClient
import sys

class turtle_start:
    def __init__(self):
        rospy.init_node('turtle_start')

        self.wavepath = rospy.get_param("~wavepath",sys.path[0] + "/../sounds")
        
        # Create the sound client object
        self.soundhandle = SoundClient()
        
        rospy.sleep(1)
        
        # Announce that we are ready for input
        self.soundhandle.playWave(self.wavepath + "/R2D2a.wav")

        rospy.sleep(2)
        self.soundhandle.say("welcome ", "voice_kal_diphone")

        rospy.sleep(2)
        self.soundhandle.say("process starting ", "voice_kal_diphone")
        
if __name__=="__main__":
    try:
        turtle_start()
        #rospy.spin()
    except rospy.ROSInterruptException:
        rospy.loginfo("Talking error.")
