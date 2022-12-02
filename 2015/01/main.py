TEST = [
    ("(())", 0),
    ("()()", 0),
    ("(()(()(", 3),
]

TEST2 = [
    (")", 1),
    ("()())", 5),
]


import aoc


@aoc.submit(part=1)
@aoc.get_input
@aoc.tests(TEST)
@aoc.parse_text
def part_1(raw: str, ints: list[int], strs: list[str], **kwargs):
    f = 0
    for char in raw:
        if char == "(":
            f += 1
        else:
            f -= 1
    return f


@aoc.submit(part=2)
@aoc.get_input
@aoc.tests(TEST2)
@aoc.parse_text
def part_2(raw: str, ints: list[int], strs: list[str], **kwargs):
    f = 0
    for i, char in enumerate(raw):
        if char == "(":
            f += 1
        else:
            f -= 1

        if f == -1:
            return i + 1


if __name__ == "__main__":
    print("Part 1:", part_1(__file__))
    print("Part 2:", part_2(__file__))
