from Piece import Piece


class Pawn(Piece):

    def __init__(self,name,  value, color):
        self.piece = {name, value}
        self.color = color

    # prevent pieces to move to where they cant
    def cannot_move(self):
        pass

    # make the piece move
    def move(self):
        pass

    # make one piece to "eat" the opponent piece
    def eat(self):
        pass

    # show what piece threat on other piece on the board
    def threaten(self):
        pass

    # show if there is a check situation on the board
    def check(self):
        pass
