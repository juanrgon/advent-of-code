TEST =[("""
0
3
0
1
-3
""", 5)]

TEST2 =[("""
0
3
0
1
-3
""", 10)]


from typing import List
from collections import Counter

import aoc


@aoc.submit(part=1)
@aoc.get_input
@aoc.tests(TEST)
@aoc.parse_text
def part_1(raw: str, ints: List[int], strs: List[str]):
    position = 0
    steps = 0

    while -1 < position < len(ints):
        jump = ints[position]
        ints[position] += 1
        position += jump
        steps += 1

    return steps


@aoc.submit(part=2)
@aoc.get_input
@aoc.tests(TEST2)
@aoc.parse_text
def part_2(raw: str, ints: List[int], strs: List[str]):
    position = 0
    steps = 0

    while -1 < position < len(ints):
        jump = ints[position]
        ints[position] += 1 if ints[position] < 3 else -1
        position += jump
        steps += 1

    return steps


if __name__ == "__main__":
    print("Part 1:", part_1(__file__))
    print("Part 2:", part_2(__file__))
