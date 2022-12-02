TEST = [
    (
        """
3,4,1,5
0,1,2,3,4
""",
        12,
    )
]

TEST2 = [
    ("", "a2582a3a0e66e6e86e3812dcb672a272"),
    ("AoC 2017", "33efeb34ea91902bb2f59c9920caa6cd"),
    ("1,2,3", "3efbe78a8d82f29979031a4aa0b16a9d"),
    ("1,2,4", "63960835bcdc130f0b66d7ff4f6a5a8e"),
]

import operator
import functools

import aoc


@aoc.submit(part=1)
@aoc.get_input
@aoc.tests(TEST)
@aoc.parse_text
def part_1(raw: str, ints: list[int], strs: list[str], **kwargs):
    match strs:
        case [lengths, nums]:
            nums = aoc.ints(nums)
        case [lengths]:
            nums = list(range(256))

    lengths = aoc.ints(lengths)

    pos = 0
    skip = 0
    for length in lengths:
        indices = list(range(pos, pos + length))

        temp = []
        for i in indices:
            temp.append(nums[i % len(nums)])

        for i in indices:
            nums[i % len(nums)] = temp.pop()

        pos += (length + skip) % len(nums)
        skip += 1

    return nums[0] * nums[1]


@aoc.submit(part=2)
@aoc.get_input
@aoc.tests(TEST2)
@aoc.parse_text
def part_2(raw: str, ints: list[int], strs: list[str], **kwargs):
    lengths = [ord(l) for l in raw] + [17, 31, 73, 47, 23]

    pos = 0
    skip = 0
    nums = list(range(256))

    for _ in range(64):
        for length in lengths:
            indices = list(range(pos, pos + length))

            temp = []
            for i in indices:
                temp.append(nums[i % len(nums)])

            for i in indices:
                nums[i % len(nums)] = temp.pop()

            pos += (length + skip) % len(nums)
            skip += 1

    sparse_hash = [
        functools.reduce(operator.xor, nums[i * 16 : (i + 1) * 16], 0)
        for i in range(16)
    ]

    return "".join([hex(i).removeprefix("0x").zfill(2) for i in sparse_hash])


if __name__ == "__main__":
    print("Part 1:", part_1(__file__))
    print("Part 2:", part_2(__file__))
