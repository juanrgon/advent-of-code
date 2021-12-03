TEST = """
199
200
208
210
200
207
240
269
260
263
"""

import sys
from pathlib import Path
from typing import List

# import local AOC lib
sys.path.append(str(Path(__file__).parent.parent.parent))
import aoc


@aoc.tests([(TEST, 7)])
@aoc.parse_text
def part_1(raw: str, ints: List[int], strs: List[str]):
    return sum([int(b > a) for a, b in aoc.mi.windowed(ints, 2, fillvalue=0)])


@aoc.tests([(TEST, 5)])
@aoc.parse_text
def part_2(raw: str, ints: List[int], strs: List[str]):
    return sum(
        [
            int(b > a)
            for a, b in aoc.mi.windowed(
                [sum(triple) for triple in aoc.mi.windowed(ints, 3, fillvalue=0)],
                2,
                fillvalue=0,
            )
        ]
    )


if __name__ == "__main__":
    puzzle = (Path(__file__).parent / "input").read_text().strip()

    part_1.test()
    print("Part 1:", part_1(puzzle))

    part_2.test()
    print("Part 2:", part_2(puzzle))
