import os.path
from collections import Counter


def main():
    print("Solution to Part 1: " + str(_part_1()))
    print("Solution to Part 2: " + str(_part_2()))


def _part_1():
    return sum(len(set(g.replace("\n", ""))) for g in _input().split("\n\n"))


def _part_2():
    total = 0
    for group in _input().split("\n\n"):
        all_yes = set()
        for question, count in Counter(group.replace("\n", "")).items():
            if count == len(group.split()):
                all_yes.add(question)
        total += len(all_yes)
    return str(total)


def _input():
    with open(os.path.join(os.path.dirname(__file__), "input")) as f:
        return f.read()


if __name__ == "__main__":
    main()
