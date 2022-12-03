from __future__ import annotations
import string
import aoc
import itertools

# fmt: off
TESTS_1 = [
("""
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
""", 157),
]

TESTS_2 = [
("""
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
""", 70),
]
# fmt: on


@aoc.solution(part=1, tests=TESTS_1)
def part_1(
    raw: aoc.String,
    ints: aoc.Integers,
    strs: list[aoc.String],
    paragraphs: list[aoc.Paragraph],
):
    letters = string.ascii_lowercase + string.ascii_uppercase

    s = 0
    for l in strs:
        first, second = l[:len(l)//2], l[len(l)//2:]
        common = set(first) & set(second)

        for c in common:
            s += letters.index(c) + 1

    return s


@aoc.solution(part=2, tests=TESTS_2)
def part_2(
    raw: aoc.String,
    ints: aoc.Integers,
    strs: list[aoc.String],
    paragraphs: list[aoc.Paragraph],
):
    letters = string.ascii_lowercase + string.ascii_uppercase

    groups = []
    elfs = []
    s = 0

    i = 0
    for l in strs:
        elfs.append(l)

        i += 1
        if i % 3 == 0:
            groups.append(elfs)
            elfs = []
            i = 0

    s = 0
    for group in groups:
        a, b, c =  group
        common = set(a) & set(b) & set(c)
        for c in common:
            s += letters.index(c) + 1

    return s



if __name__ == "__main__":
    print("Part 1:", part_1(__file__))
    print("Part 2:", part_2(__file__))
