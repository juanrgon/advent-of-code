from __future__ import annotations
import aoc
from collections import defaultdict, Counter
from itertools import (
    combinations,
    count,
    permutations,
    combinations_with_replacement,
    product,
    cycle,
    accumulate,
)
from more_itertools import windowed
import terminology


# fmt: off
TESTS_1 = [
("""
6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
""", 17),
]

TESTS_2 = [
("""
6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
""", "O"),
]
# fmt: on

@aoc.submit(part=1)
@aoc.get_input
@aoc.tests(TESTS_1)
@aoc.parse_text
def part_1(raw: str, ints: list[int], strs: list[str]):
    points = defaultdict(bool)
    inst, folds = raw.split("\n\n")

    width = 0
    height = 0

    for line in inst.splitlines():
        x, y = aoc.ints(line.split(","))
        points[(x, y)] = True
        width = max(x, width)
        height = max(y, height)

    width = width + 1
    height = height + 1

    for f in folds.splitlines():
        axis, n = f.split()[-1].split("=")
        num = int(n)
        if axis == "y":
            for y in range(num + 1, height):
                for x in range(width):
                    points[(x, 2 * num - y)] |= points[(x, y)]

            height = num

        elif axis == "x":
            for x in range(num + 1, width):
                for y in range(height):
                    points[(2* num - x, y)] |= points[(x, y)]

            width = num

        break

    total = 0
    for y in range(height):
        for x in range(width):
            total += points[(x, y)]
    return total


# @aoc.submit(part=2)
@aoc.get_input
@aoc.tests(TESTS_2)
@aoc.parse_text
def part_2(raw: str, ints: list[int], strs: list[str]):
    points = defaultdict(bool)
    inst, folds = raw.split("\n\n")

    width = 0
    height = 0

    for line in inst.splitlines():
        x, y = line.split(",")
        points[(int(x), int(y))] = True
        width = max(int(x), width)
        height = max(int(y), height)

    width = width + 1
    height = height + 1

    for f in folds.splitlines():
        axis, num = f.split()[-1].split("=")
        num = int(num)
        if axis == "y":
            for y in range(num + 1, height):
                for x in range(width):
                    d = y - num
                    merge = (x, y)
                    dest = (x, num - d)
                    points[dest] |= points[merge]

            height = num

        elif axis == "x":
            for x in range(num + 1, width):
                for y in range(height):
                    d = x - num
                    merge = (x, y)
                    points[(num - d, y)] |= points[merge]

            width = num

    hash_and_dots: list[str] = []

    for y in range(height):
        row = ''
        for x in range(width):
            row += '#' if points[(x, y)] else "."
        hash_and_dots.append(row)

    print('\n'.join(hash_and_dots))
    return "O"

if __name__ == "__main__":
    print("Part 1:", part_1(__file__))
    print("Part 2:", part_2(__file__))
