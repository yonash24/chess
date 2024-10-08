from abc import ABC, abstractmethod


class Piece(ABC):

    # general constructor
    @abstractmethod
    def __init__(self, name ,value, color):
        self.piece = {name,value}
        self.color = color

    #prevent pieces to move to where they cant
    @abstractmethod
    def cannot_move(self):
        pass

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
