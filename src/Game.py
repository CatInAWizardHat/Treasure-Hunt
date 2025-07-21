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

    def get_player(self, id: int) -> Player:
        if id < 0 or id >= MAX_PLAYERS:
            raise ValueError("Invalid ID")
        else:
            return self.players[id]

    def add_player(self) -> None:
        if self.cnx == MAX_PLAYERS:
            return

        new_player = Player(PLAYER_NAMES[self.cnx])
        self.cnx += 1
        self.players.append(new_player)

    def handle_pick(self, player, row, col):
        if row < 1 or row > self.board.n:
            raise ValueError(
                f"Invalid row selection, must be between 1 and {self.board.n}"
            )
        elif col < 1 or row > self.board.n:
            raise ValueError(
                f"Invalid column selection, must be between 1 and {self.board.n}"
            )
        else:
            value = self.board.pick(row, col)
            if value.isnumeric():
                player.add_score(int(value))
                return player.score
