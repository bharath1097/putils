import pytest
from putils.maze_utils import *


@pytest.mark.parametrize("current_direction, new_direction",
                         [(North, East), (East, South), (South, West)])
def test_turn_right(current_direction: Direction, new_direction: Direction):
    next_direction = turn_right(current_direction)
    assert next_direction == new_direction


@pytest.mark.parametrize("current_direction, new_direction",
                         [(North, West), (West, South), (South, East)])
def test_turn_left(current_direction: Direction, new_direction: Direction):
    next_direction = turn_left(current_direction)
    assert next_direction == new_direction
