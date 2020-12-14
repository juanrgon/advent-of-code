import os.path
import math


def main():
    print("Solution to Part 1: " + str(_part_1()))
    print("Solution to Part 2: " + str(_part_2()))


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, amount):
        return Vector(amount * self.x, amount * self.y)

    def __rmul__(self, amount):
        return Vector(amount * self.x, amount * self.y)

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def __round__(self, ndigits=None):
        return Vector(round(self.x, ndigits), round(self.y, ndigits))

    def __iter__(self):
        return iter((self.x, self.y))

    def manhattan_distance(self, other=None):
        other = other or Vector(0, 0)
        return abs(self.x - other.x) + abs(self.y - other.y)

    def rotate(self, degrees):
        radians = math.pi / 180 * degrees

        # There is a less mathy solution, but I don't care
        c = complex(self.x, self.y) * complex(math.cos(radians), math.sin(radians))
        return Vector(c.real, c.imag)


NORTH = Vector(0, 1)
SOUTH = Vector(0, -1)
EAST = Vector(1, 0)
WEST = Vector(-1, 0)


class Ship:
    def __init__(self, position=None, velocity=None):
        self.position = position or Vector(0, 0)
        self.velocity = velocity or Vector(1, 0)

    def translate(self, direction, amt):
        if direction == "N":
            translation = NORTH
        elif direction == "S":
            translation = SOUTH
        elif direction == "E":
            translation = EAST
        elif direction == "W":
            translation = WEST
        self.position = self.position + amt * translation

    def advance(self, amt):
        self.position = self.position + amt * self.velocity

    def change_course(self, direction, amt):
        if direction == "N":
            self.velocity += amt * NORTH
        elif direction == "S":
            self.velocity += amt * SOUTH
        elif direction == "E":
            self.velocity += amt * EAST
        elif direction == "W":
            self.velocity += amt * WEST


def _part_1():
    s = Ship()
    for inst in f().split():
        a, amt = inst[0], int(inst[1:])
        if a in ("E", "N", "S", "W"):
            s.translate(a, amt)
        elif a == "F":
            s.advance(amt)
        elif a == "L":
            s.velocity = round(s.velocity.rotate(amt))
        elif a == "R":
            s.velocity = round(s.velocity.rotate(-amt))

    return s.position.manhattan_distance()


def _part_2():
    s = Ship(velocity=Vector(10, 1))
    for inst in f().split():
        a, amt = inst[0], int(inst[1:])
        if a in ("E", "N", "S", "W"):
            s.change_course(a, amt)
        elif a == "F":
            s.advance(amt)
        elif a == "L":
            s.velocity = round(s.velocity.rotate(amt))
        elif a == "R":
            s.velocity = round(s.velocity.rotate(-amt))
    return s.position.manhattan_distance()


def f():
    with open(os.path.join(os.path.dirname(__file__), "input")) as f:
        return f.read().strip()


if __name__ == "__main__":
    main()
