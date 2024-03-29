from __future__ import annotations
import aoc
from itertools import pairwise
from functools import cache
import re
from collections import Counter, defaultdict


# fmt: off
TESTS_1 = [
("""
NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
""", 1588),
]

TESTS_2 = [
("""
NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
""", 2188189693529),
]
# fmt: on


@aoc.submit(part=1)
@aoc.get_input
@aoc.tests(TESTS_1)
@aoc.parse_text
def part_1(raw: str, ints: list[int], strs: list[str], **kwargs):
    template , rules = raw.split('\n\n')
    c = counts(rules=rules, text=template, steps=10)
    return max(c.values()) - min(c.values())


@aoc.submit(part=2)
@aoc.get_input
@aoc.tests(TESTS_2)
@aoc.parse_text
def part_2(raw: str, ints: list[int], strs: list[str], **kwargs):
    template , rules = raw.split('\n\n')
    c = counts(rules=rules, text=template, steps=40)
    return max(c.values()) - min(c.values())


@cache
def counts(*, rules: str, text: str, steps: int) -> dict:
    translations = load_translations(rules)

    if steps == 0:
        return Counter(text)

    counter = Counter({text[0]: 1})
    for a, b in pairwise(text):
        c = translations.get(a + b, '')
        counter.update(counts(rules=rules, text=a + c + b, steps=steps - 1))
        counter[a] -= 1

    return counter


@cache
def load_translations(rules: str) -> dict[str, str]:
    t = {}
    for rule in rules.splitlines():
        a, b = rule.split(" -> ")
        t[a] = b
    return t


if __name__ == "__main__":
    print("Part 1:", part_1(__file__))
    print("Part 2:", part_2(__file__))
