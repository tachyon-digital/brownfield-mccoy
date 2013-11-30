__author__ = 'George Spiceland'
#Brownfield-McCoy is a game of skill based on trying to think through often complicated and multi-layered problems
#in an attempt to access secured networks. It is also a training field for Python for the Tachyon-Digital team.

#This py contains the classes and functions pertaining to the use of nodes as a way of building a simulated internetwork


class Node:
    def __init__(self, addr, type, neighbor):
        self.addr = addr
        self.type = type
        self.neighbor = neighbor
        self.dname = []


#def new_node():
