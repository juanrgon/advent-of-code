import os.path
from collections import defaultdict
import re


def main():
    print("Solution to Part 1: " + str(_part_1()))
    print("Solution to Part 2: " + str(_part_2()))


class Bag:
    def __init__(self):
        self.subbags = dict()

    def contains(self, target):
        for bag in self.subbags:
            if bag == target or bag.contains(target):
                return True
        return False

    def total_subbags(self):
        total = 0
        for bag, count in self.subbags.items():
            total += count + count * bag.total_subbags()
        return total


def _part_1():
    bags = _bags()
    shiny_gold_bag = bags['shiny gold']
    return len([b for b in bags.values() if b.contains(shiny_gold_bag)])


def _part_2():
    bags = _bags()
    return bags["shiny gold"].total_subbags()


def _bags():
    bags = defaultdict(Bag)
    for i in _input().split(".\n"):
        color, contains = i.split(' bags contain ')
        bag = bags[color]
        for desc in contains.split(", "):
            match = re.match(r"(\d) (.*) bags?", desc)
            if not match:
                continue

            count = int(match.group(1))
            color = match.group(2)

            bag.subbags[bags[color]] = count
    return bags


def _input():
    with open(os.path.join(os.path.dirname(__file__), "input")) as f:
        return f.read().strip()


if __name__ == "__main__":
    main()
