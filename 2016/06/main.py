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
from collections import defaultdict


# fmt: off
TESTS_1 = [
("""
eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar
""", 'easter'),
]

TESTS_2 = [
("""
eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar
""", 'advent'),
]
# fmt: on


@aoc.submit(part=1)
@aoc.get_input
@aoc.tests(TESTS_1)
@aoc.parse_text
def part_1(raw: str, ints: list[int], strs: list[str], **kwargs):
    cols = []
    for i in range(len(strs[0])):
        cols.append([])

    for s in strs:
        for i, c in enumerate(s):
            cols[i].append(c)

    word = ''
    for col in cols:
        word += Counter(col).most_common()[0][0]

    return word


@aoc.submit(part=2)
@aoc.get_input
@aoc.tests(TESTS_2)
@aoc.parse_text
def part_2(raw: str, ints: list[int], strs: list[str], **kwargs):
    cols = []
    for i in range(len(strs[0])):
        cols.append([])

    for s in strs:
        for i, c in enumerate(s):
            cols[i].append(c)

    word = ''
    for col in cols:
        word += Counter(col).most_common()[-1][0]

    return word


if __name__ == "__main__":
    print("Part 1:", part_1(__file__))
    print("Part 2:", part_2(__file__))
