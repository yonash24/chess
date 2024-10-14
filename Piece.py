from abc import ABC, abstractmethod
import Board

class Piece(ABC):

    # general constructor
    @abstractmethod
    def __init__(self, color, row, col):
        self.position = (row,col)
        self.color = color

    #make the piece move
    @abstractmethod
    def move(self):
        pass

    #make one piece to "eat" the opponent piece
    @abstractmethod
    def eat(self):
        pass

    #show what piece threat on other piece on the board
    @abstractmethod
    def threaten(self):
        pass

    #show if there is a check situation on the board
    @abstractmethod
    def check(self):
        pass

