import pytest

from pig import Human

def test_human():
    my_human = Human()
    assert my_human.score == 0
    # assert my_human.turn == 0
    # assert my_human.die == 
    # assert human.choice == 