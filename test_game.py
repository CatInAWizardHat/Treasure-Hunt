from Player import Player
from Board import Board
import pytest
import random

def test_player():
    p = Player("TestPlayer")

    assert p.name == "TestPlayer"
    assert p.score == 0

    p.add_score(10)
    assert p.get_score() == 10

    assert "Player: TestPlayer\nScore is: 10" == str(p)

def test_board_size_min():
    with pytest.raises(ValueError, match='n must not be less than 2'):
        b = Board(1, 2)


def test_board_size_too_small():
    with pytest.raises(Exception, match='Board size too small for number of treasures'):
        b = Board(3, 4)


def test_pick_oob():
    b = Board(10, 4)
    assert b.pick(11,11) == "Out of bounds of board"
    assert b.pick(0, 0) == "Out of bounds of board"

def test_pick_success_on_empty():
    b = Board(3, 0)
    assert b.pick(1, 1) == "Empty"


@pytest.mark.parametrize('execution_number', range(5))
def test_pick_success_with_value(execution_number):
    random.seed(1)
    b = Board(3, 3)
    assert b.pick(2, 2).isnumeric()

def test_board_print():
    b = Board(3, 0)
    assert "_ _ _ \n_ _ _ \n_ _ _ \n" == str(b)
