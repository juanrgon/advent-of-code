import aoc
import itertools
from operator import add, mul


@aoc.solution(1)
def part_1(
    raw: aoc.String,
    ints: aoc.Integers,
    strs: list[aoc.String],
    paragraphs: list[aoc.Paragraph],
):
    tests = {}
    for line in raw.splitlines():
        test, numbers_string = line.split(":")
        numbers = [int(n) for n in numbers_string.split()]
        tests[int(test)] = numbers

    ops_list = [add, mul]

    total = 0
    for test, numbers in tests.items():
        for ops in itertools.product(ops_list, repeat=len(numbers) - 1):
            result = numbers[0]
            for i, op in enumerate(ops):
                result = op(result, numbers[i + 1])

            if result == test:
                total += test
                break

    return total


@aoc.solution(2)
def part_2(
    raw: aoc.String,
    ints: aoc.Integers,
    strs: list[aoc.String],
    paragraphs: list[aoc.Paragraph],
):
    tests = {}
    for line in raw.splitlines():
        test, numbers_string = line.split(":")
        numbers = [int(n) for n in numbers_string.split()]
        tests[int(test)] = numbers

    def concat(a, b):
        return int(str(a) + str(b))

    ops_list = [add, mul, concat]

    total = 0
    for test, numbers in tests.items():
        for ops in itertools.product(ops_list, repeat=len(numbers) - 1):
            result = numbers[0]
            for i, op in enumerate(ops):
                result = op(result, numbers[i + 1])

            if result == test:
                total += test
                break

    return total


if __name__ == "__main__":
    print("Part 1:", part_1(__file__))
    print("Part 2:", part_2(__file__))
