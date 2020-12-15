import os.path
from collections import defaultdict
import re
import sys



def ints(text):
    if callable(text):
        text = text()
    return [int(i) for i in re.findall(r"\d+", text)]



def main():
    print("Solution to Part 1: " + str(_part_1()))
    print("Solution to Part 2: " + str(_part_2()))


def _part_1():
    nums = ints(f)

    turn = {n: i + 1 for i, n in enumerate(nums)}

    for i in range(len(nums), 2020):
        nums.append(i - turn.get(nums[-1], i))
        turn[nums[-2]] = i

    return nums[-1]


def _part_2():
    nums = ints(f)

    turn = {n: i + 1 for i, n in enumerate(nums)}

    s2, s1 = nums[-2], nums[-1]
    for i in range(len(nums), 30000000):
        s2, s1 = s1, i - turn.get(s1, i)
        turn[s2] = i

    return s1


def f():
    if "t" in sys.argv or "-t" in sys.argv:
        name = "test"
    else:
        name = "input"

    with open(os.path.join(os.path.dirname(__file__), name)) as f:
        return f.read().strip()


if __name__ == "__main__":
    main()
