import tkinter as tk
import Rook
import Bishop
import King
import Queen
import Pawn
import Knight

class Board:
    
    def __init__(self):
        self.game_board = [
            [Rook("black",0,0),Knight("black",0,1),Bishop("black",0,2),Queen("black",0,3),Knight("black",0,4),Bishop("black",0,5),Knight("black",0,6),Rook("black",0,7)],
            [Pawn("black",1,0),Pawn("black",1,1),Pawn("black",1,2),Pawn("black",1,3),Pawn("black",1,4),Pawn("black",1,5),Pawn("black",1,6),Pawn("black",1,7)],
            [None for _ in range(8)],
            [None for _ in range(8)],
            [None for _ in range(8)],
            [None for _ in range(8)],
            [Rook("white",6,0),Knight("white",6,1),Bishop("white",6,2),Queen("white",6,3),Knight("white",6,4),Bishop("white",6,5),Knight("white",6,6),Rook("white",6,7)],
            [Pawn("white",7,0),Pawn("white",7,1),Pawn("white",7,2),Pawn("white",7,3),Pawn("white",7,4),Pawn("white",7,5),Pawn("white",7,6),Pawn("white",7,7)] 
        ]


    def update_tool_location(self):
        pass
    
    def is_empty(self,row, col, color):
        if self.game_board[row][col] == '-' or self.game_board.color != color:
            return True
        else:
            return False
    
    def get_king_position(self,color):
        for i in range(7):
            for j in range(7):
                if isinstance(self.game_board[i][j],King) and self.game_board[i][j].color != color:
                    return self.game_board[i][j].position
                
    
        
        