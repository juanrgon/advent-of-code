TEST ="""
0
3
0
1
-3
""", 5

TEST2 ="""
0
3
0
1
-3
""", 10


import sys
from pathlib import Path
from typing import List
from collections import Counter

# import local AOC lib
sys.path.append(str(Path(__file__).parent.parent.parent))
import aoc


@aoc.tests([TEST])
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


@aoc.tests([TEST2])
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
    puzzle = (Path(__file__).parent / "input").read_text().strip()

    part_1.test()
    print("Part 1:", part_1(puzzle))

    part_2.test()
    print("Part 2:", part_2(puzzle))
