from ..boards.Board import Board

# Abstract class for a ruleset
class Ruleset:
    """_summary_
    """
    board: Board
    def __init__(self):
        # Make a new board in implementation of abstract class
        self.board: Board = None
        self.winner = None

    def is_game_over(self, gameframe):
        raise NotImplementedError
    
    def encode_gameframe(self, gameframe):
        raise NotImplementedError
    
    def decode_gameframe(self, encoded_gameframe):
        raise NotImplementedError
    
    def encode_game(self):
        raise NotImplementedError
    
    def decode_game(self, encoded_game):
        raise NotImplementedError
    
    def get_next_gameframe(self, gameframe, move):
        raise NotImplementedError
    
    def get_valid_moves(self, gameframe):
        raise NotImplementedError
    
