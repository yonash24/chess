import  Board

class pawn():

    def __init__(self, color, row, col):
        super().__init__(color, row, col)


    def get_row(self):
        return self.position[0]

    def get_col(self):
        return  self.position[1]
    


    # make the piece move
    def move(self,new_row,new_col, board):
        #if the pawn get to the enemy line
        #turn him into a queen bishop knigt or rook
        if self.color == "white":
            direction = self.get_row +1 
        else:
            direction = self.get_row-1
        
        if board[direction][self.get_col] != '-' or direction > 7 or direction < 0 or new_row > 7 or new_col < 0 or new_row > 7 or new_row < 0 or new_row != direction or new_col != self.get_col+1 or new_col != self.get_col-1:
            print("invalid moove")
        
        if new_row == direction and new_col == self.get_col and board.is_empty(new_row, new_col):
            self.position = (new_row, new_col)
                
        elif new_row == direction and (new_col == self.get_col+1 or new_col == self.get_col-1) and board[new_row][new_col].color != self.color:
            self.position = (new_row, new_col)
          
        else:
            print("invalid moove")
                

    # show what piece threat on other piece on the board
    def threat(self,board):
        if self.color == "white" and (board[self.get_row+1][self.get_col+1] != '-' or board[self.get_row+1][self.get_col-1] != '-'):
            return True
        else:
            return False
        
        if self.color == "black" and (board[self.get_row-1][self.get_col+1] != '-' or board[self.get_row-1][self.get_col-1] != '-'):
            return True
        else:
            return False
        

    # show if there is a check situation on the board
    def check(self,board):
        if self.threat and (type(board[self.get_row+1][self.get_col+1]) == "King" or type(board[self.get_row+1][self.get_col-1]) == "King"):
            return True
        else:
            return False
