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
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
""", 24000),
]

TESTS_2 = [
("""
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
""", 45000),
]
# fmt: on


@aoc.submit(part=1)
@aoc.get_input
@aoc.tests(TESTS_1)
@aoc.parse_text
def part_1(raw: aoc.String, ints: aoc.Integers, strs: list[aoc.String], paragraphs: list[aoc.Paragraph]) -> int:
    return max(p.ints.sum for p in paragraphs)

@aoc.submit(part=2)
@aoc.get_input
@aoc.tests(TESTS_2)
@aoc.parse_text
def part_2(raw: aoc.String, ints: aoc.Integers, strs: list[aoc.String], paragraphs: list[aoc.Paragraph]):
    return sum(sorted([p.ints.sum for p in paragraphs], reverse=True)[:3])


if __name__ == "__main__":
    print("Part 1:", part_1(__file__))
    print("Part 2:", part_2(__file__))
