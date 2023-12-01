from __future__ import annotations
import aoc


@aoc.solution(1)
def part_1(
    raw: aoc.String,
    ints: aoc.Integers,
    strs: list[aoc.String],
    paragraphs: list[aoc.Paragraph],
):
    nums = []
    for s in strs:
        k = []
        for c in s:
            if c in "0123456789":
                k.append(c)
        s = int("".join([k[0], k[-1]]))
        nums.append(s)

    return sum(nums)


@aoc.solution(2)
def part_2(
    raw: aoc.String,
    ints: aoc.Integers,
    strs: list[aoc.String],
    paragraphs: list[aoc.Paragraph],
):
    nums = []

    numstrs = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "zero",
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
    ]

    nums_to_ints = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "zero": 0,
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
    }

    for s in strs:
        positions = {}

        for n in numstrs:
            print(n, s)
            if n in s:
                print(s)
                for index in get_all_indexes(s, n):
                    print(index, n, s)
                    positions[index] = nums_to_ints[n]

        print(s)
        print(positions)
        first = positions[min(positions.keys())]
        last = positions[max(positions.keys())]
        print((first * 10 + last))
        nums.append(first * 10 + last)

    return sum(nums)


def get_all_indexes(s: str, sub: str):
    indexes = []
    index = -1
    while True:
        index = s.find(sub, index + 1)
        if index == -1:
            break
        indexes.append(index)
    return indexes


if __name__ == "__main__":
    print("Part 1:", part_1(__file__))
    print("Part 2:", part_2(__file__))
