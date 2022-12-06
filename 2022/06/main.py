from __future__ import annotations
import aoc


@aoc.solution(1)
def part_1(
    raw: aoc.String,
    ints: aoc.Integers,
    strs: list[aoc.String],
    paragraphs: list[aoc.Paragraph],
):
    diff = []
    for i, c in enumerate(raw):
        if c in diff:
            i = diff.index(c)
            diff = diff[i+1:]

        diff.append(c)

        if len(diff) == 4:
            return i + 1



@aoc.solution(2)
def part_2(
    raw: aoc.String,
    ints: aoc.Integers,
    strs: list[aoc.String],
    paragraphs: list[aoc.Paragraph],
):
    diff = []
    for i, c in enumerate(raw):
        if c in diff:
            i = diff.index(c)
            diff = diff[i+1:]

        diff.append(c)

        if len(diff) == 14:
            return i + 1


if __name__ == "__main__":
    print("Part 1:", part_1(__file__))
    print("Part 2:", part_2(__file__))
