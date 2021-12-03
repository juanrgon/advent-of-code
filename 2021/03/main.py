TEST ="""
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
""", 198

TEST2 ="""
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
""", 230


import sys
from pathlib import Path
from typing import List, Match
from collections import defaultdict, Counter
import math

# import local AOC lib
sys.path.append(str(Path(__file__).parent.parent.parent))
import aoc


@aoc.tests([TEST])
@aoc.parse_text
def part_1(raw: str, ints: List[int], strs: List[str]):
    return 0

@aoc.tests([TEST2])
@aoc.parse_text
def part_2(raw: str, ints: List[int], strs: List[str]):
    return 0


if __name__ == "__main__":
    puzzle = (Path(__file__).parent / "input").read_text().strip()

    part_1.test()
    print("Part 1:", part_1(puzzle))

    part_2.test()
    print("Part 2:", part_2(puzzle))
