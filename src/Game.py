from Board import Board
from Player import Player
from typing import List

PLAYER_NAMES = ["One", "Two"]
MAX_PLAYERS = 2


class Game:
    def __init__(self, board: Board = Board(10, 4)) -> None:
        self.players: List[Player] = []
        self.board: Board = board
        self.cnx: int = 0

    def get_player(self) -> Player:
        return self.players[self.cnx]

    def add_player(self) -> None:
        if self.cnx == MAX_PLAYERS:
            return

        new_player = Player(PLAYER_NAMES[self.cnx])
        self.cnx += 1
        self.players.append(new_player)
