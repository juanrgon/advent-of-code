import aoc


@aoc.solution(1)
def part_1(
    raw: aoc.String,
    ints: aoc.Integers,
    strs: list[aoc.String],
    paragraphs: list[aoc.Paragraph],
):
    sums = []
    for i, line in enumerate(strs):
        nums = [int(n) for n in line.split(" ")]
        last_nums = [nums[-1]]
        while not all(n == 0 for n in nums):
            nums = [nums[i + 1] - nums[i] for i in range(len(nums) - 1)]
            last_nums.append(nums[-1])

        sums.append(sum(last_nums))
    return sum(sums)


@aoc.solution(2)
def part_2(
    raw: aoc.String,
    ints: aoc.Integers,
    strs: list[aoc.String],
    paragraphs: list[aoc.Paragraph],
):
    firsts = []
    for i, line in enumerate(strs):
        nums = [int(n) for n in line.split(" ")]
        first_nums = [nums[0]]
        while not all(n == 0 for n in nums):
            nums = [nums[i + 1] - nums[i] for i in range(len(nums) - 1)]
            first_nums.append(nums[0])

        new_first = 0
        for first_num in reversed(first_nums):
            new_first = first_num - new_first
        firsts.append(new_first)

    return sum(firsts)


if __name__ == "__main__":
    print("Part 1:", part_1(__file__))
    print("Part 2:", part_2(__file__))
