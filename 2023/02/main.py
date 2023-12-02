from __future__ import annotations
import aoc


@aoc.solution(1)
def part_1(
    raw: aoc.String,
    ints: aoc.Integers,
    strs: list[aoc.String],
    paragraphs: list[aoc.Paragraph],
):
    possible = 0
    for i, game in enumerate(strs):
        name, rounds = game.split(": ")
        id = int(name.split(" ")[1])
        valid = True
        for round in rounds.split("; "):
            for reveal in round.split(", "):
                num, color = reveal.split(" ")
                if (color == "blue") and int(num) > 14:
                    valid = False
                if (color == "green") and int(num) > 13:
                    valid = False
                if (color == "red") and int(num) > 12:
                    valid = False

        if valid:
            possible += id

    return possible


@aoc.solution(2)
def part_2(
    raw: aoc.String,
    ints: aoc.Integers,
    strs: list[aoc.String],
    paragraphs: list[aoc.Paragraph],
):
    power_sum = 0
    for i, game in enumerate(strs):
        _, rounds = game.split(": ")
        max_red = 0
        max_blue = 0
        max_green = 0
        for round in rounds.split("; "):
            for reveal in round.split(", "):
                num, color = reveal.split(" ")

                if (color == "blue"):
                    max_blue = max(max_blue, int(num))

                if (color == "green"):
                    max_green = max(max_green, int(num))

                if (color == "red"):
                    max_red = max(max_red, int(num))

        power_sum += max_red * max_green * max_blue

    return power_sum


if __name__ == "__main__":
    print("Part 1:", part_1(__file__))
    print("Part 2:", part_2(__file__))
