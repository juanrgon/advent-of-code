TEST = [
    (
        """
forward 5
down 5
forward 8
up 3
down 8
forward 2
""",
        150,
    )
]

TEST2 = [
    (
        """
forward 5
down 5
forward 8
up 3
down 8
forward 2
""",
        900,
    )
]


from pathlib import Path

import aoc


@aoc.submit(part=1)
@aoc.get_input
@aoc.tests(TEST)
@aoc.parse_text
def part_1(raw: str, ints: list[int], strs: list[str], **kwargs):
    x, y = 0, 0

    for line in strs:
        d, a = line.split()
        a = int(a)

        if d.startswith("f"):
            x += a
        elif d.startswith("d"):
            y -= a
        elif d.startswith("u"):
            y += a

    return abs(y * x)


@aoc.submit(part=2)
@aoc.get_input
@aoc.tests(TEST2)
@aoc.parse_text
def part_2(raw: str, ints: list[int], strs: list[str], **kwargs):
    x, y, aim = 0, 0, 0

    for line in strs:
        d, a = line.split()
        a = int(a)

        if d.startswith("f"):
            x += a
            y += aim * a
        elif d.startswith("d"):
            aim += a
        elif d.startswith("u"):
            aim -= a

    return abs(y * x)


if __name__ == "__main__":
    print("Part 1:", part_1(__file__))
    print("Part 2:", part_2(__file__))
