TEST = [(
    """
b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10
""", 1
)]

TEST2 = [(
"""
b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10
""", 10
)]

import sys
from pathlib import Path
from collections import defaultdict

import aoc


@aoc.submit(part=1)
@aoc.get_input
@aoc.tests(TEST)
@aoc.parse_text
def part_1(raw: str, ints: list[int], strs: list[str]):
    registers: defaultdict[str, int] = defaultdict(int)

    for inst in strs:
        reg1, mod, a1, _, reg2, cond, a2 = inst.split()

        r1 = registers[reg1]
        r2 = registers[reg2]

        if eval(f"{r2} {cond} {int(a2)}"):
            registers[reg1] = r1 + int(a1) if mod == "inc" else r1 - int(a1)

    return max(registers.values())


@aoc.submit(part=2)
@aoc.get_input
@aoc.tests(TEST2)
@aoc.parse_text
def part_2(raw: str, ints: list[int], strs: list[str]):
    highest = 0
    registers: defaultdict[str, int] = defaultdict(int)

    for inst in strs:
        reg1, mod, a1, _, reg2, cond, a2 = inst.split()

        r1 = registers[reg1]
        r2 = registers[reg2]

        if eval(f"{r2} {cond} {int(a2)}"):
            registers[reg1] = r1 + int(a1) if mod == "inc" else r1 - int(a1)
            highest = max(highest, registers[reg1])

    return highest


if __name__ == "__main__":
    print("Part 1:", part_1(__file__))
    print("Part 2:", part_2(__file__))
