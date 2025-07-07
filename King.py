from Piece import Piece

class King(Piece):

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

        row_diff = abs(new_row - self.get_row())
        col_diff = abs(new_col - self.get_col())

        if max(row_diff, col_diff) > 1:
            print("invalid move - king moves only one square")
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

        row_diff = abs(new_row - self.get_row())
        col_diff = abs(new_col - self.get_col())

        if max(row_diff, col_diff) > 1:
            print("invalid capture - king captures only one square away")
            return

        target = board.game_board[new_row][new_col]
        if target and target.color != self.color:
            self.position = (new_row, new_col)
            board.game_board[new_row][new_col] = self
        else:
            print("invalid capture - no enemy piece")

    def threaten(self, board):
        threatened_squares = []
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                row = self.get_row() + dr
                col = self.get_col() + dc
                if 0 <= row <= 7 and 0 <= col <= 7:
                    threatened_squares.append((row, col))
        return threatened_squares

    def check(self, board):
        threats = self.threaten(board)
        for row, col in threats:
            piece = board.game_board[row][col]
            if piece and isinstance(piece, King) and piece.color != self.color:
                return True
        return False

    def checkmate(self, board):
        """
        Simple placeholder for checkmate logic.
        A proper checkmate check requires scanning all legal king moves
        to see if any escape check.
        """
        if not self.check(board):
            return False

        # Check if any move would escape check
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                row = self.get_row() + dr
                col = self.get_col() + dc
                if 0 <= row <= 7 and 0 <= col <= 7:
                    # simulate move
                    piece = board.game_board[row][col]
                    if piece is None or piece.color != self.color:
                        # Assume king moves there
                        original_pos = self.position
                        temp_piece = board.game_board[row][col]
                        self.position = (row, col)
                        board.game_board[row][col] = self
                        board.game_board[original_pos[0]][original_pos[1]] = None

                        still_in_check = False
                        for i in range(8):
                            for j in range(8):
                                enemy = board.game_board[i][j]
                                if enemy and enemy.color != self.color:
                                    if (row, col) in enemy.threaten(board):
                                        still_in_check = True
                                        break
                            if still_in_check:
                                break

                        # Undo the move
                        self.position = original_pos
                        board.game_board[original_pos[0]][original_pos[1]] = self
                        board.game_board[row][col] = temp_piece

                        if not still_in_check:
                            return False
        return True

    def draw(self, board):
        """
        Placeholder for draw logic.
        A real draw detection involves:
            - insufficient material
            - stalemate
            - repetition
        """
        return False

