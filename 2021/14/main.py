from __future__ import annotations
import aoc
from itertools import pairwise


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

import re
from collections import Counter, defaultdict


@aoc.submit(part=1)
@aoc.get_input
@aoc.tests(TESTS_1)
@aoc.parse_text
def part_1(raw: str, ints: list[int], strs: list[str]):
    global translations
    template = strs[0]
    translations = dict()
    regex = {}
    for rules in strs[1:]:
        a, b = rules.split(" -> ")
        a0, a1 = list(a)

        translations[a] = f"{a0}{b}"

    for i in range(10):
        parts = list(template)
        for j in range(len(template) - 1):
            s = template[j] + template[j + 1]
            if s in translations:
                parts[j] = translations[s]
        template = "".join(parts)

    c = Counter(template)
    A = c.most_common(1)[0][1]
    B = c.most_common(len(set(template)))[-1][1]

    return A - B


@aoc.submit(part=2)
@aoc.get_input
@aoc.tests(TESTS_2)
@aoc.parse_text
def part_2(raw: str, ints: list[int], strs: list[str]):
    template = strs[0]

    c = counts(rules="\n".join(strs[1:]), text=template, steps=40)
    A = max(c.values())
    B = min(c.values())

    return A - B


from functools import cache


@cache
def counts(*, rules: str, text: str, steps: int) -> dict:
    translations = load_translations(rules)

    if steps == 0:
        return Counter(text)

    counter = Counter()
    for a, b in pairwise(text):
        c = translations.get(a + b)
        if c:
            counter.update(counts(rules=rules, text=a + c + b, steps=steps - 1))
            counter[a] -= 1
        else:
            counter[a] += 1
            counter[b] += 1

    counter[text[0]] += 1

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
