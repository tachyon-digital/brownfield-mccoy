__author__ = 'George Spiceland'
#Brownfield-McCoy is a game of skill based on trying to think through often complicated and multi-layered problems
#in an attempt to access secured networks. It is also a training field for Python for the Tachyon-Digital team.

#This py contains the classes and functions pertaining to the use of nodes as a way of building a simulated internetwork
import random


class Node:
    def __init__(self, addr, ntype, neighbor, dname):
        self.addr = addr
        self.type = ntype
        self.neighbor = [neighbor]
        self.dname = dname

    def nn_transfer(self):
        if self.type == 'end':
            print('derp')


def new_node(randa1, randa2, randa3):
    if randa1 == "":
        h_a1 = str(hex(random.randint(0, 512)))
    else:
        h_a1 = randa1
    if randa2 == "":
        h_a2 = str(hex(random.randint(0, 512)))
    else:
        h_a2 = randa2
    if randa3 == "":
        h_a3 = str(hex(random.randint(0, 512)))
    else:
        h_a3 = randa3
    home_addr = str(h_a1 + '.' + h_a2 + '.' + h_a3)
    return home_addr


class NetPacket:
    def __init__(self, source, dest, size):
        self.source = source
        self.dest = dest
        self.size = size
        self.contents = []
        self.location = ''

    def p_move(self):
        print('derp')
