TEST = (
    """
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
""",
    198,
)

TEST2 = (
    """
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
""",
    230,
)


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

    bit_counts = defaultdict(lambda: {"0": 0, "1": 1})

    for line in strs:
        for i, bit in enumerate(line):
            bit_counts[i][bit] += 1

    gr = ""
    er = ""
    for counts in bit_counts.values():
        gr += "1" if counts["1"] > counts["0"] else "0"
        er += "1" if counts["1"] < counts["0"] else "0"

    return int(gr, 2) * int(er, 2)


@aoc.tests([TEST2])
@aoc.parse_text
def part_2(raw: str, ints: List[int], strs: List[str]):
    oxy = strs
    co2 = strs

    for bit in range(len(strs[0])):
        o = defaultdict(list)
        c = defaultdict(list)

        for n in oxy:
            o[n[bit]].append(n)

        for n in co2:
            c[n[bit]].append(n)

        if len(oxy) > 1:
            oxy = o["1"] if len(o["1"]) >= len(o["0"]) else o["0"]

        if len(co2) > 1:
            co2 = c["0"] if len(c["1"]) >= len(c["0"]) else c["1"]

    return int(oxy[0], 2) * int(co2[0], 2)


if __name__ == "__main__":
    puzzle = aoc.get_puzzle(__file__)

    part_1.test()
    print("Part 1:", part_1(puzzle))

    part_2.test()
    print("Part 2:", part_2(puzzle))
