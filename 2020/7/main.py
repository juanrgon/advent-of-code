import os.path
from collections import defaultdict
import __main__
import re


def main():
    print("Solution to Part 1: " + str(_part_1()))
    print("Solution to Part 2: " + str(_part_2()))


class Bag:
    def __init__(self):
        self.subbags = defaultdict(Bag)

    def contains(self, target):
        for bag in self.subbags:
            if bag == target:
                return True
            elif bag.contains(target):
                return True

        return False

    def total_subbags(self):
        total = 0
        for bag, count in self.subbags.items():
            total += count + count * bag.total_subbags()
        return total


def _part_1():
    bags = _bags()
    total = 0
    for b in bags.values():
        if b.contains(bags["shiny gold"]):
            total += 1
    return total


def _part_2():
    bags = _bags()
    return bags["shiny gold"].total_subbags()


def _bags():
    bags = defaultdict(Bag)
    for i in _input().split(".\n")[:-1]:
        bag, contains = i.split(" bags contain ")
        for desc in contains.split(", "):
            if desc == "no other bags":
                continue

            match = re.match("(\d) (.*) bags?", desc)
            count = match.group(1)
            color = match.group(2)
            bags[bag].subbags[bags[color]] = int(count)
    return bags


def _input():
    with open(os.path.join(os.path.dirname(__main__.__file__), "input")) as f:
        return f.read()


if __name__ == "__main__":
    main()
