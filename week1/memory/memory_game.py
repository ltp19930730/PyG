#! /usr/local/bin/python3
import simpleguitk as sg
import copy
import random

FRONT = 1
BACK = 0
state = 0
prev = [[],[]]
total_turns = 0

def new_game():
    #initialize all the global value
    global state, total_turns, label
    state = 0
    total_turns = 0
    label.set_text("Turns : 0")
    init()

# define a function from mapping the area to the index of list
def getIndex(pos):
    x = pos[0] // 50
    y = pos[1] // 50
    return x*8 + y

def addTurns():
    global total_turns, label
    total_turns += 1
    label.set_text("Turns : " + str(total_turns))


#define event handlers
def mouseclick(pos):
    #add game state logic here
    global number, state, prev
    index = getIndex(pos)
    while 1:
        if state == 0 :
            if number[index][1] == BACK:
                # the card is in the back state
                number[index][1] = FRONT
                prev[0] = [index, number[index][0]]
                state = 1
                addTurns() # increase the counter
            break
        elif state == 1:
            if number[index][1] == BACK:
                prev[1] = [index, number[index][0]]
                number[index][1] = FRONT
                state = 2
                addTurns() # increase the counter
            break
        elif state == 2:
            if number[index][1] == BACK:
                # compare the previous card
                if prev[0][1] != prev[1][1] :
                    ## flip the two unpaired cards over
                    number[prev[0][0]][1] = BACK
                    number[prev[1][0]][1] = BACK
                state = 0
            else:
                break

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
    number = [[i,BACK] for i in range(32)]
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
label = frame.add_label("Turns: 0")


# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
