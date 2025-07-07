from Piece import Piece
import King

class Rook(Piece):

    def __init__(self, color, row, col):
        super().__init__(color, row, col)

    def get_row(self):
        return self.position[0]
    
    def get_col(self):
        return self.position[1]

    def move(self, new_row, new_col, board):
        if not (0 <= new_row <= 7 and 0 <= new_col <= 7):
            print("invalid move - out of board")
            return

        if new_row != self.get_row() and new_col != self.get_col():
            print("invalid move - rook moves only straight")
            return

        if new_row == self.get_row():
            step = 1 if new_col > self.get_col() else -1
            for col in range(self.get_col() + step, new_col, step):
                if board.game_board[new_row][col] is not None:
                    print("invalid move - path blocked")
                    return
        else:
            step = 1 if new_row > self.get_row() else -1
            for row in range(self.get_row() + step, new_row, step):
                if board.game_board[row][new_col] is not None:
                    print("invalid move - path blocked")
                    return

        target = board.game_board[new_row][new_col]
        if target is None or target.color != self.color:
            self.position = (new_row, new_col)
            board.game_board[new_row][new_col] = self
        else:
            print("invalid move - same color piece")

    def eat(self, new_row, new_col, board):
        if not (0 <= new_row <= 7 and 0 <= new_col <= 7):
            print("invalid capture - out of board")
            return

        if new_row != self.get_row() and new_col != self.get_col():
            print("invalid capture - rook captures only straight")
            return

        if new_row == self.get_row():
            step = 1 if new_col > self.get_col() else -1
            for col in range(self.get_col() + step, new_col, step):
                if board.game_board[new_row][col] is not None:
                    print("invalid capture - path blocked")
                    return
        else:
            step = 1 if new_row > self.get_row() else -1
            for row in range(self.get_row() + step, new_row, step):
                if board.game_board[row][new_col] is not None:
                    print("invalid capture - path blocked")
                    return

        target = board.game_board[new_row][new_col]
        if target and target.color != self.color:
            self.position = (new_row, new_col)
            board.game_board[new_row][new_col] = self
        else:
            print("invalid capture - no enemy piece")

    def threaten(self, board):
        threatened_squares = []
        
        # Vertical up
        for row in range(self.get_row()-1, -1, -1):
            piece = board.game_board[row][self.get_col()]
            if piece is None:
                threatened_squares.append((row, self.get_col()))
            else:
                if piece.color != self.color:
                    threatened_squares.append((row, self.get_col()))
                break

        # Vertical down
        for row in range(self.get_row()+1, 8):
            piece = board.game_board[row][self.get_col()]
            if piece is None:
                threatened_squares.append((row, self.get_col()))
            else:
                if piece.color != self.color:
                    threatened_squares.append((row, self.get_col()))
                break

        # Horizontal right
        for col in range(self.get_col()+1, 8):
            piece = board.game_board[self.get_row()][col]
            if piece is None:
                threatened_squares.append((self.get_row(), col))
            else:
                if piece.color != self.color:
                    threatened_squares.append((self.get_row(), col))
                break

        # Horizontal left
        for col in range(self.get_col()-1, -1, -1):
            piece = board.game_board[self.get_row()][col]
            if piece is None:
                threatened_squares.append((self.get_row(), col))
            else:
                if piece.color != self.color:
                    threatened_squares.append((self.get_row(), col))
                break

        return threatened_squares

    def check(self, board):
        threats = self.threaten(board)
        for row, col in threats:
            piece = board.game_board[row][col]
            if piece and isinstance(piece, King.King) and piece.color != self.color:
                return True
        return False
