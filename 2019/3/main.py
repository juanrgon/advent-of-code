import os.path
from collections import namedtuple
from collections import defaultdict
import time


def main():
    print("Part 1 Solution: " + str(_part_1()))
    print("Part 2 Solution: " + str(_part_2()))


def _part_1():
    wire_1, wire_2 = _wires()
    intersections = set(_points(wire_1)) & set(_points(wire_2))
    return min(abs(p[0]) + abs(p[1]) for p in intersections)


def _part_2():
    wire_1, wire_2 = _wires()
    wire_1_points = _points(wire_1)
    wire_2_points = _points(wire_2)

    min_combined_moves = float("inf")
    for point in wire_1_points:
        if point in wire_2_points:
            min_combined_moves = min(
                min_combined_moves, wire_1_points[point] + wire_2_points[point]
            )
    return min_combined_moves


def _points(wire):
    position = (0, 0)

    points = dict()
    moves = 0

    for turn in wire:
        direction = turn[0]
        distance = int(turn[1:])

        for i in range(0, distance):
            if direction == "U":
                position = position[0] + 0, position[1] + 1
            if direction == "D":
                position = position[0] + 0, position[1] + -1
            if direction == "L":
                position = position[0] + -1, position[1] + 0
            if direction == "R":
                position = position[0] + 1, position[1] + 0

            moves += 1
            points[position] = moves

    return points


def _wires():
    with open(os.path.join(os.path.abspath("."), "wires")) as f:
        return [w.strip().split(",") for w in f.readlines()]


if __name__ == "__main__":
    main()
