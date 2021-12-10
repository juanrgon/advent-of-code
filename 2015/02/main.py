TEST = [
    (
        """
2x3x4
1x1x10
""",
        58 + 43,
    )
]

TEST2 = [
    (
        """
2x3x4
1x1x10
""",
        48,
    )
]


import aoc


@aoc.submit(part=1)
@aoc.get_input
@aoc.tests(TEST)
@aoc.parse_text
def part_1(raw: str, ints: list[int], strs: list[str]):
    t = 0

    for l in strs:
        l, w, h = aoc.ints(l)
        a = l * w
        b = w * h
        c = h * l

        t += 2 * a + 2 * b + 2 * c + min(a, b, c)

    return t


@aoc.submit(part=2)
@aoc.get_input
@aoc.tests(TEST2)
@aoc.parse_text
def part_2(raw: str, ints: list[int], strs: list[str]):
    t = 0

    for line in strs:
        l, w, h = aoc.ints(line)
        x, y = sorted(aoc.ints(line))[:2]

        a = 2 * x + 2 * y
        b = l * w * h
        t += a + b

    return t


if __name__ == "__main__":
    print("Part 1:", part_1(__file__))
    print("Part 2:", part_2(__file__))
