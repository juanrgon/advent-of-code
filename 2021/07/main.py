TEST = [(
"""
16,1,2,0,4,2,7,1,2,14
""",
    37,
)]

TEST2 = [(
"""
16,1,2,0,4,2,7,1,2,14
""",
    168,
)]

import aoc


@aoc.submit(part=1)
@aoc.get_input
@aoc.tests(TEST)
@aoc.parse_text
def part_1(raw: str, ints: list[int], strs: list[str], **kwargs):
    return min(total_cost(ints, i) for i in range(min(ints), max(ints)))


@aoc.submit(part=2)
@aoc.get_input
@aoc.tests(TEST2)
@aoc.parse_text
def part_2(raw: str, ints: list[int], strs: list[str], **kwargs):
    return min(total_cost_2(ints, i) for i in range(min(ints), max(ints)))


def total_cost(positions, new):
    return sum(abs(p - new) for p in positions)


def total_cost_2(positions, new):
    return sum(cost_2(p, new) for p in positions)


def cost_2(current, new):
    diff = abs(current - new)
    return int((diff * (diff + 1)) / 2)


if __name__ == "__main__":
    print("Part 1:", part_1(__file__))
    print("Part 2:", part_2(__file__))
