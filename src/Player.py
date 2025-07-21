from dataclasses import dataclass


@dataclass
class Player:
    name: str
    score: int = 0

    def add_score(self, score: int) -> None:
        """
        :param score: the score to be added onto the current player object
        :return: nothing
        """
        self.score += score

    def __str__(self) -> str:
        """
        :return: string representation of the player
        """
        return str(f"Player: {self.name}\nScore is: {self.score}")
