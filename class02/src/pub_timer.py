#!/usr/bin/env python

import rospy as rp
from std_msgs.msg import String

rp.init_node('node1', anonymous=True)
# anynomous: mata outro node com nome igual na inicializacao
# caso contrario, adiciona um numero na frente do novo node

msg = String()
msg.data = 'coisa'

pub = rp.Publisher('/test1', String, queue_size=1)


def timerCallBack(event):
    pub.publish(msg)

# timer com 0.1s de periodo (10hz)
timer = rp.Timer(rp.Duration(0.1), timerCallBack)


# evita a finalizacao do script
rp.spin()
