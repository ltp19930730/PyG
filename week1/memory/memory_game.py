import simpleguitk as sg
import copy
import random

FRONT = 1
BACK = 0

def new_game():
    pass

# define a function from mapping the area to the index of list
def getIndex(pos):
    x = pos[0] // 50
    y = pos[1] // 50
    return x*8 + y


#define event handlers
def mouseclick(pos):
    #add game state logic here
    global number
    index = getIndex(pos)
    if number[index][1] == 0:
        # the card is in the back state
        number[index][1] = 1

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
    number = [[i,0] for i in range(32)]
    tmp = copy.deepcopy(number)
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
            if number[i*8+j][1] == FRONT:
                canvas.draw_text(number[i*8+j][0], (i*50 + offset[0], j * 50 + offset[1]), 25, 'Green')

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
