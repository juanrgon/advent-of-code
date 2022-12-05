from __future__ import annotations
import aoc
from collections import defaultdict



@aoc.solution(1)
def part_1(
    raw: aoc.String,
    ints: aoc.Integers,
    strs: list[aoc.String],
    paragraphs: list[aoc.Paragraph],
):
    stacks = []

    for l in raw.splitlines():
        if l.startswith('-'):
            break

        for i, c in enumerate(l):

            if i >= len(stacks):
                stacks.append([])
            if c == ' ':
                continue
            stacks[i].append(c)

    for k in raw.splitlines():
        if k.startswith("move"):
            _, amt, _, src, _, dest = k.split()
            for _ in range(int(amt)):
                stacks[int(dest) - 1].insert(0, stacks[int(src) - 1].pop(0))

    return ''.join([s[0] for s in stacks])



@aoc.solution(2)
def part_2(
    raw: aoc.String,
    ints: aoc.Integers,
    strs: list[aoc.String],
    paragraphs: list[aoc.Paragraph],
):
    stacks = []

    for l in raw.splitlines():
        if l.startswith('-'):
            break

        for i, c in enumerate(l):

            if i >= len(stacks):
                stacks.append([])
            if c == ' ':
                continue
            stacks[i].append(c)

    for k in raw.splitlines():
        if k.startswith("move"):
            _, amt, _, src, _, dest = k.split()

            x = []
            for _ in range(int(amt)):
                x.insert(0, stacks[int(src) - 1].pop(0))

            for v in x:
                stacks[int(dest) - 1].insert(0, v)

    return ''.join([s[0] for s in stacks])


if __name__ == "__main__":
    print("Part 1:", part_1(__file__))
    print("Part 2:", part_2(__file__))
