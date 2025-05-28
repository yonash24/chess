from Piece import Piece
import King

class Knight(Piece):

    def __init__(self, color, row, col):
        super().__init__(color, row, col)

    def get_row(self):
        return self.position[0]
    
    def get_col(self):
        return self.position[1]

    def move(self, new_row, new_col, board):
        row_diff = abs(new_row - self.get_row())
        col_diff = abs(new_col - self.get_col())

        if not (0 <= new_row <= 7 and 0 <= new_col <= 7):
            print("invalid move - out of board")
            return

        if (row_diff, col_diff) not in [(2,1), (1,2)]:
            print("invalid move - knight can only move in L-shape")
            return

        target = board.game_board[new_row][new_col]
        if target is None or target.color != self.color:
            self.position = (new_row, new_col)
            board.game_board[new_row][new_col] = self
        else:
            print("invalid move - same color piece")

    def eat(self, new_row, new_col, board):
        row_diff = abs(new_row - self.get_row())
        col_diff = abs(new_col - self.get_col())

        if (row_diff, col_diff) in [(2,1), (1,2)]:
            target = board.game_board[new_row][new_col]
            if target and target.color != self.color:
                self.position = (new_row, new_col)
                board.game_board[new_row][new_col] = self
            else:
                print("invalid capture - no enemy piece")
        else:
            print("invalid capture - invalid knight path")

    def threaten(self, board):
        threats = []
        directions = [
            (2, 1), (1, 2), (-1, 2), (-2, 1),
            (-2, -1), (-1, -2), (1, -2), (2, -1)
        ]
        for dr, dc in directions:
            row = self.get_row() + dr
            col = self.get_col() + dc
            if 0 <= row <= 7 and 0 <= col <= 7:
                threats.append((row, col))
        return threats

    def check(self, board):
        for row, col in self.threaten(board):
            piece = board.game_board[row][col]
            if piece and isinstance(piece, King.King) and piece.color != self.color:
                return True
        return False
