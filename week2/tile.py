class Tile:
    def __init__(self, num, exp):
        self.number = num
        self.exposed = exp

    def get_number(self):
        return self.number

    def is_exposed(self):
        return self.exposed

    def expose_tile(self):
        self.exposed = True

    def hide_tile(self):
        self.exposed = False


myTile = Tile(5)

print Tile
print myTile.number
print myTile.get_number()
