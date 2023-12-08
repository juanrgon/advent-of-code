import aoc
from pprint import pprint
from itertools import cycle
import math


@aoc.solution(1)
def part_1(
    raw: aoc.String,
    ints: aoc.Integers,
    strs: list[aoc.String],
    paragraphs: list[aoc.Paragraph],
):
    start_moves_str, network_str = raw.split("\n\n")

    start_moves = list(start_moves_str)

    # network[AAA][L] = BBB
    # network[AAA][R] = CCC
    # network[BBB][L] = DDD
    # network[BBB][R] = EEE
    # ...
    network = {}
    for i, line in enumerate(network_str.splitlines()):
        key, lr_str = line.split(" = ")
        lr_str = lr_str.strip("()")
        l, r = lr_str.split(", ")
        network.setdefault(key, {})
        network[key].setdefault("L", l)
        network[key].setdefault("R", r)

    key = "AAA"
    for i, move in enumerate(cycle(start_moves)):
        key = network[key][move]

        if key == "ZZZ":
            break

    return i + 1


@aoc.solution(2)
def part_2(
    raw: aoc.String,
    ints: aoc.Integers,
    strs: list[aoc.String],
    paragraphs: list[aoc.Paragraph],
):
    start_moves_str, network_str = raw.split("\n\n")

    start_moves = list(start_moves_str)

    # network[AAA][L] = BBB
    # network[AAA][R] = CCC
    # network[BBB][L] = DDD
    # network[BBB][R] = EEE
    # ...
    network = {}
    for i, line in enumerate(network_str.splitlines()):
        # if i == 0:
        #     start_key = line.split(" = ")[0]
        key, lr_str = line.split(" = ")
        lr_str = lr_str.strip("()")
        l, r = lr_str.split(", ")
        network.setdefault(key, {})
        network[key].setdefault("L", l)
        network[key].setdefault("R", r)

    a_keys = [k for k in network.keys() if k.endswith("A")]

    moves_to_z = []
    for key in a_keys:
        for i, move in enumerate(cycle(start_moves)):
            key = network[key][move]

            if key.endswith("Z"):
                moves_to_z.append(i + 1)
                break

    # return the least common multiple of all the moves to Z
    return math.lcm(*moves_to_z)


if __name__ == "__main__":
    print("Part 1:", part_1(__file__))
    print("Part 2:", part_2(__file__))
