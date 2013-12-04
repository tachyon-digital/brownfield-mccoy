__author__ = 'George Spiceland'


#This file contains classes and functions for the generation and handling of rooms.

class RoomUnit:
    def __init__(self):
        self.rid = 0
        self.exits = []
        self.links = []
        self.desc = []
        self.objects = []