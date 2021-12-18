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
    pairwise,
)
from more_itertools import windowed
import terminology
from functools import cache
import re
from pathlib import Path


# fmt: off
TESTS_1 = [
    ("target area: x=20..30, y=-10..-5", 45),
]

TESTS_2 = [
    ("target area: x=20..30, y=-10..-5", 112),
]
# fmt: on


@aoc.submit(part=1)
@aoc.get_input
@aoc.tests(TESTS_1)
@aoc.parse_text
def part_1(raw: str, ints: list[int], strs: list[str]):
    _, _, x_range, y_range = raw.split()
    x0, x1 = aoc.ints(x_range.split("=")[1].strip(",").split(".."))
    y0, y1 = sorted(aoc.ints(y_range.split("=")[1].split("..")))

    highest_y = float("-inf")
    for vx0 in range(1, x1):
        for vy0 in range(-max(abs(y1), abs(y0)), max(abs(y1), abs(y0))):
            t = 1

            y_max = 0
            while x(vx0, t) < x1:
                y_max = max(y(vy0, t), y_max)

                if y0 <= y(vy0, t) <= y1 and x0 <= x(vx0, t) <= x1:
                    highest_y = max(y_max, highest_y)
                    break

                if vx(vx0, t) == 0 and vy(vy0, t) < 0 and y(vy0, t) < y1:
                    break

                t += 1

    return highest_y


@aoc.submit(part=2)
@aoc.get_input
@aoc.tests(TESTS_2)
@aoc.parse_text
def part_2(raw: str, ints: list[int], strs: list[str]):
    _, _, x_range, y_range = raw.split()
    x0, x1 = aoc.ints(x_range.split("=")[1].strip(",").split(".."))
    y0, y1 = sorted(aoc.ints(y_range.split("=")[1].split("..")))

    cords = []

    total = 0
    for vx0 in range(1, x1 + 1):
        for vy0 in range(-max(abs(y1), abs(y0)), max(abs(y1), abs(y0)) + 1):
            t = 1

            y_max = 0
            while x(vx0, t) <= x1:
                y_max = max(y(vy0, t), y_max)

                if y0 <= y(vy0, t) <= y1 and x0 <= x(vx0, t) <= x1:
                    cords.append((vx0, vy0))
                    total += 1
                    break

                if vx(vx0, t) == 0 and vy(vy0, t) < 0 and y(vy0, t) < min(y1, y0):
                    break

                t += 1

    return total


@cache
def y(vy0, t):
    if t == 0:
        return 0
    return y(vy0, t - 1) + vy(vy0, t - 1)


@cache
def x(vx0, t):
    if t == 0:
        return 0
    return x(vx0, t - 1) + vx(vx0, t - 1)


@cache
def vx(vx0, t):
    return max(vx0 - t, 0)


@cache
def vy(vy0, t):
    return vy0 - t


if __name__ == "__main__":
    print("Part 1:", part_1(__file__))
    print("Part 2:", part_2(__file__))
