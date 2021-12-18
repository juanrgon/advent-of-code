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
    pairwise
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
""", -42),
]

TESTS_2 = [
("""
""", -42),
]
# fmt: on


@aoc.submit(part=1)
@aoc.get_input
@aoc.tests(TESTS_1)
@aoc.parse_text
def part_1(raw: str, ints: list[int], strs: list[str]):
    return 0


@aoc.submit(part=2)
@aoc.get_input
@aoc.tests(TESTS_2)
@aoc.parse_text
def part_2(raw: str, ints: list[int], strs: list[str]):
    return 0


if __name__ == "__main__":
    print("Part 1:", part_1(__file__))
    print("Part 2:", part_2(__file__))
