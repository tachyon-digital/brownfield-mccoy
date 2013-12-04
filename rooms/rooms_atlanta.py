__author__ = 'George Spiceland'


#This file contains rooms for the "Atlanta" network area.

import rooms.handler

#Exits dictionary
a001 = rooms.handler.RoomUnit
a001.rid = 1
a001.exits = ['N', 'S']
a001.desc = 'A dimly lit empty room.'
a001.objects = 'Computer'
a002 = rooms.handler.RoomUnit
a002.rid = 2

plid = [1, 1]

rdict = {[1, 1]: a001, [2, 1]: a002}
clid = rdict[plid]
print(clid.desc)
print(clid.exits)