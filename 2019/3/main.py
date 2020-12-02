import os.path
from collections import namedtuple
from collections import defaultdict
import heapq


def main():
    print("Part 1 Solution: " + str(_part_1()))
    print("Part 2 Solution: " + str(_part_2()))

class Point(object):
    __slots__ = ["x", "y", "moves"]

    def __init__(self, x, y, moves = 0):
        self.x = x
        self.y = y
        self.moves = moves

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def move_up(self):
        return Point(self.x, self.y + 1, self.moves + 1)

    def move_down(self):
        return Point(self.x, self.y - 1, self.moves + 1)

    def move_left(self):
        return Point(self.x - 1, self.y, self.moves + 1)

    def move_right(self):
        return Point(self.x + 1, self.y, self.moves + 1)

def _manhattan_distance_from_start(point):
    return abs(point.x) + abs(point.y)

def _part_1():
    wire_1, wire_2 = _wires()
    wire_1_points, wire_2_points = _points(wire_1), _points(wire_2)
    intersections = wire_1_points & wire_2_points
    return min(_manhattan_distance_from_start(i) for i in intersections)

def _part_2():
    wire_1, wire_2 = _wires()
    wire_1_points = {p: p.moves for p in _points(wire_1)}
    wire_2_points = {p: p.moves for p in _points(wire_2)}

    min_combined_moves = float('inf')
    for point in wire_2_points:
        if point in wire_1_points:
            min_combined_moves = min(min_combined_moves, point.moves + wire_1_points[point])
    return min_combined_moves


def _points(wire):
    position = Point(0, 0)

    points = set()

    for turn in wire:
        direction = turn[0]
        distance = int(turn[1:])

        for i in range(0, distance):
            if direction == 'U':
                position = position.move_up()
            if direction == 'D':
                position = position.move_down()
            if direction == 'L':
                position = position.move_left()
            if direction == 'R':
                position = position.move_right()

            points.add(position)

    return points

def _wires():
    with open(os.path.join(os.path.abspath("."), "wires")) as f:
        return [w.strip().split(',') for w in f.readlines()]

if __name__ == "__main__":
    main()
