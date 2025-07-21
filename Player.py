class Player:
    def __init__(self, name):
        """
        :param name: a name for the player from a prompt
        """
        self.name = name
        self.score = 0

    def add_score(self, score):
        """
        :param score: the score to be added onto the current player object
        :return: nothing
        """
        self.score += score

    def get_score(self) -> int:
        """
        :return: the current score value for the player
        """
        return self.score

    def __str__(self):
        """
        :return: string representation of the player
        """
        return str("Player: " + self.name + "\nScore is: " + str(self.get_score()))
