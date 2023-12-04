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
    score = 0

    for _, line in enumerate(strs):
        left, right = line.split(" | ")
        _, winner_str = left.strip().split(": ")
        winners = winner_str.strip().split(" ")
        mine = right.strip().split(" ")

        match = 0
        for n in mine:
            if n and n in winners:
                match += 1

        if match > 0:
            score += 2 ** (match - 1)

    return score


@aoc.solution(2)
def part_2(
    raw: aoc.String,
    ints: aoc.Integers,
    strs: list[aoc.String],
    paragraphs: list[aoc.Paragraph],
):
    scratchcard_counts = defaultdict(lambda: 1)

    for card_num, line in enumerate(strs):
        left, right = line.split(" | ")
        _, winner_str = left.strip().split(": ")
        winners = winner_str.strip().split(" ")
        mine = right.strip().split(" ")

        match = 0
        for n in mine:
            if n and n in winners:
                match += 1

        base_count = scratchcard_counts[card_num]
        for i in range(match):
            scratchcard_counts[card_num + i + 1] += base_count

    return sum(scratchcard_counts.values())


if __name__ == "__main__":
    print("Part 1:", part_1(__file__))
    print("Part 2:", part_2(__file__))
