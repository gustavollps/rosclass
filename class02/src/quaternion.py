#!/usr/bin/env python

import rospy as rp
from nav_msgs.msg import Odometry
import tf
import math

rp.init_node('node5')
quat = [0,0,0,0]

def callBack(msg):
    global quat
    quaternion = msg.pose.pose.orientation
    quat = [quaternion.x, quaternion.y, quaternion.z, quaternion.w]
    euler = tf.transformations.euler_from_quaternion(quat)
    rp.loginfo(180*euler[2]/math.pi) # angulo em graus


sub = rp.Subscriber('/RosAria/pose', Odometry, callBack)

rp.spin()
