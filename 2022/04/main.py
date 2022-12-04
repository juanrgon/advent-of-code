from __future__ import annotations
import aoc

# fmt: off
TESTS_1 = [
("""
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
16-16,4-16
2-6,4-8
2-6,4-8
""", 2),
]

TESTS_2 = [
("""
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
""", 4),
]
# fmt: on


@aoc.solution(part=1, tests=TESTS_1)
def part_1(
    raw: aoc.String,
    ints: aoc.Integers,
    strs: list[aoc.String],
    paragraphs: list[aoc.Paragraph],
):
    s = 0
    for l in strs:
        a, b = l.split(",")

        i, j = a.split("-")
        i, j = int(i), int(j)

        x, y = b.split("-")
        x, y = int(x), int(y)

        if (x <= i <= y and x <= j <= y) or (i <= x <= j and i <= y <= j):
            s += 1

    return s



@aoc.solution(part=2, tests=TESTS_2)
def part_2(
    raw: aoc.String,
    ints: aoc.Integers,
    strs: list[aoc.String],
    paragraphs: list[aoc.Paragraph],
):
    s = 0
    for l in strs:
        a, b = l.split(",")

        i, j = a.split("-")
        i, j = int(i), int(j)

        x, y = b.split("-")
        x, y = int(x), int(y)

        if x <= i <= y or x <= j <= y or i <= x <= j and i <= y <= j:
            s += 1

    return s


if __name__ == "__main__":
    print("Part 1:", part_1(__file__))
    print("Part 2:", part_2(__file__))
