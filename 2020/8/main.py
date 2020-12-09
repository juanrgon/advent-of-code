import os.path
from collections import defaultdict
import __main__
import re
from itertools import *
from collections import *


def main():
    print("Solution to Part 1: " + str(_part_1()))
    print("Solution to Part 2: " + str(_part_2()))


class InfiniteLoopDetected(Exception):
    def __init__(self, msg, accumulator=None):
        self.accumulator = accumulator
        return super(Exception, self).__init__(msg)


def _part_1():
    code = [i for i in _input().splitlines()]
    try:
        _run(code)
    except InfiniteLoopDetected as e:
        return e.accumulator


def _part_2():
    code = [i for i in _input().splitlines()]

    for i, instruction in enumerate(code):
        modified_code = code.copy()
        if instruction.startswith('nop'):
            modified_code[i] = instruction.replace("nop", "jmp")
        elif instruction.startswith('jmp'):
            modified_code[i] = instruction.replace("jmp", "nop")

        try:
            return _run(modified_code)
        except InfiniteLoopDetected:
            continue


def _run(code, return_on_repeat=False):
    index = 0
    acc = 0
    ran = set()

    while True:
        if index >= len(code):
            return acc

        if index in ran:
            raise InfiniteLoopDetected(
                "Infinite loop in code detected", accumulator=acc
            )

        ran.add(index)

        instr = code[index]

        if instr.startswith("acc"):
            index += 1
            acc += int(instr.split()[1])
        if instr.startswith("jmp"):
            index += int(instr.split()[1])
        if instr.startswith("nop"):
            index += 1


def _input():
    with open(os.path.join(os.path.dirname(__file__), "input")) as f:
        return f.read().strip()


if __name__ == "__main__":
    main()
