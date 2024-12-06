import aoc


@aoc.solution(1)
def part_1(
    raw: aoc.String,
    ints: aoc.Integers,
    strs: list[aoc.String],
    paragraphs: list[aoc.Paragraph],
):
    grid = [list(line.strip()) for line in raw.splitlines() if line.strip()]
    height = len(grid)
    width = len(grid[0])
    count = 0

    directions = [
        (0, 1),  # right
        (1, 0),  # down
        (1, 1),  # diagonal down-right
        (-1, 1),  # diagonal up-right
        (0, -1),  # left
        (-1, 0),  # up
        (-1, -1),  # diagonal up-left
        (1, -1),  # diagonal down-left
    ]

    def is_valid_pos(y: int, x: int) -> bool:
        return 0 <= y < height and 0 <= x < width

    def check_word(y: int, x: int, dy: int, dx: int) -> bool:
        positions = [(y + i * dy, x + i * dx) for i in range(4)]

        # Check if all positions are valid
        if not all(is_valid_pos(py, px) for py, px in positions):
            return False

        # Get the word formed in this direction
        word = ""
        for py, px in positions:
            word += grid[py][px]

        return word == "XMAS"

    # Count all occurrences
    for y in range(height):
        for x in range(width):
            # Only start checking if we find an 'X'
            if grid[y][x] == "X":
                for dy, dx in directions:
                    if check_word(y, x, dy, dx):
                        count += 1

    return count


@aoc.solution(2)
def part_2(
    raw: aoc.String,
    ints: aoc.Integers,
    strs: list[aoc.String],
    paragraphs: list[aoc.Paragraph],
):
    grid = [list(line.strip()) for line in raw.splitlines() if line.strip()]
    height = len(grid)
    width = len(grid[0])
    count = 0

    def is_valid_pos(y: int, x: int) -> bool:
        return 0 <= y < height and 0 <= x < width

    def check_mas(y: int, x: int, dy1: int, dx1: int, dy2: int, dx2: int) -> bool:
        positions = [(y + dy1, x + dx1), (y, x), (y + dy2, x + dx2)]

        # Check if all positions are valid
        if not all(is_valid_pos(py, px) for py, px in positions):
            return False

        # Get the word formed in this direction
        word = ""
        for py, px in positions:
            word += grid[py][px]
        return word in ["MAS", "SAM"]

    # X-shape directions for each arm
    x_shapes = [
        # Upper-right and lower-left arms
        [(-1, 1), (1, -1)],
        # Upper-left and lower-right arms
        [(-1, -1), (1, 1)],
    ]

    total = 0
    # Check every center position
    for y in range(1, height - 1):
        for x in range(1, width - 1):
            if grid[y][x] == "A":  # Center must be 'A'
                count = 0
                for arms in x_shapes:
                    dy1, dx1 = arms[0]
                    dy2, dx2 = arms[1]
                    if check_mas(y, x, dy1, dx1, dy2, dx2):
                        count += 1
                if count > 1:
                    total += 1

    return total


if __name__ == "__main__":
    print("Part 1:", part_1(__file__))
    print("Part 2:", part_2(__file__))
