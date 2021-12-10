TEST = [
    (">", 2),
    ("^>v<", 4),
    ("^v^v^v^v^v", 2),
]

TEST2 = [
    # ("^v", 3),
    ("^>v<", 3),
    ("^v^v^v^v^v", 11),
]


import aoc


@aoc.submit(part=1)
@aoc.load_puzzle
@aoc.tests(TEST)
@aoc.parse_text
def part_1(raw: str, ints: list[int], strs: list[str]):
    p = (0, 0)

    visited = set()
    visited.add(p)

    for c in raw:
        match c:
            case ">":
                p = (p[0] + 1, p[1])
            case "<":
                p = (p[0] - 1, p[1])
            case "^":
                p = (p[0], p[1] + 1)
            case "v":
                p = (p[0], p[1] - 1)
        visited.add(p)

    return len(visited)


@aoc.submit(part=2)
@aoc.load_puzzle
@aoc.tests(TEST2)
@aoc.parse_text
def part_2(raw: str, ints: list[int], strs: list[str]):
    santa = {
        0: (0, 0),
        1:(0, 0),

    }

    visited = set()
    visited.add((0,0))

    for i, c in enumerate(raw):
        p = santa[i % 2]

        match c:
            case ">":
                p = (p[0] + 1, p[1])
            case "<":
                p = (p[0] - 1, p[1])
            case "^":
                p = (p[0], p[1] + 1)
            case "v":
                p = (p[0], p[1] - 1)

        santa[i%2] = p
        visited.add(p)

    return len(visited)


if __name__ == "__main__":
    print("Part 1:", part_1(__file__))
    print("Part 2:", part_2(__file__))
