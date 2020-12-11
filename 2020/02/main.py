import os.path
import re
from collections import defaultdict, Counter


def main():
    print("Part 1 Solution: " + str(_part_1()))
    print("Part 2 Solution: " + str(_part_2()))


def _part_1():
    valid = 0
    for entry in _get_input():
        a, b, letter, password = _multisplit(entry, '-', ': ', ' ')

        counts = Counter(password)

        if int(a) <= counts[letter] <= int(b):
            valid += 1

    return valid


def _part_2():
    valid = 0
    for entry in _get_input():
        a, b, letter, password = _multisplit(entry, '-', ': ', ' ')

        if (password[int(a) - 1] == letter) ^ (password[int(b) - 1] == letter):
            valid += 1

    return valid


def _get_input():
    with open(os.path.join(os.path.abspath("."), "input")) as f:
        return f.read().splitlines()


def _multisplit(string, *delimiters):
    return re.split("|".join([re.escape(d) for d in delimiters]), string)


if __name__ == "__main__":
    main()
