TEST ="""
0 2 7 0
""", 5

TEST2 ="""
0 2 7 0
""", 4


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
    banks = aoc.ints(strs[0])

    mem = set(' '.join([str(b) for b in banks]))
    steps = 0
    while True:
        s = banks.index(max(banks))

        banks[s], cash = 0, banks[s]
        for i in aoc.it.cycle(range(len(banks))):
            if cash == 0:
                break

            i += (s + 1)
            i = i % len(banks)
            banks[i] += 1
            cash -= 1

        steps += 1

        banks_str = ' '.join([str(b) for b in banks])
        if banks_str in mem:
            return steps
        mem.add(banks_str)



@aoc.tests([TEST2])
@aoc.parse_text
def part_2(raw: str, ints: List[int], strs: List[str]):
    banks = aoc.ints(strs[0])

    mem = set(' '.join([str(b) for b in banks]))
    steps = 0
    seen = ""
    while True:
        s = banks.index(max(banks))

        banks[s], cash = 0, banks[s]
        for i in aoc.it.cycle(range(len(banks))):
            if cash == 0:
                break

            i += (s + 1)
            i = i % len(banks)
            banks[i] += 1
            cash -= 1

        steps += 1

        banks_str = ' '.join([str(b) for b in banks])
        if banks_str in mem:
            if not seen:
                seen = banks_str
                steps = 0
            elif banks_str == seen:
                return steps

        if not seen:
            mem.add(banks_str)


if __name__ == "__main__":
    puzzle = (Path(__file__).parent / "input").read_text().strip()

    part_1.test()

    if not puzzle:
        raise RuntimeError("input puzzle is empty!!")

    print("Part 1:", part_1(puzzle))

    part_2.test()
    print("Part 2:", part_2(puzzle))
