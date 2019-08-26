#!/usr/bin/env python

import rospy as rp
from std_msgs.msg import String
from geometry_msgs.msg import Twist

rp.init_node('node6')

# variavel para receber o valor da msg
valor = 0

# callback do topico test3
def topiccallBack(msg):
    global valor
    valor = msg.linear.x


# subscriber
# arg: topic, tipo_de_msg, callback
sub = rp.Subscriber('/test3', Twist, topiccallBack)


# evita a finalizacao do script enquanto espera pelas mensagens
rp.spin()
