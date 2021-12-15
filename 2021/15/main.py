from __future__ import annotations
import aoc
from collections import defaultdict, Counter
from itertools import (
    combinations,
    count,
    permutations,
    combinations_with_replacement,
    product,
    cycle,
    accumulate,
    pairwise,
)
from more_itertools import windowed
import terminology
from functools import cache
import re
import attr


# fmt: off
TESTS_1 = [
("""
1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
""", 40),
]

TESTS_2 = [
("""
""", -42),
]
# fmt: on

import sys


@attr.define
class Cave:
    risk: int

    @classmethod
    def from_str(cls, s):
        return cls(int(s))


@aoc.submit(part=1)
@aoc.get_input
@aoc.tests(TESTS_1)
@aoc.parse_text
def part_1(raw: str, ints: list[int], strs: list[str]):
    risks = aoc.Grid.from_str(raw, init=Cave.from_str)

    shortest_paths_so_far = defaultdict(lambda: 1800)
    shortest_paths_so_far[(0, 0)] = 0

    max_cost = 1800  # max cost should be under this value, since the grid is
                    # 100 x 100

    @cache
    def lowest_risk_path(start: tuple, end: tuple, base_cost=0):
        if start == end:
            return 0

        lowest = float("inf")
        for neighbor, c in (
            risks.x_neighbors(start) | risks.y_neighbors(start)
        ).items():
            current_cost = base_cost + c.risk
            if neighbor not in shortest_paths_so_far:
                shortest_paths_so_far[neighbor] = 9 * neighbor[0] + 9 * neighbor[1]

            shortest_paths_so_far[neighbor] = min(
                current_cost, shortest_paths_so_far[neighbor]
            )
            if current_cost > min(shortest_paths_so_far[neighbor], max_cost):
                continue

            lowest = min(
                lowest_risk_path(neighbor, end, base_cost=current_cost) + c.risk, lowest
            )

        return lowest

    return lowest_risk_path((0, 0), (risks.width() - 1, risks.height() - 1))


@aoc.submit(part=2)
@aoc.get_input
@aoc.tests(TESTS_2)
@aoc.parse_text
def part_2(raw: str, ints: list[int], strs: list[str]):
    risks = aoc.Grid.from_str(raw, init=Cave.from_str)

    shortest_paths_so_far = defaultdict(lambda: float("inf"))
    shortest_paths_so_far[(0, 0)] = 0

    max_cost = 900  # max cost should probably be under this value, since the grid is
    # 100 x 100

    @cache
    def lowest_risk_path(start: tuple, end: tuple, base_cost=0):
        if start == end:
            return 0

        lowest = float("inf")
        for neighbor, c in (
            risks.x_neighbors(start) | risks.y_neighbors(start)
        ).items():
            current_cost = base_cost + c.risk
            shortest_paths_so_far[neighbor] = min(
                current_cost, shortest_paths_so_far[neighbor]
            )
            if current_cost > min(shortest_paths_so_far[neighbor], max_cost):
                continue

            lowest = min(
                lowest_risk_path(neighbor, end, base_cost=current_cost) + c.risk, lowest
            )

        return lowest

    return lowest_risk_path((0, 0), (risks.width() - 1, risks.height() - 1))


if __name__ == "__main__":
    print("Part 1:", part_1(__file__))
    print("Part 2:", part_2(__file__))
