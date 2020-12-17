import os.path
from collections import defaultdict
import re
from itertools import *
from collections import *
from more_itertools import *
from sortedcontainers import *
import sys
from pathlib import Path
from functools import lru_cache
import math


def main():
    print("Solution to Part 1: " + str(_part_1()))
    print("Solution to Part 2: " + str(_part_2()))


def _part_1():
    return 0
    nearby = f().split("nearby tickets:")[1].strip().splitlines()
    fields = f().split("your ticket")[0].strip().splitlines()

    ranges = []
    for l in fields:
        a, b, c, d = ints(l)
        ranges.append([a, b, c, d])

    errors = 0
    for nt in nearby:
        for n in ints(nt):
            for a, b, c, d in ranges:
                if (a <= n <= b) or (c <= n <= d):
                    break
            else:
                errors += n

    return errors


def _part_2():
    fields_text, your_ticket_text, nearby_tickets_text = f().split("\n\n")

    fields = dict()
    for line in fields_text.splitlines():
        key, a, b, c, d = re.split(" or |-|: ", line)
        fields[key] = set(range(int(a), int(b) + 1)).union(
            set(range(int(c), int(d) + 1))
        )

    your_ticket = ints(your_ticket_text)

    tickets = []
    all_valid_numbers = set.union(*fields.values())
    for line in nearby_tickets_text.splitlines()[1:]:
        ticket = [int(i) for i in line.split(",")]
        if all(val in all_valid_numbers for val in ticket):
            tickets.append(ticket)

    position_candidates = defaultdict(list)
    for i in range(len(your_ticket)):
        for name, valid_values in fields.items():
            pass
            if all([ticket[i] in valid_values for ticket in tickets]):
                position_candidates[i].append(name)

    fields_found = [pc[0] for pc in position_candidates.values() if len(pc) == 1]

    while len(fields_found) != len(position_candidates):
        for found_field in fields_found:
            for candidates in position_candidates.values():
                if len(candidates) > 1 and found_field in candidates:
                    candidates.remove(found_field)
        fields_found = [pc[0] for pc in position_candidates.values() if len(pc) == 1]

    ticket_positions = {
        name_list[0]: idx for idx, name_list in position_candidates.items()
    }

    return math.prod(
        [
            your_ticket[v]
            for k, v in ticket_positions.items()
            if k.startswith("departure")
        ]
    )


def f():
    with open(os.path.join(os.path.dirname(__file__), "input")) as f:
        return f.read().strip()


@lru_cache
def ints(text):
    if callable(text):
        text = text()
    return [int(i) for i in re.findall(r"-?\d+", text)]


if __name__ == "__main__":
    main()
