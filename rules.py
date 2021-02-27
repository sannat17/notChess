from __future__ import annotations

class Piece:
  """
  Represents a piece in a game
  """
  def __init__(self, start_pos):
    # Alternatively we can store each piece in the boards
    # 2D array which would equivalently define it's position
    # which player the piece belongs to
    self.pos = start_pos

class GameFrame:
  # A snapshot of a game position 
    # storing which pieces exist
  # Store a pgn version of the current position (a string)
  # stores which players turn it is



# Abstract
class RuleSet:
  # stores an initial state, which is an instance of a gameframe
  # 

  def is_game_over(game_frame: GameFrame) -> bool:
    """
    Given the current game_frame, returns whether the game is over (True) or not (False).

    Alternatively: Returns what type of "game over" it is...
    eg) stalemate, checkmate, draw [repetition,agreement,etc...] assuming standard chess 
    rules.
    """
    raise NotImplementedError

  def encode_gameframe(instance: GameFrame) -> str:
    """
    Given the current <instance> (a GameFrame), convert it in an easy to store format (string for now).
    """
    raise NotImplementedError
  
  def decode_gameframe(encoded_gf: str) -> GameFrame:
    """
    Given the string version of a GameFrame, generate a GameFrame instance.
    """
    raise NotImplementedError
    
class Game:
  """
  contains a ruleset, tree of GameFrames, players part of the game
  tracks turns - figure out which player's turn it is
  takes players input an
  """
  while game is not over:
    # save the space efficient version of the frame to the history
    # after each move we will update the positions of the pieces
    get current players input
    generate a new gameframe based on that input
    

    