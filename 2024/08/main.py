from collections import defaultdict
import aoc
import math

@aoc.solution(1)
def part_1(raw: aoc.String, *_, **__):
    # Parse input grid
    grid = raw.splitlines()
    grid_height = len(grid)
    grid_width = len(grid[0])

    # Collect antenna positions and group by frequency
    freq_groups = defaultdict(list)
    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch != ".":
                freq_groups[ch].append((r, c))

    antinodes = set()

    # For each frequency group, find pairs and their antinodes
    for points in freq_groups.values():
        n = len(points)
        for i in range(n):
            for j in range(i + 1, n):
                r1, c1 = points[i]
                r2, c2 = points[j]

                # Antinode 1: 2B - A
                R1, C1 = 2 * r2 - r1, 2 * c2 - c1

                # Antinode 2: 2A - B
                R2, C2 = 2 * r1 - r2, 2 * c1 - c2

                if 0 <= R1 < grid_height and 0 <= C1 < grid_width:
                    antinodes.add((R1, C1))

                if 0 <= R2 < grid_height and 0 <= C2 < grid_width:
                    antinodes.add((R2, C2))

    return len(antinodes)


@aoc.solution(2)
def part_2(raw: aoc.String, *_, **__):
    # Parse input grid
    grid = raw.splitlines()
    height = len(grid)
    width = len(grid[0])

    # Collect antenna positions by frequency
    freq_groups = defaultdict(list)
    for r in range(height):
        for c in range(width):
            ch = grid[r][c]
            if ch != '.':
                freq_groups[ch].append((r, c))

    antinodes = set()

    # For each frequency group, find all lines determined by pairs of antennas
    for points in freq_groups.values():
        # Skip if only one antenna of this frequency
        if len(points) < 2:
            continue

        # Process each pair of points
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                r1, c1 = points[i]
                r2, c2 = points[j]
                dr = r2 - r1
                dc = c2 - c1

                # Normalize direction to primitive vector using GCD
                g = math.gcd(dr, dc)
                dr //= g
                dc //= g

                # Ensure consistent direction
                if dr < 0 or (dr == 0 and dc < 0):
                    dr = -dr
                    dc = -dc

                # Generate all points on the line within grid bounds
                # Forward direction from (r1,c1)
                rr, cc = r1, c1
                while 0 <= rr < height and 0 <= cc < width:
                    antinodes.add((rr, cc))
                    rr += dr
                    cc += dc

                # Backward direction from (r1,c1)
                rr, cc = r1 - dr, c1 - dc
                while 0 <= rr < height and 0 <= cc < width:
                    antinodes.add((rr, cc))
                    rr -= dr
                    cc -= dc

    return len(antinodes)


if __name__ == "__main__":
    print("Part 1:", part_1(__file__))
    print("Part 2:", part_2(__file__))
