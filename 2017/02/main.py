TEST = (
    """
5 1 9 5
7 5 3
2 4 6 8
""",
    18,
)

TEST2 = (
    """
5 9 2 8
9 4 7 3
3 8 6 5
""",
    9,
)

import sys
from pathlib import Path
from typing import List

# import local AOC lib
sys.path.append(str(Path(__file__).parent.parent.parent))
import aoc


@aoc.tests([TEST])
@aoc.parse_text
def part_1(raw: str, ints: List[int], strs: List[str]):
    chk = 0
    for l in strs:
        nums = aoc.ints(l)
        chk += max(nums) - min(nums)
    return chk


@aoc.tests([TEST2])
@aoc.parse_text
def part_2(raw: str, ints: List[int], strs: List[str]):
    s = 0

    for line in strs:
        nums = aoc.ints(line)
        for a, b in aoc.it.combinations(nums, 2):
            a , b =  (a, b) if a > b else (b , a)
            s += int(a / b) if a % b == 0 else 0

    return s


if __name__ == "__main__":
    puzzle = (Path(__file__).parent / "input").read_text().strip()

    part_1.test()
    print("Part 1:", part_1(puzzle))

    part_2.test()
    print("Part 2:", part_2(puzzle))
