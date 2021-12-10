TEST = (("3,4,3,1,2", 5934),)

TEST2 = (("3,4,3,1,2", 26984457539),)

import sys
from pathlib import Path
from functools import cache

import aoc


@aoc.submit(part=1)
@aoc.get_input
@aoc.tests(TEST)
@aoc.parse_text
def part_1(raw: str, ints: list[int], strs: list[str]):
    return sum(total_fish(fish, days=80) for fish in ints)


@aoc.submit(part=2)
@aoc.get_input
@aoc.tests(TEST2)
@aoc.parse_text
def part_2(raw: str, ints: list[int], strs: list[str]):
    return sum(total_fish(fish, days=256) for fish in ints)


@cache
def total_fish(timer: int, days: int) -> int:
    if days == 0:
        return 1

    if timer == 0:
        return total_fish(6, days=days - 1) + total_fish(8, days=days - 1)

    return total_fish(timer - 1, days=days - 1)


if __name__ == "__main__":
    print("Part 1:", part_1(__file__))
    print("Part 2:", part_2(__file__))
