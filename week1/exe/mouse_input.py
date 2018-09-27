# Examples of mouse input

import simpleguitk as simplegui
import math

# intialize globals
WIDTH = 800
HEIGHT = 800
ball_pos = [WIDTH / 2, HEIGHT / 2]
BALL_RADIUS = 15
ball_color = "Red"

# helper function
def distance(p, q):
    return math.sqrt( (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)

# define event handler for mouse click, draw
def click(pos):
    global ball_pos, ball_color
    if distance(pos, ball_pos) < BALL_RADIUS:
        ball_color = "Green"
    else:
        ball_pos = list(pos)
        ball_color = "Red"

# define a function to make ball move
def move_v1():
    global ball_pos
    # try to make the ball moving around
    if ball_pos[0] + 1 == WIDTH : 
        ball_pos[0] = 0
    else:
        ball_pos[0] += 1
    if ball_pos[1] + 1 == HEIGHT :
        ball_pos[1] = 0
    else:
        ball_pos[1] += 1


def draw(canvas):
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "Black", ball_color)
    move_v1()

# create frame
frame = simplegui.create_frame("Mouse selection", WIDTH, HEIGHT)
frame.set_canvas_background("Blue")

# register event handler
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)

# start frame
frame.start()
