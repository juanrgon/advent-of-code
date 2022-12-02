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
A Y
B X
C Z
""", 15),
]

TESTS_2 = [
("""
A Y
B X
C Z
""", 12),
]
# fmt: on


@aoc.submit(part=1)
@aoc.get_input
@aoc.tests(TESTS_1)
@aoc.parse_text
def part_1(
    raw: aoc.String,
    ints: aoc.Integers,
    strs: list[aoc.String],
    paragraphs: list[aoc.Paragraph],
):

    two = {"X": 1, "Y": 2, "Z": 3}
    loses = {"A": "Z", "B": "X", "C": "Y"}
    beats = {"X": "C", "Y": "A", "Z": "B"}

    score = 0
    for round in strs:
        a, b = round.split()

        if beats[b] == a:
            score += two[b] + 6
        elif loses[a] == b:
            score += two[b]
        else:
            score += two[b] + 3

    return score


@aoc.submit(part=2)
@aoc.get_input
@aoc.tests(TESTS_2)
@aoc.parse_text
def part_2(
    raw: aoc.String,
    ints: aoc.Integers,
    strs: list[aoc.String],
    paragraphs: list[aoc.Paragraph],
):

    two = {"X": 1, "Y": 2, "Z": 3}
    loses = {"A": "Z", "B": "X", "C": "Y"}
    beats = {"A": "Y", "B": "Z", "C": "X"}
    ties = {"A": "X", "B": "Y", "C": "Z"}

    score = 0
    for round in strs:
        a, b = round.split()

        if b == "X":
            b = loses[a]
            score += two[b] + 0
        elif b == "Y":
            b = ties[a]
            score += two[b] + 3
        elif b == "Z":
            b = beats[a]
            score += two[b] + 6

    return score


if __name__ == "__main__":
    print("Part 1:", part_1(__file__))
    print("Part 2:", part_2(__file__))
