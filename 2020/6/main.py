import os.path
from collections import Counter, defaultdict
import re
from pathlib import Path
import requests
from itertools import cycle
import __main__



def main():
    print("Solution to Part 1: " + _part_1())
    print("Solution to Part 2: " + _part_2())


def _part_1():
    _input()

    total = 0
    for g in _input().split('\n\n'):
        yes = set()
        for question in g.replace("\n", ''):
            yes.add(question)
        total += len(yes)
    return str(total)


def _part_2():
    _input()

    total = 0
    for group in _input().split('\n\n'):
        all_yes = set()
        for question, count in Counter(group.replace('\n', '')).items():
            if count == len(group.split()):
                all_yes.add(question)
        total += len(all_yes)
    return str(total)


def _input():
    with open(os.path.join(os.path.dirname(__main__.__file__),  'input')) as f:
        return f.read()



if __name__ == "__main__":
    main()
