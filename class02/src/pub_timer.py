#!/usr/bin/env python

import rospy as rp
from std_msgs.msg import String

rp.init_node('node1')

msg = String()
msg.data = 'coisa'

pub = rp.Publisher('/test1', String, queue_size=1)


def timerCallBack(event):
    pub.publish(msg)

# timer com 0.1s de periodo (10hz)
timer = rp.Timer(rp.Duration(0.1), timerCallBack)


# evita a finalizacao do script
rp.spin()
