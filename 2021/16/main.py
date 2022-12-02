from __future__ import annotations
import aoc
from collections import defaultdict, Counter
from itertools import (
    combinations,
    count,
    permutations,
    combinations_with_replacement,
    product,
    cycle,
    accumulate,
    pairwise,
)
from more_itertools import windowed
import terminology
from functools import cache
import re
import operator
import math


# fmt: off
TESTS_1 = [
("""
D2FE28
""", 6),
("""
38006F45291200
""", 9),
("""
EE00D40C823060
""", 14),
("""
8A004A801A8002F478
""", 16),
("""
620080001611562C8802118E34
""", 12),
("""
C0015000016115A2E0802F182340
""", 23),
("""
A0016C880162017C3686B18A3D4780
""", 31),
]

TESTS_2 = [
    ("38006F45291200", 1),
    ("C200B40A82", 1 + 2),
    ("04005AC33890", 6 * 9),
    ('880086C3E88112', min(7,8,9)),
    ("CE00C43D881120", max(7, 8, 9)),
    ("D8005AC2A8F0", 1),
    ("F600BC2D8F", 0),
    ("9C005AC2F8F0", 0),
    ("9C0141080250320F1802104A08", 1),
]
# fmt: on



@aoc.submit(part=1)
@aoc.get_input
@aoc.tests(TESTS_1)
@aoc.parse_text
def part_1(raw: str, ints: list[int], strs: list[str], **kwargs):
    binary = []
    for d in raw:
        binary.append(bin(int(str(d), 16)).removeprefix("0b").zfill(4))

    bits = "".join(binary)

    return sum([int(v, 2) for v in versions(bits)[0]])


def versions(bits, max_versions=float("inf")) -> tuple[list[str], int]:
    _versions = []

    bits_consumed = 0
    while bits and len(_versions) < max_versions:
        v, bits = bits[:3], bits[3:]
        bits_consumed += 3
        _versions.append(v)
        t, bits = bits[:3], bits[3:]
        bits_consumed += 3

        if t == "100":
            while bits and bits[0] != "0":
                _, bits = bits[:5], bits[5:]
                bits_consumed += 5

            _, bits = bits[:5], bits[5:]
            bits_consumed += 5
        else:
            i, bits = bits[:1], bits[1:]
            bits_consumed += 1
            if i == "0":
                l, bits = bits[:15], bits[15:]
                bits_consumed += 15
                if not bits:
                    continue
                subpacket_bits, bits = (bits[: int(l, 2)], bits[(int(l, 2)) :])
                bits_consumed += int(l, 2)
                _versions.extend(versions(subpacket_bits)[0])
            elif i == "1":
                l, bits = bits[:11], bits[11:]
                bits_consumed += 11
                if not bits:
                    continue
                _subversions, subbits_consumed = versions(bits, max_versions=int(l, 2))
                _versions.extend(_subversions)
                _, bits = bits[:subbits_consumed], bits[subbits_consumed:]
                bits_consumed += subbits_consumed

    return _versions, bits_consumed


def eval(bits: str, max_packets=1) -> tuple[int, int]:
    bits_consumed = 0

    v, bits = bits[:3], bits[3:]
    bits_consumed += len(v)

    t, bits = bits[:3], bits[3:]
    bits_consumed += len(t)

    if t == "100":
        nums = []
        while bits and bits[0] != "0":
            _, num, bits = bits[:1], bits[1:5], bits[5:]
            nums.append(num)
            bits_consumed += len(num) + len(_)

        _, num, bits = bits[:1], bits[1:5], bits[5:]
        nums.append(num)
        bits_consumed += len(num) + len(_)
        return int("".join(nums), 2), bits_consumed

    i, bits = bits[:1], bits[1:]
    bits_consumed += len(i)

    values = []
    if i == "0":
        l, bits = bits[:15], bits[15:]
        bits_consumed += len(l)

        subpacket_bits, bits = (bits[: int(l, 2)], bits[(int(l, 2)) :])
        bits_consumed += int(l, 2)

        subbits_consumed = 0
        while subbits_consumed < int(l, 2):
            result = eval(subpacket_bits)
            values.append(result[0])
            subbits_consumed += result[1]
            subpacket_bits = subpacket_bits[result[1] :]

    elif i == "1":
        l, bits = bits[:11], bits[11:]
        bits_consumed += len(l)

        val_count = int(l, 2)
        subbits_consumed = 0
        for _ in range(val_count):
            result = eval(bits)
            values.append(result[0])
            subbits_consumed += result[1]
            _, bits = bits[:result[1]], bits[result[1]:]

        bits_consumed += subbits_consumed

    def gt(l):
        return int(operator.gt(*l))

    def lt(l):
        return int(operator.lt(*l))

    def eq(l):
        return int(operator.eq(*l))

    op = {
        0: sum,
        1: math.prod,
        2: min,
        3: max,
        5: gt,
        6: lt,
        7: eq,
    }

    return op[int(t, 2)](values), bits_consumed


@aoc.submit(part=2)

@aoc.get_input
@aoc.tests(TESTS_2)
@aoc.parse_text
def part_2(raw: str, ints: list[int], strs: list[str], **kwargs):
    binary = []
    for d in raw:
        binary.append(bin(int(str(d), 16)).removeprefix("0b").zfill(4))

    bits = "".join(binary)

    return eval(bits)[0]


if __name__ == "__main__":
    print("Part 1:", part_1(__file__))
    print("Part 2:", part_2(__file__))
