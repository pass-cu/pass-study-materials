import math

from consts import *

def getOnMap (x, y):
    p = math.floor(x) + math.floor(y) * MAP_HEIGHT
    return p

def pointDistance(ax, ay, bx, by):
    return math.sqrt((bx - ax) ** 2 + (by - ay) ** 2)