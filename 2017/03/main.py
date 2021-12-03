TEST = (
    ("1", 0),
    ("12", 3),
    ("13", 4),
    ("23", 2),
    ("25", 4),
    ("1024", 31),
)

TEST2 = (
    ("1", 2),
    ("12", 23),
    ("23", 25),
    ("800", 806),
)

import sys
from pathlib import Path
from typing import List
import math

# import local AOC lib
sys.path.append(str(Path(__file__).parent.parent.parent))
import aoc


@aoc.tests(TEST)
@aoc.parse_text
def part_1(raw: str, ints: List[int], strs: List[str]):
    """
    Visual representation of this solution:

    let s be the square root of the next perfect square greater then or equal to x

    i.e. s = ceil(sqrt(x))

    17  16  15  14  13             3   1   0   3   2                 0  2  1  0  3              4  3  2  3  4
    18   5   4   3  12   x+1 % s   4   0   1   0   1    x + 1 % p    1  0  1  0  2              3  2  1  2  3
    19   6   1   2  11   ------>   0   1   0   1   0   ---------->   2  1  0  1  1              2  1  0  1  2
    20   7   8   9  10             1   2   0   1   3                 3  2  1  0  0              3  2  1  2  3
    21  22  23  24  25             2   3   4   0   1                 0  1  2  3  0              4  3  2  3  4

    WHY DOES THIS WORK???

    Consider a square of numbers in this spiral, with bottom-right number S, along with
    the outer top-right band of numbers (R0 -> Ri) and the bottom-left band of numbers
    (L0 -> Lj) that surround the inner square:

    L0  Ri  <-   .   .
    L1   .   .   .   .
    .    .   .   .  R1
    .    .   .   S  R0
    .    .   .  ->  Lj

    It should be easy to see that S is always a square number, since it is the largest
    number in it's inner-square.

    Define s = sqrt(S)

    """

    x = int(raw)
    s = math.ceil(math.sqrt(x))

    # arm_root = math.sqrt(num)
    # arm_root = int(arm_root) + math.ceil(arm_root % 1)
    # if arm_root %2 == 0:
    #     arm_root += 1

    # For any arm, the manhattan distance for the numbers in the arm repeats every (root -1)
    # number of digits.
    #
    # e.g. the numbers 10-25 are in the third arm of the spiral, and the highest square
    #      root in this spiral is 5, for the number 25. In this arm the manhattan dist.
    #      goes, 4 3 2 3 4 3 2 3 4, etc. repeating every 5th term.

    m = int((x - 1) % s)
    return abs(m -int(s/2)) + int(s / 2)


@aoc.tests(TEST2)
@aoc.parse_text
def part_2(raw: str, ints: List[int], strs: List[str]):
    target = int(raw)

    # construct grid of numbers
    # logically grid has to be less than sqrt()


if __name__ == "__main__":
    puzzle = (Path(__file__).parent / "input").read_text().strip()

    part_1.test()
    print("Part 1:", part_1(puzzle))

    # part_2.test()
    # print("Part 2:", part_2(puzzle))
