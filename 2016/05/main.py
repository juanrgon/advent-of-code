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
import hashlib



# fmt: off
TESTS_1 = [
("""
abc
""", "18f47a30"),
]

TESTS_2 = [
("""
abc
""", "05ace8e3"),
]
# fmt: on


@aoc.submit(part=1)
@aoc.get_input
@aoc.tests(TESTS_1)
@aoc.parse_text
def part_1(raw: str, ints: list[int], strs: list[str]):
    door_id = raw
    password = ''
    for i in count():
        hash = hashlib.md5((door_id + str(i)).encode()).hexdigest()
        if hash.startswith('00000'):
            password += hash[5]
            if len(password) == 8:
                return password


@aoc.submit(part=2)
@aoc.get_input
@aoc.tests(TESTS_2)
@aoc.parse_text
def part_2(raw: str, ints: list[int], strs: list[str]):
    door_id = raw
    found = 0
    password = ['_'] * 8
    for i in count():
        hash = hashlib.md5((door_id + str(i)).encode()).hexdigest()
        if hash.startswith('00000'):

            if not hash[5].isdigit():
                continue

            pos = int(hash[5])

            if pos > 7:
                continue

            if password[pos] != '_':
                continue

            password[pos] = hash[6]
            found += 1
            if found == 8:
                return "".join(password)


if __name__ == "__main__":
    # print("Part 1:", part_1(__file__))
    print("Part 2:", part_2(__file__))
