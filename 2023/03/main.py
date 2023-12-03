from __future__ import annotations
import aoc


@aoc.solution(1)
def part_1(
    raw: aoc.String,
    ints: aoc.Integers,
    strs: list[aoc.String],
    paragraphs: list[aoc.Paragraph],
):
    # grid of (x, y) -> char
    grid = {}

    # build the grid
    for y, line in enumerate(strs):
        current_number = None

        for x, char in enumerate(line):
            grid[(x, y)] = char

    # coords of the numbers in the grid
    # (x_start, y) -> number
    num_coords = {}

    # find the numbers in the grid
    for y, line in enumerate(strs):
        current_number = None
        current_num_x_start = None

        for x, char in enumerate(line):
            if char.isdigit():
                if current_number is None:
                    current_number = char
                    current_num_x_start = x
                else:
                    current_number += char
                num_coords[(current_num_x_start, y)] = current_number
            else:
                current_number = None
                current_num_x_start = None

    nums = []
    # loop through the numbers and find the numbers that are surrounded by . or other digits only
    for (x_start, y), num in num_coords.items():
        x_stop = x_start + len(num) - 1
        surrounded = True
        for x in range(x_start, x_stop + 1):
            # check if the number is surrounded by . or other digits only
            # check the 4 directions
            # up
            up = (x, y - 1)
            if up in grid:
                up_char = grid[up]
                if up_char != "." and not up_char.isdigit():
                    surrounded = False
                    continue

            # down
            down = (x, y + 1)
            if down in grid:
                down_char = grid[down]
                if down_char != "." and not down_char.isdigit():
                    surrounded = False
                    continue

            # left
            left = (x - 1, y)
            if left in grid:
                left_char = grid[left]
                if left_char != "." and not left_char.isdigit():
                    surrounded = False
                    continue

            # right
            right = (x + 1, y)
            if right in grid:
                right_char = grid[right]
                if right_char != "." and not right_char.isdigit():
                    surrounded = False
                    continue

            # check the 4 diagonals
            top_left = (x - 1, y - 1)
            if top_left in grid:
                top_left_char = grid[top_left]
                if top_left_char != "." and not top_left_char.isdigit():
                    surrounded = False
                    continue

            top_right = (x + 1, y - 1)
            if top_right in grid:
                top_right_char = grid[top_right]
                if top_right_char != "." and not top_right_char.isdigit():
                    surrounded = False
                    continue

            bottom_left = (x - 1, y + 1)
            if bottom_left in grid:
                bottom_left_char = grid[bottom_left]
                if bottom_left_char != "." and not bottom_left_char.isdigit():
                    surrounded = False
                    continue

            bottom_right = (x + 1, y + 1)
            if bottom_right in grid:
                bottom_right_char = grid[bottom_right]
                if bottom_right_char != "." and not bottom_right_char.isdigit():
                    surrounded = False
                    continue

        if not surrounded:
            nums.append(num)

    return sum(int(num) for num in nums)


@aoc.solution(2)
def part_2(
    raw: aoc.String,
    ints: aoc.Integers,
    strs: list[aoc.String],
    paragraphs: list[aoc.Paragraph],
):
    # grid of (x, y) -> char
    grid = {}

    # build the grid
    for y, line in enumerate(strs):
        current_number = None

        for x, char in enumerate(line):
            grid[(x, y)] = char

    # coords of the numbers in the grid
    # (x_start, y) -> number
    num_coords = {}

    # find the numbers in the grid
    for y, line in enumerate(strs):
        current_number = None
        current_num_x_start = None

        for x, char in enumerate(line):
            if char.isdigit():
                if current_number is None:
                    current_number = char
                    current_num_x_start = x
                else:
                    current_number += char
                num_coords[(current_num_x_start, y)] = current_number
            else:
                current_number = None
                current_num_x_start = None

    # coords of the stars in the grid pointing to the set of coords of the numbers adjacent to them
    # (x, y) -> [(x_start, y)]
    star_nums = {}

    nums_coords = []
    # loop through the numbers and find the numbers that are surrounded by . or other digits only
    for (x_start, y), num in num_coords.items():
        x_stop = x_start + len(num) - 1

        for x in range(x_start, x_stop + 1):
            # check if the number is surrounded by . or other digits only
            # check the 4 directions
            # up
            up = (x, y - 1)
            if up in grid:
                up_char = grid[up]
                if up_char == '*':
                    star_nums.setdefault(up, set()).add((x_start, y))

            # down
            down = (x, y + 1)
            if down in grid:
                down_char = grid[down]
                if down_char == '*':
                    star_nums.setdefault(down, set()).add((x_start, y))

            # left
            left = (x - 1, y)
            if left in grid:
                left_char = grid[left]
                if left_char == '*':
                    star_nums.setdefault(left, set()).add((x_start, y))

            # right
            right = (x + 1, y)
            if right in grid:
                right_char = grid[right]
                if right_char == '*':
                    star_nums.setdefault(right, set()).add((x_start, y))

            # check the 4 diagonals
            top_left = (x - 1, y - 1)
            if top_left in grid:
                top_left_char = grid[top_left]
                if top_left_char == '*':
                    star_nums.setdefault(top_left, set()).add((x_start, y))

            top_right = (x + 1, y - 1)
            if top_right in grid:
                top_right_char = grid[top_right]
                if top_right_char == '*':
                    star_nums.setdefault(top_right, set()).add((x_start, y))

            bottom_left = (x - 1, y + 1)
            if bottom_left in grid:
                bottom_left_char = grid[bottom_left]
                if bottom_left_char == '*':
                    star_nums.setdefault(bottom_left, set()).add((x_start, y))

            bottom_right = (x + 1, y + 1)
            if bottom_right in grid:
                bottom_right_char = grid[bottom_right]
                if bottom_right_char == '*':
                    star_nums.setdefault(bottom_right, set()).add((x_start, y))


    gear_ratio_sum = 0

    for nums_coords in star_nums.values():
        numbers = []
        for coord in nums_coords:
            numbers.append(num_coords[coord])

        # check if the star has exactly 2 numbers adjacent to it
        if len(numbers) == 2:
            gear_ratio = int(numbers[0]) * int(numbers[1])
            gear_ratio_sum += gear_ratio

    return gear_ratio_sum


if __name__ == "__main__":
    print("Part 1:", part_1(__file__))
    print("Part 2:", part_2(__file__))
