import simpleguitk as simplegui

#define globals
TILE_WIDTH = 50
TILE_HEIGHT = 100

# definition of a Tile class
class Tile:
    def __init__(self, num, exp, loc):
        self.number = num
        self.exposed = exp
        self.loc = loc

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
        loc = self.loc
        if self.exposed:
            text_location = [loc[0] + 0.2 * TILE_WIDTH, loc[1] - 0.3 * TILE_HEIGHT]
            canvas.draw_text(str(self.number), text_location, TILE_WIDTH, 'White')
        else:
            tile_corners = (loc, [loc[0] + TILE_WIDTH, loc[1]], [loc[0] + TILE_WIDTH, loc[1] - TILE_HEIGHT], [loc[0], loc[1] - TILE_HEIGHT])
            canvas.draw_polygon(tile_corners, 1, "Red", "Green")
    # selection method for tiles
    def is_selected(self, pos):
        loc = self.loc
      #  if pos[0] < loc[0] + TILE_WIDTH and pos[0] > loc[0]:
      #      if pos[1] < loc[1] and pos[1] > loc[1] - TILE_HEIGHT:
      #          return True
        inside_hor = loc[0] <= pos[0] <= loc[0] + TILE_WIDTH
        inside_vert = loc[1] - TILE_HEIGHT <= pos[1] <= loc[1]
        return inside_hor and inside_vert


#define event handlers
def mouseclick(pos):
    for tile in tiles:
        if tile.is_selected(pos):
            if tile.is_exposed():
                tile.hide_tile()
            else:
                tile.expose_tile()


# draw handler
def draw(canvas):
    for tile in tiles:
        tile.draw_tile(canvas)

frame = simplegui.create_frame("Memory", 2 * TILE_WIDTH, TILE_HEIGHT)
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(mouseclick)


tile1 = Tile(3, True, [0, TILE_HEIGHT])
tile2 = Tile(5, False, [TILE_WIDTH, TILE_HEIGHT])
tiles = [tile1, tile2]

frame.start()
