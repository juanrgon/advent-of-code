from __future__ import annotations
import aoc


@aoc.solution(1)
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
        i, j = i.as_int, j.as_int

        x, y = b.split("-")
        x, y = x.as_int, y.as_int

        if (x <= i <= y and x <= j <= y) or (i <= x <= j and i <= y <= j):
            s += 1

    return s


@aoc.solution(2)
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
        i, j = i.as_int, j.as_int

        x, y = b.split("-")
        x, y = x.as_int, y.as_int

        if x <= i <= y or x <= j <= y or i <= x <= j and i <= y <= j:
            s += 1

    return s


if __name__ == "__main__":
    print("Part 1:", part_1(__file__))
    print("Part 2:", part_2(__file__))
