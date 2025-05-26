from Bishop import Bishop
from Rook import Rook

class Queen(Bishop, Rook):

    def __init__(self, color, row, col):
        super().__init__(color, row, col)

    # make the piece move
    def move(self):
        pass

    # show what piece threat on other piece on the board
    def threaten(self):
        pass

    # show if there is a check situation on the board
    def check(self):
        pass

