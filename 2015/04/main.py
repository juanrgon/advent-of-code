TEST = [
    ("abcdef", 609043),
    ("pqrstuv", 1048970),
]

TEST2 = [
    (
        """
""",
        -42,
    ),
]


import aoc
import hashlib
from itertools import count


@aoc.submit(part=1)
@aoc.get_input
@aoc.tests(TEST)
@aoc.parse_text
def part_1(raw: str, ints: list[int], strs: list[str], **kwargs):
    for i in count():
        if hashlib.md5((raw + (str(i))).encode()).hexdigest().startswith('00000'):
            return i

    return 0


@aoc.submit(part=2)
@aoc.get_input
@aoc.parse_text
def part_2(raw: str, ints: list[int], strs: list[str], **kwargs):
    for i in count():
        if hashlib.md5((raw + (str(i))).encode()).hexdigest().startswith('000000'):
            return i


if __name__ == "__main__":
    print("Part 1:", part_1(__file__))
    print("Part 2:", part_2(__file__))
