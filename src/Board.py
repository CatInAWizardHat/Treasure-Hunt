import random


class Board:
    """
    Takes 2 parameters
    n = Number of rows & columns (Board is N x N)
    t = Number of treasures
    if n < t, the board is too small to house the number of treasures
    else, initializes a multi-dimensional array containing underscores.
    """

    def __init__(self, n, t):
        try:
            self.n = n
            self.t = t
            if n < 2:
                raise ValueError("n must not be less than 2")
            if n < t:
                raise Exception("Board size too small for number of treasures")
        except ValueError as details:
            raise ValueError(details) from details
        except Exception as details:
            raise Exception(details) from details
        else:
            self.board = [["_" for _ in range(self.n)] for _ in range(self.n)]
            self.populate_board()

    def pick(self, row, col) -> str:
        """
        Picks a row and column passed in from user input.
        returns "Empty" if value within board[row][col] is an underscore,
        else returns the value.
        """
        try:
            row -= 1
            col -= 1
            if row >= self.n or col >= self.n:
                raise Exception("Out of bounds of board")
            elif row < 0 or col < 0:
                raise Exception("Out of bounds of board")
        except Exception as details:
            return str(details)
        else:
            value = self.board[row][col]
            self.board[row][col] = " "
            if "_" == value:
                return "Empty"
            else:
                return value

    def populate_board(self) -> None:
        """
        Populates the board by choosing a random starting location,
        then iterating over the row or column based
        the value from random.choice().

        if True, the treasure is seeded up -> down
        else the treasure is seeded left -> right

        if the index of the treasure would exceed the bounds of the array
        uses modulo operator to wrap back to the nth index
        """
        all_coords = [(r, c) for r in range(self.n) for c in range(self.n)]
        random.shuffle(all_coords)

        starting_coords = [all_coords.pop() for _ in range(self.t)]

        for i in range(1, self.t + 1):
            row, col = starting_coords[i - 1]
            vertical_direction = random.choice([True, False])

            if vertical_direction:
                for j in range(i):
                    self.board[(row + j) % self.n][col] = str(i)
            else:
                for j in range(i):
                    self.board[row][(col + j) % self.n] = str(i)

    def __str__(self) -> str:
        """
        Creates a string representation of the board to be returned
        Iterates over self.board[][]
        Concatenates a space and the value within each index
        Every self.n indexes, concatenates a newline character.
        :return: a string representation of the current board.
        """
        return "\n".join(" ".join(row) for row in self.board) + "\n"
