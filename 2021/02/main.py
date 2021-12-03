TEST = """
forward 5
down 5
forward 8
up 3
down 8
forward 2
""", 150

TEST2 = """
forward 5
down 5
forward 8
up 3
down 8
forward 2
""", 900


import sys
from pathlib import Path
from typing import List

# import local AOC lib
sys.path.append(str(Path(__file__).parent.parent.parent))
import aoc


@aoc.tests([TEST])
@aoc.parse_text
def part_1(raw: str, ints: List[int], strs: List[str]):
    x, y = 0, 0

    for line in strs:
        d, a = line.split()
        a = int(a)

        if d.startswith('f'):
            x += a
        elif d.startswith('d'):
            y -= a
        elif d.startswith('u'):
            y += a

    return abs(y * x)


@aoc.tests([TEST2])
@aoc.parse_text
def part_2(raw: str, ints: List[int], strs: List[str]):
    x, y, aim = 0, 0, 0

    for line in strs:
        d, a = line.split()
        a = int(a)

        if d.startswith('f'):
            x += a
            y += aim * a
        elif d.startswith('d'):
            aim += a
        elif d.startswith('u'):
            aim -= a

    return abs(y * x)

if __name__ == "__main__":
    puzzle = (Path(__file__).parent / "input").read_text().strip()

    part_1.test()
    print("Part 1:", part_1(puzzle))

    part_2.test()
    print("Part 2:", part_2(puzzle))
