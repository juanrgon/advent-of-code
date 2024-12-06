import aoc
import re


@aoc.solution(1)
def part_1(
    raw: aoc.String,
    ints: aoc.Integers,
    strs: list[aoc.String],
    paragraphs: list[aoc.Paragraph],
):
    regex = r"mul\(\d+,\d+\)"
    inner_regex = r"\d+"
    total = 0

    for line in raw.splitlines():
        for match in re.findall(regex, line):
            x, y = re.findall(inner_regex, match)
            total += int(x) * int(y)

    return total


@aoc.solution(2)
def part_2(
    raw: aoc.String,
    ints: aoc.Integers,
    strs: list[aoc.String],
    paragraphs: list[aoc.Paragraph],
):
    regex = r"mul\(\d+,\d+\)|don't\(\)|do\(\)"
    inner_regex = r"\d+"
    total = 0

    enabled = True
    for line in raw.splitlines():
        for match in re.findall(regex, line):
            if match == "don't()":
                enabled = False
            elif match == "do()":
                enabled = True
            else:
                if enabled:
                    x, y = re.findall(inner_regex, match)
                    total += int(x) * int(y)

    return total


if __name__ == "__main__":
    print("Part 1:", part_1(__file__))
    print("Part 2:", part_2(__file__))
