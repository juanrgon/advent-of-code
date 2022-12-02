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
import operator
import math
import sys


# fmt: off
TESTS_1 = [
("""
ULL
RRDDD
LURDL
UUUUD
""", '1985'),
]

TESTS_2 = [
("""
ULL
RRDDD
LURDL
UUUUD
""", "5DB3"),
]
# fmt: on


@aoc.submit(part=1)
@aoc.get_input
@aoc.tests(TESTS_1)
@aoc.parse_text
def part_1(raw: str, ints: list[int], strs: list[str], **kwargs):
    x, y = 1, 1

    nums = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    code = ""

    for line in strs:
        for c in line:
            match c:
                case "U":
                    x -= 1
                    x = max(x, 0)
                case "D":
                    x += 1
                    x = min(x, 2)
                case "L":
                    y -= 1
                    y = max(y, 0)
                case "R":
                    y += 1
                    y = min(y, 2)
        code += f"{nums[x][y]}"

    return code


@aoc.submit(part=2)
@aoc.get_input
@aoc.tests(TESTS_2)
@aoc.parse_text
def part_2(raw: str, ints: list[int], strs: list[str], **kwargs):
    nums = (
        "  1  ",
        " 234 ",
        "56789",
        " ABC ",
        "  D  ",
    )

    y, x = 2, 0
    code = ""

    for line in strs:
        for c in line:
            match c:
                case "U":
                    y -= 1
                    y = max(y, 0)
                    if nums[y][x] == " ":
                        y += 1
                case "D":
                    y += 1
                    y = min(y, 4)
                    if nums[y][x] == " ":
                        y -= 1
                case "L":
                    x -= 1
                    x = max(x, 0)
                    if nums[y][x] == " ":
                        x += 1
                case "R":
                    x += 1
                    x = min(x, 4)
                    if nums[y][x] == " ":
                        x -= 1
        code += f"{nums[y][x]}"

    return code


if __name__ == "__main__":
    print("Part 1:", part_1(__file__))
    print("Part 2:", part_2(__file__))
