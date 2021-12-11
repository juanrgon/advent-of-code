from __future__ import annotations
import textwrap
import attr
from typing import TypeVar, Callable, ParamSpec, Generic
import terminology


P = ParamSpec("P")
T = TypeVar("T")


class Grid(list[list[T]]):
    @classmethod
    def from_str(cls, s: str, init: Callable[[str], T] = int, delimiter="") -> Grid[T]:
        grid: list[list[T]] = cls()

        for line in s.splitlines():
            grid.append(
                [init(e) for e in (line.split(delimiter) if delimiter else line)]
            )

        return grid

    @classmethod
    def of_zeroes(cls, height: int, width: int) -> Grid[int]:
        grid: list[list[int]] = cls()

        for _ in range(height):
            grid.append([0 for _ in range(width)])

        return grid

    @classmethod
    def of(cls, init: Callable[[], T], *, height: int, width: int) -> Grid[T]:
        grid: list[list[T]] = cls()

        for _ in range(height):
            grid.append([init() for _ in range(width)])

        return grid

    def height(self):
        return len(self)

    def width(self):
        return len(self[0]) if self else 0

    def subgrid(self, start: tuple[int, int], end: tuple[int, int]) -> Grid[T]:
        (row_0, col_0), (row_1, col_1) = start, end
        return type(self)([row[col_0 : col_1 + 1] for row in self[row_0 : row_1 + 1]])

    def for_each(self, f):
        for v in self.values():
            f(v)

    def values(self) -> list[T]:
        v = []

        for row in self:
            v.extend(row)

        return v

    def items(self) -> list[tuple[tuple[int, int], T]]:
        l = []

        for x, row in enumerate(self):
            for y , el in enumerate(row):
                l.append(((x, y), el))

        return l

    def neighbors(self, point: tuple[int, int]) -> dict[tuple[int, int], T]:
        x, y = point

        n = {}

        for row in range(x - 1, x + 2):
            for col in range(y - 1, y + 2):
                if row < 0 or col < 0:
                    continue

                if row >= self.height() or col >= self.width():
                    continue

                if (row, col) == point:
                    continue

                n[row, col] = self[row][col]

        return n

    def __str__(self):
        x = ""
        for row in self:
            x += " ".join([str(cell) for cell in row])
            x += "\n"
        return x

    def __repr__(self):
        x = []
        for row in self:
            x.append(" ".join([repr(cell) for cell in row]))
        return "\n".join(x)

    def __getitem__(self, i):
        if isinstance(i, tuple):
            x, y = i
            return super().__getitem__(x)[y]
        return super().__getitem__(i)


if __name__ == "__main__":
    # Tests

    x = textwrap.dedent(
        """\
            5483143223
            2745854711
            5264556173
            6141336146
            6357385478
            4167524645
            2176841721
            6882881134
            4846848554
            5283751526
        """
    )

    # ------ Grid.from_str() -----------
    @attr.define
    class Light:
        brightness: int = 0

        @classmethod
        def from_str(cls, s: str) -> Light:
            return cls(brightness=int(s))

        def on(self) -> bool:
            return self.brightness >= 5

        def __str__(self):
            return (
                terminology.in_green(self.brightness)
                if self.on()
                else str(self.brightness)
            )

        def __repr__(self):
            return f"*{self.brightness}*" if self.on() else str(self.brightness)

    lights = Grid.from_str(x, init=Light.from_str)
    print(str(lights))

    # ------ Grid.of() --------
    zeroes = Grid.of(int, width=4, height=3)
    print(zeroes)
    assert zeroes.width() == 4
    assert zeroes.height() == 3

    lights = Grid.of(Light, width=5, height=3)
    print(lights)

    # ---- Grid[x][y] ------
    nums = Grid.from_str("\n".join(["012345", "67891"]))
    assert nums[1][0] == 6

    # ------ Grid.subgrid() --------
    lights = Grid.from_str(x, init=Light.from_str)
    print(lights.subgrid((2, 3), (7, 8)))

    # ------ Grid.neighbors() --------
    letters = Grid.from_str(
        textwrap.dedent(
            """\
            ABCDE
            FGHIJ
            KLMNO
            """
        ),
        init=str,
    )
    assert letters[1][1] == "G"
    assert letters[1, 1] == "G"
    assert letters.neighbors((1, 1)) == {
        (0, 0): "A",
        (0, 1): "B",
        (0, 2): "C",
        (1, 0): "F",
        (1, 2): "H",
        (2, 0): "K",
        (2, 1): "L",
        (2, 2): "M",
    }

    assert letters.neighbors((0, 0)) == {
        (0, 1): "B",
        (1, 0): "F",
        (1, 1): "G",
    }

    assert letters.neighbors((0, 4)) == {
        (0, 3): "D",
        (1, 3): "I",
        (1, 4): "J",
    }
