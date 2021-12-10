TEST = [
    (1122, 3),
    (1111, 4),
    (1234, 0),
    (91212129, 9),
]

TEST2 = [
    (1212, 6),
    (1221, 0),
    (123425, 4),
    (123123, 12),
    (12131415, 4),
]

from pathlib import Path

import aoc


@aoc.submit(part=1)
@aoc.get_input
@aoc.tests(TEST)
@aoc.parse_text
def part_1(raw: str, ints: list[int], strs: list[str]):
    total = 0
    digits = [int(s) for s in raw]
    for i, d in enumerate(digits):
        if d == digits[(i + 1) % len(digits)]:
            total += d
    return total


@aoc.submit(part=2)
@aoc.get_input
@aoc.tests(TEST2)
@aoc.parse_text
def part_2(raw: str, ints: list[int], strs: list[str]):
    x = 0
    digits = [int(s) for s in raw]
    for i, d in enumerate(digits):
        if d == digits[int(i + len(digits) / 2) % len(digits)]:
            x += digits[i]
    return x


if __name__ == "__main__":
    print("Part 1:", part_1(__file__))
    print("Part 2:", part_2(__file__))
