TEST = [
    (
        """
199
200
208
210
200
207
240
269
260
263
""",
        7,
    )
]

TEST2 = [
    (
        """
199
200
208
210
200
207
240
269
260
263
""",
        5,
    )
]

from more_itertools import windowed

import aoc


@aoc.submit(part=1)
@aoc.get_input
@aoc.tests(TEST)
@aoc.parse_text
def part_1(raw: str, ints: list[int], strs: list[str]):
    return sum([int(b > a) for a, b in windowed(ints, 2, fillvalue=0)])


@aoc.submit(part=1)
@aoc.get_input
@aoc.tests(TEST2)
@aoc.parse_text
def part_2(raw: str, ints: list[int], strs: list[str]):
    return sum(
        [
            int(b > a)
            for a, b in windowed(
                [sum(triple) for triple in windowed(ints, 3, fillvalue=0)],
                2,
                fillvalue=0,
            )
        ]
    )


if __name__ == "__main__":
    print("Part 1:", part_1(__file__))
    print("Part 2:", part_2(__file__))
