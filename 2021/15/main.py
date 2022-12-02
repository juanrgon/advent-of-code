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
import sys


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
""", 315),
]
# fmt: on

import sys


@aoc.submit(part=1)
@aoc.get_input
@aoc.tests(TESTS_1)
@aoc.parse_text
def part_1(raw: str, ints: list[int], strs: list[str], **kwargs):
    risks = aoc.Grid.from_str(raw)

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
            current_cost = base_cost + c
            if neighbor not in shortest_paths_so_far:
                shortest_paths_so_far[neighbor] = 9 * neighbor[0] + 9 * neighbor[1]

            shortest_paths_so_far[neighbor] = min(
                current_cost, shortest_paths_so_far[neighbor]
            )
            if current_cost > min(shortest_paths_so_far[neighbor], max_cost):
                continue

            lowest = min(
                lowest_risk_path(neighbor, end, base_cost=current_cost) + c, lowest
            )

        return lowest

    return lowest_risk_path((0, 0), (risks.width() - 1, risks.height() - 1))


@aoc.submit(part=2)
@aoc.get_input
@aoc.tests(TESTS_2)
@aoc.parse_text
def part_2(raw: str, ints: list[int], strs: list[str], **kwargs):
    risks = aoc.Grid.from_str(raw)

    def increment(num):
        num += 1
        if num >= 10:
            num = 1
        return num

    # build the new grid
    grids = [risks]
    for i in range(4):
        grids.append(grids[-1].modify(increment))

    for grid in grids[1:]:
        risks = risks.append_right(grid)

    grids = [risks]
    for i in range(4):
        grids.append(grids[-1].modify(increment))

    for grid in grids[1:]:
        risks = risks.append_below(grid)

    max_cost = (
        risks.width() * 9
    )  # max cost should be under this value, since the grid is

    sys.setrecursionlimit(risks.width() * risks.width())

    shortest_paths_so_far = {}
    shortest_paths_so_far[(0, 0)] = 0

    @cache
    def _shortest_path_default(point):
        x, y = point

        if (x, y) == (0, 0):
            return 0

        if x == 0:
            return _shortest_path_default((x, y - 1)) + risks[x, y]
        elif y == 0:
            return _shortest_path_default((x - 1, y)) + risks[x, y]
        else:
            return (
                min(
                    _shortest_path_default((x - 1, y)),
                    _shortest_path_default((x, y - 1)),
                )
                + risks[x, y]
            )

    for x in range(risks.height()):
        for y in range(risks.width()):
            shortest_paths_so_far[x, y] = _shortest_path_default((x, y))

    @cache
    def lowest_risk_path(start: tuple, end: tuple, base_cost=0):
        if start == end:
            return 0

        lowest = (end[0] - start[0]) * 9 + (end[1] - start[1]) * 9
        shortest_paths_so_far[start] = shortest_paths_so_far.get(start, lowest)
        for neighbor, c in (
            risks.x_neighbors(start) | risks.y_neighbors(start)
        ).items():
            current_cost = base_cost + c

            if neighbor not in shortest_paths_so_far:
                x, y = neighbor
                max_cost = x * 9 + y * 9

                if x == 0:
                    max_cost = shortest_paths_so_far[(x, y - 1)] + 9
                elif y == 0:
                    max_cost = shortest_paths_so_far[(x - 1, y)] + 9
                else:
                    max_cost = (
                        min(
                            shortest_paths_so_far[x - 1, y],
                            shortest_paths_so_far[x, y - 1],
                        )
                        + 9
                    )

                shortest_paths_so_far[neighbor] = max_cost

            shortest_paths_so_far[neighbor] = min(
                current_cost, shortest_paths_so_far[neighbor]
            )

            if current_cost > shortest_paths_so_far[neighbor]:
                continue

            lowest = min(
                lowest_risk_path(neighbor, end, base_cost=current_cost) + c, lowest
            )
            shortest_paths_so_far[start] = shortest_paths_so_far.get(start, lowest)

        return lowest

    return lowest_risk_path((0, 0), (risks.width() - 1, risks.height() - 1))


if __name__ == "__main__":
    print("Part 1:", part_1(__file__))
    print("Part 2:", part_2(__file__))
