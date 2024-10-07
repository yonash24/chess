import tkinter as tk

from numpy import roots

#creating the main window
window = tk.Tk()
window.title("ChessBoard")


BOARD_SIZE = 8  #define the size of the board
CELL_SIZE = 60  #define the size of each cell
COLORS = ["#DDB88C", "#A66D4F"] #define the colors of the board game black and white

# uniocode symbol for chess pieces
 # W-for whit B-for black and first letter of each chess piece
PIECES = {'WR': '\u2656', 'WN':'\u2658', 'WB':'\u2657', 'WQ':'\u2655', 'WK':'\u2654','WP':'\u2659',
              'BR': '\u265C', 'BN':'\u265E', 'BB':'\u265D', 'BQ':'\u265B', 'BK':'\u265A','BP':'\u265F'}

# Initial board setup
initial_board = [
    ['WR', 'WN', 'WB', 'WQ', 'WK', 'WB', 'WN', 'WR'],  # Row 1 (White pieces)
    ['WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP'],  # Row 2 (White pawns)
    ['.', '.', '.', '.', '.', '.', '.', '.'],  # Row 3 (Empty)
    ['.', '.', '.', '.', '.', '.', '.', '.'],  # Row 4 (Empty)
    ['.', '.', '.', '.', '.', '.', '.', '.'],  # Row 5 (Empty)
    ['.', '.', '.', '.', '.', '.', '.', '.'],  # Row 6 (Empty)
    ['BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP'],  # Row 7 (Black pawns)
    ['BR', 'BN', 'BB', 'BQ', 'BK', 'BB', 'BN', 'BR'],  # Row 8 (Black pieces)
]

class Board:

    # constructore
    def __init__(self, root):
        self.root = root    # stores the main Tkinter window object
        self.board = initial_board  # the 2d array we defined earlier that hold the stat of the board
        self.selected_piece = None  # stores the coordinate of the selected piece
        self.current_turn = 'whit'  # track of how turn is it, white start first
        self.create_board()  #call the method create_board to create and display the chess board

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
            if(self.current_turn == 'white' and piece[0] == 'W') or \
              (self.current_turn == 'black' and piece[0] == 'B'):
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
