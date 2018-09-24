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
        pos = self.pos
        if self.exposed:
            text_location = [pos[0] + 0.2 * TILE_WIDTH, pos[1] - 0.3 * TILE_HEIGHT]
            canvas.draw_text(str(self.number), text_location, TILE_WIDTH, 'White')
        else:
            tile_corners = (pos, [pos[0] + TILE_WIDTH, pos[1]], [pos[0] + TILE_WIDTH, pos[1] - TILE_HEIGHT], [pos[0], pos[1] - TILE_HEIGHT])
            canvas.draw_polygon(tile_corners, 1, "Red", "Green")

# draw handler
def draw(canvas):
    tile1.draw_tile(canvas)
    tile2.draw_tile(canvas)

frame = simplegui.create_frame("Memory", 2 * TILE_WIDTH, TILE_HEIGHT)
frame.set_draw_handler(draw)


tile1 = Tile(3, True, [0, TILE_HEIGHT])
tile2 = Tile(5, False, [TILE_WIDTH, TILE_HEIGHT])

frame.start()
