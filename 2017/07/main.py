TEST = [(
    """
pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)
""",
    "tknk",
)]

TEST2 = [(
    """
pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)
""",
    60,
)]


import sys
from pathlib import Path
from typing import List, Optional
from collections import Counter, defaultdict
import attr

# import local AOC lib
sys.path.append(str(Path(__file__).parent.parent.parent))
import aoc


@attr.s(auto_attribs=True)
class Node:
    weight: int = 0
    children: List["Node"] = None

    def total_weight(self):
        return self.weight + sum([c.total_weight() for c in self.children], start=0)


@aoc.submit(part=1)
@aoc.get_input
@aoc.tests(TEST)
@aoc.parse_text
def part_1(raw: str, ints: List[int], strs: List[str], **kwargs):
    held = set()
    all = set()

    for p in strs:
        d = ""
        if "->" in p:
            p, d = p.split(" -> ")

        p, w = p.split()
        w = w.strip("()")

        all.add(p)

        for p in d.split(", "):
            held.add(p)

    return list(all.difference(held))[0]


@aoc.submit(part=2)
@aoc.get_input
@aoc.tests(TEST2)
@aoc.parse_text
def part_2(raw: str, ints: List[int], strs: List[str], **kwargs):
    held = set()
    all = set()

    tower = defaultdict(lambda: Node(weight=0, children=[]))

    for p in strs:
        d = ""
        if "->" in p:
            p, d = p.split(" -> ")

        p, w = p.split()
        w = w.strip("()")

        tower[p].weight = int(w)

        all.add(p)

        if d:
            for s in d.split(", "):
                tower[p].children.append(tower[s])
                held.add(s)

    root = tower[list(all.difference(held))[0]]

    return new_weight(root)


def new_weight(node):
    if not node.children:
        return 0

    heavy_child = max(node.children, key=lambda c: c.total_weight())
    normal_child = min(node.children, key=lambda c: c.total_weight())

    diff = heavy_child.total_weight() - normal_child.total_weight()

    if diff == 0:
        return 0

    return new_weight(heavy_child) or heavy_child.weight - diff


if __name__ == "__main__":
    print("Part 1:", part_1(__file__))
    print("Part 2:", part_2(__file__))
