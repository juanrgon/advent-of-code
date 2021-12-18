TEST = [
(
"""
123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i
g -> a
""",
    114
),
]

TEST2 = [
(
"""
""",
-42
),
]


import aoc
from collections import defaultdict


# @aoc.submit(part=1)
@aoc.get_input
@aoc.tests(TEST)
@aoc.parse_text
def part_1(raw: str, ints: list[int], strs: list[str]):
    wires: defaultdict[str, int] = defaultdict(int)

    for line in strs:
        line = line.replace('as', "_as")
        line = line.replace('if', "_if")
        line = line.replace('in', "_in")
        line = line.replace('is', "_is")

        cmd, wire = line.split(' -> ')
        cmd = cmd.replace(" AND ", ' & ')
        cmd = cmd.replace(" OR ", ' | ')
        cmd = cmd.replace(" LSHIFT ", ' << ')
        cmd = cmd.replace(" RSHIFT ", ' >> ')
        cmd = cmd.replace("NOT", '~')

        wires[wire] = eval(cmd, wires)

    return wires['a'] % 65536 if wires['a'] == 0 else wires['a']


@aoc.submit(part=2)
@aoc.get_input
@aoc.tests(TEST2)
@aoc.parse_text
def part_2(raw: str, ints: list[int], strs: list[str]):
    return 0


if __name__ == "__main__":
    print("Part 1:", part_1(__file__))
    print("Part 2:", part_2(__file__))
