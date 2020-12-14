import os.path
from collections import defaultdict
import re
import sys


def ints(text):
    if callable(text):
        text = text()
    return [int(i) for i in re.findall(r"\d+", text)]


def main():
    print("Solution to Part 1: " + str(_part_1()))
    print("Solution to Part 2: " + str(_part_2()))


def _part_1():
    lines = f().splitlines()
    mask = lines[0].split("=")[1].strip()
    code = lines[1:]

    mem = {}
    for c in code:
        if c.startswith("mask"):
            mask = c.split("=")[1].strip()
            continue

        add, binary = ints(c)

        binary = str(bin(binary)[2:]).zfill(len(mask))

        val = "".join([v if m == "X" else m for v, m in zip(binary, mask)])
        mem[add] = val

    return sum(list([int(i, 2) for i in mem.values()]))


def _part_2():
    lines = f().splitlines()
    mask = lines[0].split("=")[1].strip()
    code = lines[1:]

    mem = {}
    for c in code:
        if c.startswith("mask"):
            mask = c.split("=")[1].strip()
            continue

        add, val = ints(c)

        new_addresses = all_addresses(
            ["".join([m if m != "0" else v for v, m in zip(bin(add)[2:].zfill(len(mask)), mask)])]
        )

        for add in new_addresses:
            mem[add] = val

    return sum(list([i for i in mem.values()]))


def all_addresses(addresses):
    new = []
    for add in addresses:
        if "X" not in add:
            new.append(add)
        else:
            new += all_addresses([add.replace("X", "0", 1), add.replace("X", "1", 1)])
    return new


def f():
    if "t" in sys.argv or "-t" in sys.argv:
        name = "test"
    else:
        name = "input"

    with open(os.path.join(os.path.dirname(__file__), name)) as f:
        return f.read().strip()



if __name__ == "__main__":
    main()
