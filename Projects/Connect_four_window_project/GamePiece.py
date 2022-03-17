class GamePiece:
    def __init__(self, color, key):
        self.color = color
        self.key = key
        self.column = key % 7
        self.x_coord = (self.column * 110) + 13

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

