import tkinter as tk
from xml.sax import parse

from reportlab.lib.colors import white

from Bishop import Bishop
from King import King
from Knight import Knight
from Pawn import Pawn
from Queen import Queen
from Rook import Rook

BOARD_SIZE = 8  #define the size of the board
CELL_SIZE = 60  #define the size of each cell
COLORS = ["#DDB88C", "#A66D4F"] #define the colors of the board game black and white


# Initial board setup
initial_board = [
    [Rook('black',0,0), Knight('black',0,1), Bishop('black',0,2), Queen('black',0,4), King('king',0,5), Bishop('black',0,5), Knight('black',0,6), Rook('black',0,7)],  # Row 1 (White pieces)
    [Pawn('black',1,0), Pawn('black',1,1), Pawn('black',1,2), Pawn('black',1,3), Pawn('black',1,4), Pawn('black',1,5), Pawn('black',1,6), Pawn('black',1,7)],  # Row 2 (White pawns)
    ['.', '.', '.', '.', '.', '.', '.', '.'],  # Row 3 (Empty)
    ['.', '.', '.', '.', '.', '.', '.', '.'],  # Row 4 (Empty)
    ['.', '.', '.', '.', '.', '.', '.', '.'],  # Row 5 (Empty)
    ['.', '.', '.', '.', '.', '.', '.', '.'],  # Row 6 (Empty)
    [Pawn('white',6,0), Pawn('white',6,1), Pawn('white',6,2), Pawn('white',6,3),  Pawn('white',6,4), Pawn('white',6,5), Pawn('white',6,6), Pawn('white',6,7)],  # Row 7 (Black pawns)
    [Rook('white',7,0), Knight('white',7,1), Bishop('white',7,2), Queen('white',7,3), Knight('white',7,4), Bishop('white',7,5), Knight('white',7,6), Rook('white',7,7)],  # Row 8 (Black pieces)
]

class Board:

    # constructore
    def __init__(self, root):
        self.root = root    # stores the main Tkinter window object
        self.board = initial_board  # the 2d array we defined earlier that hold the stat of the board
        self.selected_piece = None  # stores the coordinate of the selected piece
        self.current_turn = 'whit'  # track of how turn is it, white start first
        self.create_board()  #call the method create_board to create and display the chess board
        self.wturn = True
        self.bturn = False


    # method that create the chess board
    def create_board(self):
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                color = COLORS[(row+col)%2]     # will later determine the color of each button
                piece = self.board[row][col]    # the coordinate of each square on the 2d board


                # create button for each square
                button = tk.Button(
                    self.root,
                    text = PIECES.get(piece, ''),   #display the chess piece if presented
                    font = ('HELVETICA', 24),   #   set the font size
                    bg = color,  #sets the background color
                    width=4, height=2,  #set the heigth and width of each button
                    command=lambda r = row, c = col: self.on_square_click(r,c)  #lambda function call the method on_square_click each time when button clicked
                )
                button.grid(row=row, column=col)
                button.piece = piece    #store the piece on the button
                button.row = row
                button.col = col

    def on_square_click(self, row, col):
        piece = self.board[row][col]

        # select a piece to move
        if self.selected_piece is None and piece != '.':
            if(self.current_turn == 'white' and piece.color == 'white') or \
              (self.current_turn == 'black' and piece.color == 'black'):
                self.selected_piece = (row,col)
                print(f"selected piece at {row},{col}")
        else:
            if self.selected_piece:
                start_row, start_col = self.selected_piece
                self.board[start_row][start_col] = '.'
                self.board[row][col] = piece
                self.update_board()
                self.selected_piece = None
                self.current_turn =  'black' if self.current_turn == 'white' else 'white'



    def update_board(self):
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                piece = self.board[row][col]
                button = self.root.grid_slaves(row=row, column=col)[0]
                button.config(text=PIECES.get(piece,''))


# set up the main loop
root = tk.Tk()
root.title("chess game")    #call the board chess game
game = Board(root)  #initalize the Board class with root
root.mainloop() #start the main loop (event loop)
