import simpleguitk as sg
import random

def new_game():
    pass

#define event handlers
def mouseclick(pos):
    #add game state logic here
    pass

#cards are logically 50x50 pixels in size
def layout():
    lines_number = 400 // 50
    lines = []
    for i in range(1,lines_number):
        lines.append(([i*50, 0], [i*50, 400]))
    print(lines)
    return lines

lines = layout()

def draw(canvas):
    global lines
    for line in lines:
        canvas.draw_line(line[0], line[1], 2, 'Blue')
        canvas.draw_line(line[0][::-1], line[1][::-1], 2, 'Blue')

# create frame and add a button and labels
frame = sg.create_frame("Memory", 400,400)
frame.add_button("Reset", new_game, 60)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
