TEST = [
    (
        """
ugknbfddgicrmopn
aaa
jchzalrnumimnmhp
haegwjzuvuyypxyu
dvszwmarrgswjxmb
""",
        1 + 1,
    ),
]

TEST2 = [
    (
        """
qjhvhtzxzqqjkmpb
xxyxx
uurcxstgmygtbstg
ieodomkazucvgmuy
""",
        1 + 1,
    ),
]


import aoc
from collections import Counter
from itertools import product
import string


@aoc.submit(part=1)
@aoc.load_puzzle
@aoc.tests(TEST)
@aoc.parse_text
def part_1(raw: str, ints: list[int], strs: list[str]):
    vowels = "aeiou"

    nice = 0

    for s in strs:
        if sum(Counter(s)[v] for v in vowels) < 3:
            continue

        for l in string.ascii_lowercase:
            if l + l in s:
                break
        else:
            continue

        if "ab" in s or "cd" in s or "pq" in s or "xy" in s:
            continue

        nice += 1

    return nice


@aoc.submit(part=2)
@aoc.load_puzzle
@aoc.tests(TEST2)
@aoc.parse_text
def part_2(raw: str, ints: list[int], strs: list[str]):
    vowels = "aeiou"

    nice = 0

    for s in strs:
        for l, k in product(string.ascii_lowercase, repeat=2):
            t = s.replace(l + k, "")
            if len(s) - len(t) >= 4:
                break
        else:
            continue

        for l, k in product(string.ascii_lowercase, repeat=2):
            if l + k + l in s:
                break
        else:
            continue

        nice += 1

    return nice


if __name__ == "__main__":
    print("Part 1:", part_1(__file__))
    print("Part 2:", part_2(__file__))
