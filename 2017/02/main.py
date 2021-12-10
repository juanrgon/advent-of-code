TEST = [(
    """
5 1 9 5
7 5 3
2 4 6 8
""",
    18,
)]

TEST2 = [(
    """
5 9 2 8
9 4 7 3
3 8 6 5
""",
    9,
)]

from typing import List
import itertools

import aoc


@aoc.submit(part=1)
@aoc.get_input
@aoc.tests(TEST)
@aoc.parse_text
def part_1(raw: str, ints: List[int], strs: List[str]):
    chk = 0
    for l in strs:
        nums = aoc.ints(l)
        chk += max(nums) - min(nums)
    return chk


@aoc.submit(part=2)
@aoc.get_input
@aoc.tests(TEST2)
@aoc.parse_text
def part_2(raw: str, ints: List[int], strs: List[str]):
    s = 0

    for line in strs:
        nums = aoc.ints(line)
        for a, b in itertools.combinations(nums, 2):
            a , b =  (a, b) if a > b else (b , a)
            s += int(a / b) if a % b == 0 else 0

    return s


if __name__ == "__main__":
    print("Part 1:", part_1(__file__))
    print("Part 2:", part_2(__file__))
