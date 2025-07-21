from Board import Board
from Player import Player
from typing import List


class Game:
    def __init__(self, board: Board) -> None:
        self.players: List[Player] = []
        self.board: Board = board
