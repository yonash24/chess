from Piece import Piece
import Board

class Knight(Piece):

    def __init__(self, color, row, col):
        super().__init__(color, row, col)

    # make the piece move
    def move(self,new_row, new_col, board):
        pass


    # show what piece threat on other piece on the board
    def threaten(self,board):
        pass

    # show if there is a check situation on the board
    def check(self,board):
        pass
