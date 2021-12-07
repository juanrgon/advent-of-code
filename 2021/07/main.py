TEST = (
"""
16,1,2,0,4,2,7,1,2,14
""",
    37,
)

TEST2 = (
"""
16,1,2,0,4,2,7,1,2,14
""",
    168,
)

import aoc


@aoc.tests([TEST])
@aoc.parse_text
def part_1(raw: str, ints: list[int], strs: list[str]):
    return min(total_cost(ints, i) for i in range(min(ints), max(ints)))


@aoc.tests([TEST2])
@aoc.parse_text
def part_2(raw: str, ints: list[int], strs: list[str]):
    return min(total_cost_2(ints, i) for i in range(min(ints), max(ints)))


def total_cost(positions, new):
    return sum(abs(p - new) for p in positions)


def total_cost_2(positions, new):
    return sum(cost_2(p, new) for p in positions)


def cost_2(current, new):
    diff = abs(current - new)
    return int((diff * (diff + 1)) / 2)


if __name__ == "__main__":
    puzzle = aoc.get_puzzle(__file__)

    part_1.test()
    print("Part 1:", part_1(puzzle))

    part_2.test()
    print("Part 2:", part_2(puzzle))
