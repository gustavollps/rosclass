#!/usr/bin/env python

import rospy as rp
from geometry_msgs.msg import Twist

rp.init_node('node3')

kp = 1
ki = 2
kd = 3
I = 0
setpoint = 0
process_var = 0
error = 0
old_error = 0


def callBack_setpoint(msg):
    global setpoint
    setpoint = msg.linear.x


def callBack_var(msg):
    global process_var
    process_var = msg.linear.x


sub = rp.Subscriber('/setpoint', Twist, callBack_setpoint)
sub2 = rp.Subscriber('/process_var', Twist, callBack_var)
pub = rp.Publisher('/output', Twist, queue_size=1)


def timerCallBack(event):
    global kp
    global ki
    global I
    global kd
    global process_var
    global setpoint
    global error
    global old_error
    global pub

    error = setpoint - process_var
    P = kp*error
    I = I + error * ki
    D = (error - old_error)*kd

    PID = P + I + D
    error = old_error
    msg = Twist()
    msg.linear.x = PID
    pub.publish(msg)



# timer com 0.1s de periodo (10hz)
timer = rp.Timer(rp.Duration(0.1), timerCallBack)

# evita a finalizacao do script
rp.spin()
