TEST = [
(
"""
""",
    -42
),
]

TEST2 = [
(
"""
""",
-42
),
]


import aoc


@aoc.submit(part=1)
@aoc.load_puzzle
@aoc.tests(TEST)
@aoc.parse_text
def part_1(raw: str, ints: list[int], strs: list[str]):
    return 0


@aoc.submit(part=2)
@aoc.load_puzzle
@aoc.tests(TEST2)
@aoc.parse_text
def part_2(raw: str, ints: list[int], strs: list[str]):
    return 0


if __name__ == "__main__":
    print("Part 1:", part_1(__file__))
    print("Part 2:", part_2(__file__))
