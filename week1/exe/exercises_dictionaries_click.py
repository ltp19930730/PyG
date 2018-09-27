# Image positioning problem

###################################################
# Student should enter code below

import simpleguitk as sg

# global constants
WIDTH = 1000
HEIGHT = 1000
click_pos = [WIDTH/2, HEIGHT/2]

# load test image
image_st = sg.load_image("https://avatars2.githubusercontent.com/u/15324716?s=400&u=037e1fd9b770fd07e2b93a6a0a468449e296978d&v=4")
image_sz = [image_st.get_width(), image_st.get_height()]
image_ct = [image_sz[0]/2, image_sz[1]/2]

# mouseclick handler
def click(pos):
    global click_pos
    click_pos = pos
    
# draw handler
def draw(canvas):
    canvas.draw_image(image_st, image_ct, image_sz,
                        click_pos, image_sz)

    
# create frame and register draw handler    
frame = sg.create_frame("Test image", WIDTH, HEIGHT)
frame.set_canvas_background("Gray")
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)

# start frame
frame.start()
        
