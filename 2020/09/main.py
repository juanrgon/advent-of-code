import os.path
from itertools import combinations


def main():
    print("Solution to Part 1: " + str(_part_1()))
    print("Solution to Part 2: " + str(_part_2()))


def _part_1():
    nums = [int(i) for i in _input().split()]

    last_25 = nums[:25]
    nums = nums[25:]
    for num in nums:
        for pair in combinations(last_25, 2):
            if sum(pair) == num:
                break
        else:
            return num

        last_25 = last_25[1:] + [num]


def _part_2():
    nums = [int(i) for i in _input().split()]
    part_1 = _part_1()
    for a, b in combinations(range(len(nums)), 2):
        if sum(nums[a:b]) == part_1:
            return min(nums[a:b]) + max(nums[a:b])


def _input():
    with open(os.path.join(os.path.dirname(__file__), "input")) as f:
        return f.read().strip()


if __name__ == "__main__":
    main()
