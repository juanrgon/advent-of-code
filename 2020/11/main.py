import os.path
import re
from itertools import (
    product,
)


def main():
    print("Solution to Part 1: " + str(_part_1()))
    print("Solution to Part 2: " + str(_part_2()))


def _part_1():
    return 0


def _part_2():
    return 0


def f():
    f = "input"
    # f = 'test'
    with open(os.path.join(os.path.dirname(__file__), f)) as f:
        return f.read().strip()


class Grid(dict):

    def display(self):
        height = max(self.keys(), key=lambda rc: rc[0], default=[-1, -1])[0] + 1
        width = max(self.keys(), key=lambda rc: rc[1], default=[-1, -1])[1] + 1

        for row in range(height):
            for col in range(width):
                s = self.get((row, col), Floor())
                print(s.symbol(), end="")
            print()

    def _connect(self):
        self.


def _connect():
    pass

class Space:
    def __init__(self):
        self.siblings = {}

    def __repr__(self):
        return self.symbol()


class Floor(Space):
    def symbol(self):
        return "."


class Seat(Space):
    def __init__(self, occupied):
        self.siblings = {}
        self.occupied = occupied

    def symbol(self):
        return "#" if self.occupied else "L"

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


grid = Grid()

rows = f().split("\n")
for r, row in enumerate(rows):
    for c, char in enumerate(row):
        if char == ".":
            grid[r, c] = Floor()
        else:
            grid[r, c] = Seat(occupied=(char == "#"))

grid.display()


# for (row, col), s in seats.items():
#     for a, b in product(range(-1, 2), repeat=2):
#         if (a, b) == (0, 0):
#             continue

#         t = seats.get((row + a, col + b))
#         if t:
#             s.siblings[(a, b)] = t


# while True:
#     n = dict()
#     for seat in seats.values():
#         if seat.is_dot:
#             continue
#         n[(seat.row, seat.col)] = seat.next_2()

#     prev = len([s for s in seats.values() if not s.is_dot and s.occupied])

#     for (a, b), state in n.items():
#         seats[(a, b)].occupied = state

#     if prev == len([s for s in seats.values() if not s.is_dot and s.occupied]):
#         break

#     # for r in range(10):
#     #     for c in range(10):
#     #         s = seats.get((r, c))
#     #         if not s.is_dot:
#     #             print('#' if s.occupied else 'L', end ='')
#     #         else:
#     #             print('.', end='')
#     #     print()
#     # print("--------------------")

# print(prev)


if __name__ == "__main__":
    main()
