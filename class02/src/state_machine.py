#!/usr/bin/env python

import rospy as rp
from std_msgs.msg import String
from geometry_msgs.msg import Twist

rp.init_node('node3')

# msg
msg = String()
msg.data = 'coisa'

# callback do topico test3_1
def topiccallBack(msg):
    valor = msg.linear.x


# publisher e subscriber
pub = rp.Publisher('/test3', String, queue_size=1)
sub = rp.Subscriber('/test3_1', Twist, topiccallBack)

estado = 0
valor = 0


def timerCallBack(event):
    global estado
    global valor

    if estado == 1:
        pub.publish(msg)
        # condicao para sair
        if valor == 5:
            estado = 2
    elif estado == 2:
        print 'chegou no estado: ' + str(estado)
        estado = 3
    elif estado == 3:
        print 'chegou no estado: ' + str(estado)
    else:
        estado = 1


# timer com 0.1s de periodo (10hz)
timer = rp.Timer(rp.Duration(0.1), timerCallBack)

# evita a finalizacao do script
rp.spin()
