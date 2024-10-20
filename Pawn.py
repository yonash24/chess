from Bishop import Bishop
from Board import Board
from Knight import Knight
from Piece import Piece
from Queen import Queen
from Rook import Rook


class Pawn(Piece,Queen,Knight,Bishop,Rook):

    symbol = '\u2659' if Piece.__name__ == 'WP' else '\u265F'

    def __init__(self, color, row, col):
        super.__init__(color, row, col)


    def get_row(self):
        return self.position.row

    def get_col(self):
        return  self.position.col

    # make the piece move
    def move(self):

        #if the pawn get to the enemy line
        #turn him into a queen bishop knigt or rook
        if self.position.row == 7 or self.position.row == 0:
            upgrade_pawn = input("choose what to turn your pawn to: queen/rook/bishop/knight")
            upgrade_pawn.lower()
            if upgrade_pawn == 'queen':
                pass
        elif self.threat() == True:
            self.eat()
        else:
            self.position.row += 1


    # make one piece to "eat" the opponent piece
    def eat(self):
        if  self.threat() == True:
            self.position.row += 1
            self.position.col += 1


    # show what piece threat on other piece on the board
    def threat(self):
        if self.color == "white":
            if self.board[][] != None or (self.get_row+1, self.get_col-1) != None:
                return True
            else:
                return False
        else:
            if (self.get_row-1, self.get_col+1) != None or (self.get_row-1, self.get_col+1) != None:
                return True
            else:
                return False

    # show if there is a check situation on the board
    def check(self):
        pass
