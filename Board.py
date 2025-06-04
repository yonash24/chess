import Rook
import Bishop
import King
import Queen
import Pawn
import Knight

class Board:

    def __init__(self):
        self.game_board = [[None for _ in range(8)] for _ in range(8)]

        # Setup Black Pieces
        self.game_board[0] = [
            Rook.Rook("black", 0, 0),
            Knight.Knight("black", 0, 1),
            Bishop.Bishop("black", 0, 2),
            Queen.Queen("black", 0, 3),
            King.King("black", 0, 4),
            Bishop.Bishop("black", 0, 5),
            Knight.Knight("black", 0, 6),
            Rook.Rook("black", 0, 7)
        ]
        for col in range(8):
            self.game_board[1][col] = Pawn.Pawn("black", 1, col)

        # Setup White Pieces
        self.game_board[7] = [
            Rook.Rook("white", 7, 0),
            Knight.Knight("white", 7, 1),
            Bishop.Bishop("white", 7, 2),
            Queen.Queen("white", 7, 3),
            King.King("white", 7, 4),
            Bishop.Bishop("white", 7, 5),
            Knight.Knight("white", 7, 6),
            Rook.Rook("white", 7, 7)
        ]
        for col in range(8):
            self.game_board[6][col] = Pawn.Pawn("white", 6, col)

    def is_empty(self, row, col, color=None):
        piece = self.game_board[row][col]
        if piece is None:
            return True
        if color is not None and piece.color == color:
            return False
        return False

    def get_king_position(self, color):
        for i in range(8):
            for j in range(8):
                piece = self.game_board[i][j]
                if piece and isinstance(piece, King.King) and piece.color == color:
                    return (i, j)
        return None

    def print_board(self):
        for row in self.game_board:
            row_str = ""
            for piece in row:
                if piece is None:
                    row_str += "- "
                else:
                    symbol = type(piece).__name__[0]
                    symbol = symbol.upper() if piece.color == "white" else symbol.lower()
                    row_str += symbol + " "
            print(row_str)
        print()

    def move_piece(self, start_row, start_col, end_row, end_col):
        piece = self.game_board[start_row][start_col]
        if piece is None:
            print("No piece at source.")
            return

        if piece.color != self.turn:
            print(f"It's {self.turn}'s turn.")
            return

        # Try to move or eat
        target = self.game_board[end_row][end_col]
        if target is None:
            piece.move(end_row, end_col, self)
        else:
            piece.eat(end_row, end_col, self)

        # Update board reference
        self.game_board[start_row][start_col] = None
        self.game_board[end_row][end_col] = piece

    def get_piece(self, row, col):
        return self.game_board[row][col]
