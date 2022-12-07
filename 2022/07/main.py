from __future__ import annotations
import aoc
import attr
from collections import defaultdict


@aoc.solution(1)
def part_1(
    raw: aoc.String,
    ints: aoc.Integers,
    strs: list[aoc.String],
    paragraphs: list[aoc.Paragraph],
):

    filesystem = defaultdict(Dir)
    cur_dir: Dir = Dir(parent=None, contents=[], name="/")
    filesystem["/"] = cur_dir
    files = []
    for l in strs:
        if l.startswith("$"):
            if l.startswith("$ cd"):
                _, cmd, dirname = l.split()

                if dirname == "/":
                    cur_dir = filesystem["/"]
                    cur_dir.name = "/"

                elif dirname == "..":
                    cur_dir = cur_dir.parent

                else:
                    parent = cur_dir
                    cur_dir = filesystem[cur_dir.path() + dirname + "/"]
                    cur_dir.parent = parent
                    cur_dir.name = dirname

        elif l.startswith("dir"):
            _, dirname = l.split(" ")
            dir = filesystem[cur_dir.path() + dirname + "/"]
            dir.name = dirname
            cur_dir.contents.append(dir)
        else:
            size, filename = l.split(" ")
            file = File(parent=cur_dir, name=filename, size=int(size))
            filesystem[file.path()] = file
            cur_dir.contents.append(file)

    size = 0
    for i in filesystem.values():
        if isinstance(i, Dir):
            d_size = i.total_size()
            if d_size <= 100000:
                size += d_size
    return size


@aoc.solution(2)
def part_2(
    raw: aoc.String,
    ints: aoc.Integers,
    strs: list[aoc.String],
    paragraphs: list[aoc.Paragraph],
):
    filesystem = defaultdict(Dir)
    cur_dir: Dir = Dir(parent=None, contents=[], name="/")
    filesystem["/"] = cur_dir
    files = []
    for l in strs:
        if l.startswith("$"):
            if l.startswith("$ cd"):
                _, cmd, dirname = l.split()

                if dirname == "/":
                    cur_dir = filesystem["/"]
                    cur_dir.name = "/"

                elif dirname == "..":
                    cur_dir = cur_dir.parent

                else:
                    parent = cur_dir
                    cur_dir = filesystem[cur_dir.path() + dirname + "/"]
                    cur_dir.parent = parent
                    cur_dir.name = dirname

        elif l.startswith("dir"):
            _, dirname = l.split(" ")
            dir = filesystem[cur_dir.path() + dirname + "/"]
            dir.name = dirname
            cur_dir.contents.append(dir)
        else:
            size, filename = l.split(" ")
            file = File(parent=cur_dir, name=filename, size=int(size))
            filesystem[file.path()] = file
            cur_dir.contents.append(file)

    root_size = filesystem["/"].total_size()
    avail = 70000000 - root_size
    needed = 30000000 - avail

    smallest = float("inf")
    for i in filesystem.values():
        if isinstance(i, Dir):
            d_size = i.total_size()
            if d_size >= needed:
                if d_size < smallest:
                    smallest = d_size
    return smallest


@attr.define
class File:
    parent: "Dir"
    name: str
    size: int

    def path(self):
        return self.parent.path() + self.name


@attr.define
class Dir:
    parent: Dir | None = None
    contents: list[Dir | File] = attr.field(factory=list)
    name: str = ""

    def path(self):
        if self.parent is None:
            return self.name
        return self.parent.path() + self.name + "/"

    def total_size(self):
        size = 0

        for c in self.contents:
            if isinstance(c, File):
                size += c.size
            else:
                size += c.total_size()

        return size


if __name__ == "__main__":
    print("Part 1:", part_1(__file__))
    print("Part 2:", part_2(__file__))
