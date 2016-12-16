#!/usr/bin/env python

import rospy
from geometry_msgs.msg import PointStamped,Point
from std_msgs.msg import Header

def point():
    pub = rospy.Publisher('/clicked_point', PointStamped, queue_size=10)
    rospy.init_node('point', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    point1 = PointStamped(Header(0,1,'/map'),Point(3.000, 3.000, 0.000))
    pub.publish(point1)
    point2 = PointStamped(Header(1,2,'map'),Point(-3.000, 3.000, 0.000))
    pub.publish(point2)
    point3 = PointStamped(Header(2,3,'map'),Point(-3.000, -3.000, 0.000))
    pub.publish(point1)
    point4 = PointStamped(Header(3,4,'map'),Point(3.000, -3.000, 0.000))
    pub.publish(point4)
    point5 = PointStamped(Header(4,5,'map'),Point(3.000, 3.000, 0.000))
    pub.publish(point5)
    point6 = PointStamped(Header(5,6,'map'),Point(0.000, 0.000, 0.000))
    pub.publish(point6)
    rate.sleep()

if __name__ == '__main__':
    try:
        point()
    except rospy.ROSInterruptException:
        pass
