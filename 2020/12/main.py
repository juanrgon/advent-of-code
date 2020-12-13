import os.path
import re
import math


def main():
    print("Solution to Part 1: " + str(_part_1()))
    print("Solution to Part 2: " + str(_part_2()))


class Ship:
    def __init__(self, position):
        self.position = position
        self.facing = "E"

    def move(self, direction, amt):
        self.facing, previous_direction = direction, self.facing
        self.advance(amt)
        self.facing = previous_direction

    def advance(self, amt):
        if self.facing == "E":
            self.position = (self.position[0] + amt, self.position[1])
        elif self.facing == "N":
            self.position = (self.position[0], self.position[1] + amt)
        elif self.facing == "S":
            self.position = (self.position[0], self.position[1] - amt)
        elif self.facing == "W":
            self.position = (self.position[0] - amt, self.position[1])

    def left(self, deg):
        turns = int(deg / 90)

        for turn in range(turns):
            if self.facing == "E":
                self.facing = "N"
            elif self.facing == "N":
                self.facing = "W"
            elif self.facing == "W":
                self.facing = "S"
            elif self.facing == "S":
                self.facing = "E"

    def right(self, deg):
        turns = int(deg / 90)

        for turn in range(turns):
            if self.facing == "E":
                self.facing = "S"
            elif self.facing == "S":
                self.facing = "W"
            elif self.facing == "W":
                self.facing = "N"
            elif self.facing == "N":
                self.facing = "E"


def manhattan_distance(a, b=(0, 0)):
    return abs(a[0] - b[0]) + abs(a[1] - b[0])


class Follower:
    def __init__(self, waypoint):
        self.position = (0, 0)
        self.waypoint = waypoint

    def advance(self, times=1):
        for i in range(times):
            x, y = self.position
            wx, wy = self.waypoint.position
            dx, dy = wx - x, wy - y

            self.position = wx, wy
            self.waypoint.position = wx + dx, wy + dy

    def rotate_waypoint(self, degrees):
        x, y = rotate_point(
            point=self.waypoint.position, degrees=degrees, center=self.position
        )
        self.waypoint.position = round(x), round(y)


def rotate_point(point, degrees, center=(0, 0)):
    radians = math.pi / 180 * degrees

    px, py = point
    cx, cy = center
    dx, dy = px - cx, py - cy

    # There is a less mathy solution, but I don't care
    c = complex(dx, dy) * complex(math.cos(radians), math.sin(radians))
    new_dx, new_dy = c.real, c.imag

    return cx + new_dx, cy + new_dy


def _part_1():
    s = Ship((0, 0))
    for inst in f().split():
        a, amt = inst[0], int(inst[1:])
        if a in ("E", "N", "S", "W"):
            s.move(a, amt)
        elif a == "F":
            s.advance(amt)
        elif a == "L":
            s.left(amt)
        elif a == "R":
            s.right(amt)

    return manhattan_distance(s.position)


def _part_2():
    s = Follower(waypoint=Ship((10, 1)))
    for inst in f().split():
        a, amt = inst[0], int(inst[1:])
        if a in ("E", "N", "S", "W"):
            s.waypoint.move(a, amt)
        elif a == "L":
            s.rotate_waypoint(amt)
        elif a == "R":
            s.rotate_waypoint(-amt)
        elif a == "F":
            s.advance(amt)
    return manhattan_distance(s.position)


def f():
    with open(os.path.join(os.path.dirname(__file__), "input")) as f:
        return f.read().strip()


if __name__ == "__main__":
    main()
