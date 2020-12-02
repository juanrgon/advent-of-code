import os.path
from collections import defaultdict


def main():
    print("Part 1 Solution: " + str(_part_1()))
    print("Part 2 Solution: " + str(_part_2()))


def _part_1():
    valid = 0
    for entry in _get_input():
        policy, password = entry.split(':')
        password = password.strip()
        _range, letter = policy.split()
        a, b = _range.split('-')
        count = 0
        for l in password:
            if l == letter:
                count += 1
        if int(a) <= count <= int(b):
            valid += 1
    return valid


def _part_2():
    valid = 0
    for entry in _get_input():
        policy, password = entry.split(':')
        password = password.strip()
        _range, letter = policy.split()
        a, b = _range.split('-')
        if (password[int(a) -1 ] == letter) ^ (password[int(b) - 1] == letter):
            valid += 1
    return valid


def _get_input():
    with open(os.path.join(os.path.abspath("."), "input")) as f:
        return f.read().splitlines()

if __name__ == "__main__":
    main()
