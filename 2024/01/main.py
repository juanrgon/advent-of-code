import aoc


@aoc.solution(1)
def part_1(
    raw: aoc.String,
    ints: aoc.Integers,
    strs: list[aoc.String],
    paragraphs: list[aoc.Paragraph],
):
    left = []
    right = []

    for line in raw.splitlines():
        left.append(int(line.split()[0]))
        right.append(int(line.split()[1]))

    left = sorted(left)
    right = sorted(right)

    diffs = []
    for i, j in zip(left, right):
        diffs.append(abs(j - i))

    return sum(diffs)


@aoc.solution(2)
def part_2(
    raw: aoc.String,
    ints: aoc.Integers,
    strs: list[aoc.String],
    paragraphs: list[aoc.Paragraph],
):
    left = []
    right = []

    for line in raw.splitlines():
        left.append(int(line.split()[0]))
        right.append(int(line.split()[1]))

    ans = 0
    for i in left:
        # get the count of i in right
        count = right.count(i)
        ans += count * i

    return ans


if __name__ == "__main__":
    print("Part 1:", part_1(__file__))
    print("Part 2:", part_2(__file__))
