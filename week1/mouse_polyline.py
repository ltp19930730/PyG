import math
import simpleguitk as simplegui

polyline = []


# define mouseclick handler
def click(pos):
          
# button to clear canvas
def clear():

# define draw
def draw(canvas):
                   
# create frame and register handlers
frame = simplegui.create_frame("Echo click", 300, 200)
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)
frame.add_button("Clear", clear)

# start frame
frame.start()

