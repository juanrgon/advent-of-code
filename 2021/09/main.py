TEST = [
    (
        """
2199943210
3987894921
9856789892
8767896789
9899965678
""",
        15,
    )
]

TEST2 = [
    (
        """
2199943210
3987894921
9856789892
8767896789
9899965678
""",
        1134,
    )
]


import aoc
import math


@aoc.submit(part=1)
@aoc.get_input
@aoc.tests(TEST)
@aoc.parse_text
def part_1(raw: str, ints: list[int], strs: list[str]):
    total = 0

    for i, row in enumerate(strs):
        for j, num in enumerate(row):
            low = True

            # left num
            if j - 1 >= 0 and row[j - 1] <= num:
                low = False

            # right num
            if j + 1 < len(row) and row[j + 1] <= num:
                low = False

            # upper num
            if i - 1 >= 0 and strs[i - 1][j] <= num:
                low = False

            # bottom num
            if i + 1 < len(strs) and strs[i + 1][j] <= num:
                low = False

            if low:
                total += 1 + int(num)

    return total


@aoc.submit(part=2)
@aoc.get_input
@aoc.tests(TEST2)
@aoc.parse_text
def part_2(raw: str, ints: list[int], strs: list[str]):
    total = 0

    points = []

    for i, row in enumerate(strs):
        for j, num in enumerate(row):
            low = True

            # left num
            if j - 1 >= 0 and row[j - 1] <= num:
                low = False

            # right num
            if (j + 1) < len(row) and row[j + 1] <= num:
                low = False

            # upper num
            if i - 1 >= 0 and strs[i - 1][j] <= num:
                low = False

            # bottom num
            if (i + 1) < len(strs) and strs[i + 1][j] <= num:
                low = False

            if low:
                total += 1 + int(num)
                points.append((i, j))

    basin_sizes = []
    for i, j in points:
        size = basin(tuple(strs), i, j, visited=[])
        basin_sizes.append(size)

    return math.prod(sorted(basin_sizes, reverse=True)[:3])

def basin(strs, i, j, visited) -> int:

    row = strs[i]

    num = strs[i][j]

    if (i, j) in visited:
        return 0

    visited.append((i, j))

    if num == '9':
        return 0

    size = 1
    # left num
    if j - 1 >= 0:
        size += basin(strs, i, j-1, visited)

    # right num
    if (j + 1) < len(row):
        size += basin(strs, i, j+1, visited)

    # upper num
    if i - 1 >= 0:
        size += basin(strs, i-1, j, visited)

    # bottom num
    if (i + 1) < len(strs):
        size += basin(strs, i+1, j, visited)

    return size


if __name__ == "__main__":
    print("Part 1:", part_1(__file__))
    print("Part 2:", part_2(__file__))
