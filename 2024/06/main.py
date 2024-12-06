import aoc


@aoc.solution(1)
def part_1(
    raw: aoc.String,
    ints: aoc.Integers,
    strs: list[aoc.String],
    paragraphs: list[aoc.Paragraph],
):
    # Directions in order: up, right, down, left
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    grid = strs

    # Locate guard, facing direction
    start_i, start_j, d = None, None, None
    for i, row in enumerate(grid):
        for j, c in enumerate(row):
            if c in "^v<>":
                start_i, start_j = i, j
                d = {"^": 0, ">": 1, "v": 2, "<": 3}[c]
                break
        if start_i is not None:
            break

    visited = set([(start_i, start_j)])
    i, j = start_i, start_j
    R, C = len(grid), len(grid[0])

    def in_bounds(x, y):
        return 0 <= x < R and 0 <= y < C

    while True:
        # Check next cell in facing direction
        di, dj = dirs[d]
        ni, nj = i + di, j + dj

        # If out of bounds, done
        if not in_bounds(ni, nj):
            break
        # If obstacle ahead, turn right
        if grid[ni][nj] == "#":
            d = (d + 1) % 4
            continue
        # Move forward
        i, j = ni, nj
        visited.add((i, j))

    if len(strs) <= 10:  # Only print for test case
        print("Final path:")
        for y in range(len(grid)):
            row = list(grid[y])
            for vpos in visited:
                if vpos[0] == y:
                    row[vpos[1]] = "X"
            print("".join(row))
        print()

    return len(visited)


@aoc.solution(2)
def part_2(
    raw: aoc.String,
    ints: aoc.Integers,
    strs: list[aoc.String],
    paragraphs: list[aoc.Paragraph],
):
    R, C = len(strs), len(strs[0])
    dirs = [(-1,0), (0,1), (1,0), (0,-1)]
    dir_map = {'^':0, '>':1, 'v':2, '<':3}

    # Find guard start & direction
    start_i, start_j, d = None, None, None
    for i in range(R):
        for j in range(C):
            if strs[i][j] in dir_map:
                start_i, start_j = i, j
                d = dir_map[strs[i][j]]
                break
        if start_i is not None:
            break

    # Convert to list of lists for easier manipulation
    grid_map = [list(row) for row in strs]

    def in_bounds(x,y):
        return 0 <= x < R and 0 <= y < C

    def simulate(with_obstacle=None):
        # with_obstacle = (x,y) if we place new obstruction at (x,y)
        # If with_obstacle is given, place '#' there temporarily (if not start)
        if with_obstacle:
            ox, oy = with_obstacle
            grid_map[ox][oy] = '#'

        i, j, curr_d = start_i, start_j, d
        visited_states = set() # track (i, j, direction)

        while True:
            state = (i, j, curr_d)
            if state in visited_states:
                # loop detected
                result = 'loop'
                break
            visited_states.add(state)

            di, dj = dirs[curr_d]
            ni, nj = i+di, j+dj

            # Out of bounds means guard leaves
            if not in_bounds(ni,nj):
                result = 'leave'
                break

            # Obstacle ahead?
            if grid_map[ni][nj] == '#':
                # turn right
                curr_d = (curr_d+1)%4
                continue

            # move forward
            i, j = ni, nj

        # Clean up obstacle if placed
        if with_obstacle:
            ox, oy = with_obstacle
            grid_map[ox][oy] = '.'

        return result

    # Mark all empty spaces as '.' for simplicity
    for i in range(R):
        for j in range(C):
            if grid_map[i][j] in '^v<>':
                grid_map[i][j] = '.'

    # Check each cell
    loop_positions = []
    for i in range(R):
        for j in range(C):
            if (i,j) == (start_i,start_j): # can't place at start
                continue
            if grid_map[i][j] == '.':
                outcome = simulate((i,j))
                if outcome == 'loop':
                    loop_positions.append((i,j))

    return len(loop_positions)


if __name__ == "__main__":
    print("Part 1:", part_1(__file__))
    print("Part 2:", part_2(__file__))
