from typing import NamedTuple


class Position(NamedTuple):
    row: int
    col: int

    def __bool__(self):
        return bool(self.row or self.col)

    def __add__(self, other):
        row = self.row + other.row
        col = self.col + other.col
        return Position(row, col)


class Direction(Position):
    pass


North = Direction(-1, 0)
East = Direction(0, 1)
South = Direction(1, 0)
West = Direction(0, -1)
directions = [North, East, South, West]


def turn_right(direction: Direction) -> Direction:
    return directions[(directions.index(direction) + 1) % 4]


def turn_left(direction: Direction) -> Direction:
    return directions[(directions.index(direction) - 1) % 4]
