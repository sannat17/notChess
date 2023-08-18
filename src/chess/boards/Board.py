from enum import Enum
from typing import Any, Dict, List

# Abstract class fo
class Piece (Enum):
    """ Available pieces for a chess game.
    """
    pass


class Position:
    """ A position (node) on a board. 
    """
    piece: Piece
    edges: Dict # key: edgeType (could be some enum value), value: Position
    edgeTypes: List 
    reference: Any # for example "A1", "B2", "C3" or some other unique identifier

    def __init__(self, edgetypes, reference):
        self.piece = None  # Reference to the piece on this position
        self.edges = None  # Enum of the types of edges this position has
        self.reference = None  # Reference to the position on the board (for example "A1", "B2", "C3")

    def add_piece(self, piece):
        self.piece = piece
    
    def remove_piece(self):
        self.piece = None

    def add_edge(self, position, edgeType):
        self.edges[edgeType] = position
    
    
    # Other methods related to managing a position on the board


class Board:
    """ A graph of different positions on a chess board (a generalized version of a chess board).
    """
    def __init__(self):
        pass
    
    def add_position(self, position):
        # Add a position to the board's dictionary
        raise NotImplementedError
    
    def add_connection(self, position1, position2, edgeType):
        # Add a connection between two positions
        raise NotImplementedError
    
    def get_position(self, position_encoding):
        raise NotImplementedError
    
    def make_move(self, move):
        raise NotImplementedError
    
    def is_valid_move(self, move):
        raise NotImplementedError

    # Other methods for managing positions and connections