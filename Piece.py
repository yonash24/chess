from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, color, row, col):
        self.color = color  # "white" or "black"
        self.position = (row, col)

    def get_row(self):
        return self.position[0]

    def get_col(self):
        return self.position[1]

    @abstractmethod
    def move(self, new_row, new_col, board):
        """Move the piece to a new location if valid"""
        pass

    @abstractmethod
    def eat(self, new_row, new_col, board):
        """Capture an opponent piece if valid"""
        pass

    @abstractmethod
    def threaten(self, board):
        """Return a list of positions this piece threatens"""
        pass

    @abstractmethod
    def check(self, board):
        """Return True if this piece checks the opponent king"""
        pass
