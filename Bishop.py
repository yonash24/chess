from Piece import Piece
import King
import Board


class Bishop(Piece):

    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        
    def get_row(self):
        return self.position[0]
    
    def get_col(self):
        return self.position[1]

    # make the piece move
    def move(self, new_row, new_col, board):    
                   
        #check the cases of invalid mooves
        row_dif = abs(new_row- self.get_row())
        col_dif = abs(new_col-self.get_col())
        if row_dif != col_dif or new_row > 7 or new_row < 0 or new_col > 7 or new_col < 0:
            print("invalide moove")
            return
        
        
        row_step = 1 if new_row > row else -1
        col_step = 1 if new_col > col else -1
        
        row = self.get_row() + row_step
        col = self.get_col() + col_step
        
        #check that the path to the new position is clean
        while row != new_row and col != new_col:
            if not board.is_empty(row,col,self.color):
               print("invalide moove")
               return
            else:   
               row += row_step
               col += col_step 
               
        if board.is_empty(new_row,new_col,self.color):
            self.position = (new_row,new_col)    
                


    # show what piece threat on other piece on the board
    def threaten(self,board):
    
        directions = [(1,1), (1,-1), (-1,1), (-1,-1)]
        
        for row_step, col_step in directions:
            row = self.get_row + row_step
            col = self.get_col + col_step
            while 0 <= row <= 7 or 0 <= col <= 7:
                if board[row][col] != '-':
                    if board[row][col].color != self.color:
                        return True
                    else:
                        return False 
                row += row_step
                col += col_step

    # show if there is a check situation on the board
    def check(self,board):
               
        directions = [(1,1), (1,-1), (-1,1), (-1,-1)]
        
        for row_step, col_step in directions:
            row = self.get_row + row_step
            col = self.get_col + col_step
            
            while 0 <= row <= 7 or 0 <= col <= 7: 
                if board[row][col] != '-' and isinstance(board[row][col],King) and board[row][col].color != self.color:
                    return True    
                row += row_step
                col += col_step
        
        return False
                    
                
                
        