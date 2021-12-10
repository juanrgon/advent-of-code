TEST = [
    (
        """
turn on 0,0 through 999,999
toggle 0,0 through 999,0
turn off 499,499 through 500,500
""",
        1_000_000 - 1000 - 4,
    ),
]

TEST2 = [
    (
        """
turn on 0,0 through 0,0
toggle 0,0 through 999,999
""",
        1 + 2_000_000
    ),
]


import aoc
from collections import defaultdict


@aoc.submit(part=1)
@aoc.load_puzzle
@aoc.tests(TEST)
@aoc.parse_text
def part_1(raw: str, ints: list[int], strs: list[str]):

    grid = defaultdict(lambda: defaultdict(bool))

    for line in strs:
        line, b = line.split(" through ")
        inst, a = line.rsplit(" ", 1)

        a_x, a_y = aoc.ints(a.split(","))
        b_x, b_y = aoc.ints(b.split(","))

        match inst:
            case "turn on":
                f = lambda _: True
            case "turn off":
                f = lambda _: False
            case "toggle":
                f = lambda x: not x

        for x in range(a_x, b_x + 1):
            for y in range(a_y, b_y + 1):
                on = f(grid[x][y])
                grid[x][y] = on

    return sum([sum([int(w) for w in v.values()]) for v in grid.values()])


@aoc.submit(part=2)
@aoc.load_puzzle
@aoc.tests(TEST2)
@aoc.parse_text
def part_2(raw: str, ints: list[int], strs: list[str]):
    grid = defaultdict(lambda: defaultdict(int))

    ons = 0
    for line in strs:
        line, b = line.split(" through ")
        inst, a = line.rsplit(" ", 1)

        a_x, a_y = aoc.ints(a.split(","))
        b_x, b_y = aoc.ints(b.split(","))

        match inst:
            case "turn on":
                f = lambda x: x + 1
            case "turn off":
                f = lambda x: max(x - 1, 0)
            case "toggle":
                f = lambda x: x + 2

        for x in range(a_x, b_x + 1):
            for y in range(a_y, b_y + 1):
                on = f(grid[x][y])
                grid[x][y] = on

    return sum([sum([int(w) for w in v.values()]) for v in grid.values()])



if __name__ == "__main__":
    print("Part 1:", part_1(__file__))
    print("Part 2:", part_2(__file__))
