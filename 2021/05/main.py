TEST = (
    """
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
""",
    5,
)

TEST2 = (
"""
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
""",
    12,
)

import attr
from collections import defaultdict

# import local AOC lib
import aoc


@attr.define(frozen=True)
class Point:
    x: int
    y: int


@attr.define
class Vent:
    points: list[Point]

    @classmethod
    def from_string(cls, s: str, with_diagonals=False) -> "Vent":
        points = []
        start, end = s.split(" -> ")
        x0, y0 = [int(s) for s in start.split(",")]
        x1, y1 = [int(s) for s in end.split(",")]

        if x0 > x1:
            (x0, y0), (x1, y1) = (x1, y1), (x0, y0)

        if x0 == x1:
            y0, y1 = min(y0, y1), max(y0, y1)
            points = [Point(x0, y) for y in range(y0, y1 + 1)]
        elif y0 == y1:
            x0, x1 = min(x0, x1), max(x0, x1)
            points = [Point(x, y0) for x in range(x0, x1 + 1)]
        elif with_diagonals:
            y = y0
            for i, x in enumerate(range(x0, x1 + 1)):
                points.append(Point(x, y))
                y += 1 if y0 < y1 else -1

        return cls(points=points)


@attr.define
class Grid:
    hits: dict[Point, int]
    width: int
    height: int

    @classmethod
    def from_vents(cls, vents: list[Vent]) -> "Grid":
        hits: defaultdict[Point, int] = defaultdict(int)
        max_x = 0
        max_y = 0

        for vent in vents:
            for point in vent.points:
                max_x = max(max_x, point.x)
                max_y = max(max_y, point.y)
                hits[point] += 1

        return cls(hits=hits, width=max_x, height=max_y)

    def display(self):
        for y in range(self.height + 1):
            cells = []
            for x in range(self.width + 1):
                print(self.hits[Point(x, y)] or ".", "", end="")
            print()


@aoc.tests([TEST])
@aoc.parse_text
def part_1(raw: str, ints: list[int], strs: list[str]):
    vents = []
    for line in strs:
        vents.append(Vent.from_string(line))
    grid = Grid.from_vents(vents)
    return len([times for times in grid.hits.values() if times > 1])


@aoc.tests([TEST2])
@aoc.parse_text
def part_2(raw: str, ints: list[int], strs: list[str]):
    vents = []
    for line in strs:
        vents.append(Vent.from_string(line, with_diagonals=True))
    grid = Grid.from_vents(vents)
    return len([times for times in grid.hits.values() if times > 1])


if __name__ == "__main__":
    puzzle = aoc.get_puzzle(__file__)

    part_1.test()
    print("Part 1:", part_1(puzzle))

    part_2.test()
    print("Part 2:", part_2(puzzle))
