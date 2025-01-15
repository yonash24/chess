from Piece import Piece
import Board

class Rook(Piece):

    def __init__(self, color, row, col):
        super().__init__(color,row,col)

    def get_row(self):
        return self.position[0]
    
    def get_col(self):
        return self.position[1]

    # make the piece move
    def move(self, new_row, new_col, board):
        
        if (new_row != self.get_row() and new_col != self.get_col()) or new_row > 7 or new_row < 0 or new_col > 7 or new_col < 0:
            print("invalid moove")
            return
        if new_row == self.get_row():
            step = 1 if new_col > self.get_col() else -1
            for i in range(self.get_col()+step,new_col,step):
                if not board.is_empty(self.get_row(),i,self.color):
                    print("invalide moove")
                    return
        elif new_col == self.get_col():
            step = 1 if new_row > self.get_row() else -1
            for i in  range(self.get_row()+step,new_row,step):
                if not board.is_empty(i,self.get_col(),self.color):
                    print("invalide moove")
                    return
        self.position = (new_row,new_col)
        

    # show what piece threat on other piece on the board
    def threaten(self,board):
        for i in range(self.get_row(),7,1):
            if not board.is_empty(i,self.get_col(),self.color):
                return True
        for i in range(self.get_row(),0,-1):
            if not board.is_empty(i,self.get_col(),self.color):
                return True
        for i in range(self.get_col(),7,1):
            if not board.is_empty(self.get_row(),i,self.color):
                return True
        for i in range(self.get_col(),0,-1):
            if not board.is_empty(self.get_row(),i,self.color):
                return True
        return False
    
    # show if there is a check situation on the board
    def check(self,board):
        opponenmt_king = board.get_king_position(self.color)
        return opponenmt_king in self.threaten(board)
