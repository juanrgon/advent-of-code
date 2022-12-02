from __future__ import annotations
import aoc

# fmt: off
TESTS_1 = [
("""
""", 8675309),
]

TESTS_2 = [
("""
""", 42),
]
# fmt: on


@aoc.solution(part=1, tests=TESTS_1)
def part_1(
    raw: aoc.String,
    ints: aoc.Integers,
    strs: list[aoc.String],
    paragraphs: list[aoc.Paragraph],
):
    return 0


@aoc.solution(part=2, tests=TESTS_2)
def part_2(
    raw: aoc.String,
    ints: aoc.Integers,
    strs: list[aoc.String],
    paragraphs: list[aoc.Paragraph],
):
    return 0


if __name__ == "__main__":
    print("Part 1:", part_1(__file__))
    print("Part 2:", part_2(__file__))
