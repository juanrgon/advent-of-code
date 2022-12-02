from __future__ import annotations
import aoc
import attr
import string
from functools import cache
from collections import Counter


# fmt: off
TESTS_1 = [
("""
start-A
start-b
A-c
A-b
b-d
A-end
b-end
""", 10),

("""
dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc
""", 19),

("""
fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW
""", 226),
]

TESTS_2 = [
("""
start-A
start-b
A-c
A-b
b-d
A-end
b-end
""", 36),

("""
dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc
""", 103),

("""
fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW
""", 3509),
]
# fmt: on


@attr.define(eq=False)
class Cave:
    name: str
    reachable: list[Cave]

    def small(self) -> bool:
        return self.name[0] in string.ascii_lowercase

    def paths_to_cave(
        self, c: Cave, exclude: list[Cave] | None = None
    ) -> list[list[str]]:
        paths = []
        exclude = exclude or []

        for cave in self.reachable:
            if cave in exclude:
                continue

            if cave == c:
                paths.append([self.name, c.name])

            else:
                for subpath in cave.paths_to_cave(
                    c, exclude=([cave] if cave.small() else []) + exclude
                ):
                    paths.append([self.name] + subpath)

        return paths

    def paths_to_cave_2(
        self, c: Cave, visited: list[Cave] | None = None
    ) -> list[list[str]]:
        paths = []

        visited = visited or []
        if self.small():
            visited = [self] + visited

        for cave in self.reachable:
            if cave.small() and cave in visited and len(set(visited)) != len(visited):
                continue

            if cave == c:
                paths.append([self.name, c.name])

            else:
                for subpath in cave.paths_to_cave_2(c, visited=visited):
                    paths.append([self.name] + subpath)

        return paths


@aoc.submit(part=1)
@aoc.get_input
@aoc.tests(TESTS_1)
@aoc.parse_text
def part_1(raw: str, ints: list[int], strs: list[str], **kwargs):
    caves: dict[str, Cave] = {}

    start = caves.setdefault("start", Cave(name="start", reachable=[]))
    end = caves.setdefault("end", Cave(name="end", reachable=[]))

    for path in strs:
        s, e = path.split("-")

        cave_s = caves.setdefault(s, Cave(name=s, reachable=[]))
        cave_e = caves.setdefault(e, Cave(name=e, reachable=[]))

        if cave_e != start:
            cave_s.reachable.append(cave_e)

        if cave_s != start and cave_s not in cave_e.reachable:
            cave_e.reachable.append(cave_s)

    paths = start.paths_to_cave(end)

    return len(paths)


@aoc.submit(part=2)
@aoc.get_input
@aoc.tests(TESTS_2)
@aoc.parse_text
def part_2(raw: str, ints: list[int], strs: list[str], **kwargs):
    caves: dict[str, Cave] = {}

    start = caves.setdefault("start", Cave(name="start", reachable=[]))
    end = caves.setdefault("end", Cave(name="end", reachable=[]))

    for path in strs:
        s, e = path.split("-")

        cave_s = caves.setdefault(s, Cave(name=s, reachable=[]))
        cave_e = caves.setdefault(e, Cave(name=e, reachable=[]))

        if cave_e != start:
            cave_s.reachable.append(cave_e)

        if cave_s != start and cave_s not in cave_e.reachable:
            cave_e.reachable.append(cave_s)

    paths = start.paths_to_cave_2(end)

    return len(paths)


if __name__ == "__main__":
    print("Part 1:", part_1(__file__))
    print("Part 2:", part_2(__file__))
