import simpleguitk as simplegui
import math

#define global constants
RADIUS = 20
RED_POS = [50, 100]
GREEN_POS = [150, 100]
BLUE_POS = [250, 100]

#define helper function
def dist(p, q):
    return math.sqrt((p[0]  - q[0]) ** 2 + (p[1] - q[1]) ** 2)

def click(pos):
    if dist(pos, RED_POS) < RADIUS:
