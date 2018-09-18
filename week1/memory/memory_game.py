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
number = []
offset = [15, 40]

def init():
    global number
    number = [i for i in range(32)]
    tmp = number.copy()
    tmp.extend(number)
    random.shuffle(tmp)
    print(tmp)
    number = tmp

def draw(canvas):
    global lines
    global number
    for line in lines:
        canvas.draw_line(line[0], line[1], 2, 'Blue')
        canvas.draw_line(line[0][::-1], line[1][::-1], 2, 'Blue')
    for i in range(8):
        for j in range(8):
            canvas.draw_text(number[i*8+j], (i*50 + offset[0], j * 50 + offset[1]), 25, 'Green')

# create frame and add a button and labels
frame = sg.create_frame("Memory", 400,400)
frame.add_button("Reset", new_game, 60)
label = frame.add_label("Turns = 0")
init()

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
