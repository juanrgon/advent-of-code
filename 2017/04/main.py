TEST = (
    """
    aa bb cc dd ee
    aa bb cc dd aa
    aa bb cc dd aaa
    """,
    2,
)

TEST2 = (
    """
abcde fghij
abcde xyz ecdab
a ab abc abd abf abj
iiii oiii ooii oooi oooo
oiii ioii iioi iiio
""",
    3,
)


import sys
from pathlib import Path
from typing import List
from collections import Counter

# import local AOC lib
sys.path.append(str(Path(__file__).parent.parent.parent))
import aoc


@aoc.submit(part=1)
@aoc.get_input
@aoc.tests(TEST)
@aoc.parse_text
def part_1(raw: str, ints: List[int], strs: List[str], **kwargs):
    return len([p for p in strs if len(set(p.split())) == len(p.split())])


@aoc.submit(part=2)
@aoc.get_input
@aoc.tests(TEST2)
@aoc.parse_text
def part_2(raw: str, ints: List[int], strs: List[str], **kwargs):
    _s = []
    for p in strs:
        _s.append(" ".join([''.join(sorted(w)) for w in p.split()]))

    return len([p for p in _s if len(set(p.split())) == len(p.split())])


if __name__ == "__main__":
    print("Part 1:", part_1(__file__))
    print("Part 2:", part_2(__file__))
