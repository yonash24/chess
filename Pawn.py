from Piece import Piece
import King
import Queen
import Rook
import Bishop
import Knight

class Pawn(Piece):

    def __init__(self, color, row, col):
        super().__init__(color, row, col)

    def get_row(self):
        return self.position[0]
    
    def get_col(self):
        return self.position[1]

    def move(self, new_row, new_col, board):
        direction = -1 if self.color == "white" else 1
        start_row = 6 if self.color == "white" else 1

        if new_col == self.get_col():
            if new_row == self.get_row() + direction and board.is_empty(new_row, new_col, self.color):
                self.position = (new_row, new_col)
                self.promote_if_ready(board)
            elif self.get_row() == start_row and new_row == self.get_row() + 2 * direction:
                intermediate_row = self.get_row() + direction
                if board.is_empty(intermediate_row, new_col, self.color) and board.is_empty(new_row, new_col, self.color):
                    self.position = (new_row, new_col)
                    self.promote_if_ready(board)
            else:
                print("invalid move")
        else:
            print("invalid move")

    def eat(self, new_row, new_col, board):
        direction = -1 if self.color == "white" else 1
        if abs(new_col - self.get_col()) == 1 and new_row == self.get_row() + direction:
            target = board.game_board[new_row][new_col]
            if target and target.color != self.color:
                self.position = (new_row, new_col)
                self.promote_if_ready(board)
            else:
                print("invalid capture")
        else:
            print("invalid capture")

    def threaten(self, board):
        direction = -1 if self.color == "white" else 1
        threats = []
        for col_offset in [-1, 1]:
            row = self.get_row() + direction
            col = self.get_col() + col_offset
            if 0 <= row <= 7 and 0 <= col <= 7:
                threats.append((row, col))
        return threats

    def check(self, board):
        threats = self.threaten(board)
        for row, col in threats:
            piece = board.game_board[row][col]
            if piece and isinstance(piece, King.King) and piece.color != self.color:
                return True
        return False

    def promote_if_ready(self, board):
        final_row = 0 if self.color == "white" else 7
        row, col = self.position
        if row == final_row:
            choice = input(f"Promote {self.color} pawn at ({row},{col}) to (Q, R, B, N): ").strip().upper()
            if choice == "Q":
                board.game_board[row][col] = Queen.Queen(self.color, row, col)
            elif choice == "R":
                board.game_board[row][col] = Rook.Rook(self.color, row, col)
            elif choice == "B":
                board.game_board[row][col] = Bishop.Bishop(self.color, row, col)
            elif choice == "N":
                board.game_board[row][col] = Knight.Knight(self.color, row, col)
            else:
                print("Invalid choice. Promoting to Queen by default.")
                board.game_board[row][col] = Queen.Queen(self.color, row, col)
