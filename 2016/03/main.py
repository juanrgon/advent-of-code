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
 5 10 25
 5 10 24
 5 10 14
 5 10 10
""", 2),
]

TESTS_2 = [
("""
101 301 501
102 302 502
103 303 503
201 401 601
202 402 602
203 403 603
""", 6),
]
# fmt: on


@aoc.submit(part=1)
@aoc.get_input
@aoc.tests(TESTS_1)
@aoc.parse_text
def part_1(raw: str, ints: list[int], strs: list[str], **kwargs):
    c = 0
    for l in strs:
        nums = [int(x.strip()) for x in l.split()]
        smaller = sorted(nums)[:2]
        if sum(smaller) > max(nums):
            c += 1
        else:
            pass
    return c


@aoc.submit(part=2)
@aoc.get_input
@aoc.tests(TESTS_2)
@aoc.parse_text
def part_2(raw: str, ints: list[int], strs: list[str], **kwargs):
    triangles = []
    a, b, c = [], [], []
    for i, num in enumerate(ints):
        match i % 3:
            case 0:
                a.append(num)
                if len(a) == 3:
                    triangles.append(a)
                    a = []
            case 1:
                b.append(num)
                if len(b) == 3:
                    triangles.append(b)
                    b = []
            case 2:
                c.append(num)
                if len(c) == 3:
                    triangles.append(c)
                    c = []

    x = 0
    for nums in triangles:
        smaller = sorted(nums)[:2]
        if sum(smaller) > max(nums):
            x += 1
        else:
            pass

    return x


if __name__ == "__main__":
    print("Part 1:", part_1(__file__))
    print("Part 2:", part_2(__file__))
