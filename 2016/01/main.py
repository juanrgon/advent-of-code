from __future__ import annotations
import aoc
from itertools import cycle


# fmt: off
TESTS_1 = [
("""
R2, L3
""", 5),
("""
R2, R2, R2
""", 2),
("""
R5, L5, R5, R3
""", 12),
]

TESTS_2 = [
("""
R8, R4, R4, R8
""", 4),
]
# fmt: on


@aoc.submit(part=1)
@aoc.get_input
@aoc.tests(TESTS_1)
@aoc.parse_text
def part_1(raw: str, ints: list[int], strs: list[str]):
    position = (0, 0)

    direction = 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for inst in raw.split(', '):
        turn = inst[0]
        move = int(inst[1:])

        if turn == 'R':
            direction += 1
        elif turn == 'L':
            direction -= 1

        dx, dy = directions[direction % 4]
        position = position[0] + dx * move, position[1] + dy * move

    return abs(position[0]) + abs(position[1])


@aoc.submit(part=2)
@aoc.get_input
@aoc.tests(TESTS_2)
@aoc.parse_text
def part_2(raw: str, ints: list[int], strs: list[str]):
    position = (0, 0)

    direction = 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    visited = set()

    for inst in raw.split(', '):
        turn = inst[0]
        move = int(inst[1:])

        if turn == 'R':
            direction += 1
        elif turn == 'L':
            direction -= 1

        dx, dy = directions[direction % 4]
        position = position[0] + dx * move, position[1] + dy * move

        if position in visited:
            return abs(position[0]) + abs(position[1])

        visited.add(position)



if __name__ == "__main__":
    print("Part 1:", part_1(__file__))
    print("Part 2:", part_2(__file__))
