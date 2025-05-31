import pytest
from putils.maze_utils import North, South, East, West, Position, Direction, turn_left, turn_right


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


def test_equality():
    pos1 = Position(3, 4)
    assert pos1 == Position(3, 4)


def test_comparisons():
    pos1, pos2 = Position(3, 4), Position(4, 5)
    assert pos1 < pos2


def test_position_hashable():
    hash(Position(4, 5))


def test_direction_hashable():
    hash(North)
