import os.path
from functools import lru_cache
from collections import Counter


def main():
    print("Solution to Part 1: " + str(_part_1()))
    print("Solution to Part 2: " + str(_part_2()))


def _part_1():
    nums = [int(i) for i in _input().split()]
    nums.append(max(nums) + 3)

    diffs = Counter()
    prev = 0
    for i in sorted(nums):
        diffs.update([i - prev])
        prev = i

    return diffs[1] * diffs[3]


def _part_2():
    nums = [int(i) for i in _input().split()]
    nums.append(0)
    nums.append(max(nums) + 3)
    return chains(tuple(sorted(nums)))


@lru_cache()
def chains(nums):
    if len(nums) == 1:
        return 1

    count = 0
    for i in range(1, len(nums)):
        if nums[i] - nums[0] <= 3:
            count += chains(tuple(nums[i:]))
        else:
            break
    return count


def _input():
    with open(os.path.join(os.path.dirname(__file__), "input")) as f:
        return f.read().strip()


if __name__ == "__main__":
    main()
