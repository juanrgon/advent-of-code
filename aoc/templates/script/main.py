TEST ="""
""", -42

TEST2 = """
""", -42


import aoc


@aoc.tests([TEST])
@aoc.parse_text
def part_1(raw: str, ints: list[int], strs: list[str]):
    return 0


@aoc.tests([TEST2])
@aoc.parse_text
def part_2(raw: str, ints: list[int], strs: list[str]):
    return 0


if __name__ == "__main__":
    puzzle = aoc.get_puzzle(__file__)

    part_1.test()
    print("Part 1:", part_1(puzzle))

    # part_2.test()
    # print("Part 2:", part_2(puzzle))
