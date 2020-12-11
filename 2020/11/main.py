import os.path
from collections import defaultdict
import re
from itertools import (
    product,
)


def f():
    f = "input"
    # f = 'test'
    with open(os.path.join(os.path.dirname(__file__), f)) as f:
        return f.read().strip()


class S:
    def __init__(self):
        self.siblings = {}

    def next(self):
        if len([s for s in self.sibling_seats() if s.occupied]) >= 4:
            return False

        if not any([s.occupied for s in self.sibling_seats() if s.occupied]):
            return True

        return self.occupied

    def sibling_seats(self):
        return [s for s in self.siblings.values() if not s.is_dot]

    def next_2(self):
        count = 0
        for a, b in product(range(-1, 2), repeat=2):
            neighbor = self.neighbor((a, b))
            if neighbor and neighbor.occupied:
                count += 1
                if count >= 5:
                    return False
        if count == 0:
            return True

        return self.occupied

    def neighbor(self, direction):
        sib = self.siblings.get(direction)

        if not sib:
            return None

        if not sib.is_dot:
            return sib
        else:
            return sib.neighbor(direction)


seats = defaultdict(S)
rows = f().split("\n")
for r, row in enumerate(rows):
    for c, char in enumerate(row):
        s = seats[(r, c)]
        if char != ".":
            s.occupied = char == "#"
            s.is_dot = False
            s.row = r
            s.col = c
        else:
            s.is_dot = True
            s.occupied = False
            s.row = r
            s.col = c


seats = dict(seats)

for (row, col), s in seats.items():
    for a, b in product(range(-1, 2), repeat=2):
        if (a, b) == (0, 0):
            continue

        t = seats.get((row + a, col + b))
        if t:
            s.siblings[(a, b)] = t



while True:
    n = dict()
    for seat in seats.values():
        if seat.is_dot:
            continue
        n[(seat.row, seat.col)] = seat.next_2()

    prev = len([s for s in seats.values() if not s.is_dot and s.occupied])

    for (a, b), state in n.items():
        seats[(a, b)].occupied = state

    if prev == len([s for s in seats.values() if not s.is_dot and s.occupied]):
        break

    # for r in range(10):
    #     for c in range(10):
    #         s = seats.get((r, c))
    #         if not s.is_dot:
    #             print('#' if s.occupied else 'L', end ='')
    #         else:
    #             print('.', end='')
    #     print()
    # print("--------------------")

print(prev)
