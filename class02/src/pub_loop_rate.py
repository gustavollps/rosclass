#!/usr/bin/env python

import rospy as rp
from geometry_msgs.msg import Twist

rp.init_node('node2')

msg = Twist()
msg.liner.x = 1

pub = rp.Publisher('/test2', Twist, queue_size=1)


rate = rp.Rate(10) # 10hz

while not rp.is_shutdown():
   pub.publish(msg)
   rate.sleep()