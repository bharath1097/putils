class Position:
    def __init__(self, row=0, col=0):
        self.row = row
        self.col = col

    def __repr__(self):
        return f'Position({self.row!r}, {self.col!r})'

    def __bool__(self):
        return bool(self.row or self.col)

    def __add__(self, other):
        row = self.row + other.row
        col = self.col + other.col
        return Position(row, col)

    def __lt__(self, other):
        return (self.row, self.col) < (other.row, other.col)

    def __eq__(self, other):
        if type(other) is type(self):
            return (self.row, self.col) == (other.row, other.col)
        else:
            return False

    def __hash__(self):
        return hash((self.row, self.col))


class Direction(Position):
    def __init__(self, row=0, col=1):
        super().__init__(row, col)

    def __repr__(self):
        return f'Direction({self.row!r}, {self.col!r})'


North = Direction(-1, 0)
East = Direction(0, 1)
South = Direction(1, 0)
West = Direction(0, -1)
directions = [North, East, South, West]


def turn_right(direction: Direction) -> Direction:
    return directions[(directions.index(direction) + 1) % 4]


def turn_left(direction: Direction) -> Direction:
    return directions[(directions.index(direction) - 1) % 4]
