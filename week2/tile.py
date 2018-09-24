import simpleguitk as simplegui

#define globals
TILE_WIDTH = 50
TILE_HEIGHT = 100

# definition of a Tile class
class Tile:
    def __init__(self, num, exp, pos):
        self.number = num
        self.exposed = exp
        self.pos = pos

    def get_number(self):
        return self.number

    def is_exposed(self):
        return self.exposed

    def expose_tile(self):
        self.exposed = True

    def hide_tile(self):
        self.exposed = False

    def __str__(self):
        return "Number is " + str(self.number) + ", exposed is " + str(self.exposed)

    def draw_tile(self, canvas):
        if self.exposed:
            canvas.draw_text(str(self.number), self.pos, 30, 'red')

# draw handler
def draw(canvas):
    tile1.draw_tile(canvas)
    tile2.draw_tile(canvas)

frame = simplegui.create_frame("Memory", 2 * TILE_WIDTH, TILE_HEIGHT)
frame.set_draw_handler(draw)


tile1 = Tile(3, True, [0, TILE_HEIGHT])
tile2 = Tile(5, True, [TILE_WIDTH, TILE_HEIGHT])

frame.start()
