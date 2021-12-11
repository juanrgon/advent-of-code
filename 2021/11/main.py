from __future__ import annotations
import aoc
import attr
import itertools
import terminology


# fmt: off
TESTS_1 = [
("""
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
""", 1656),
]

TESTS_2 = [
("""
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
""", 195),
]
# fmt: on


@attr.define
class Octopus:
    energy: int
    flashing: bool = False

    @classmethod
    def from_str(cls, s) -> Octopus:
        return cls(energy=int(s))

    def flash(self):
        self.flashing = True

    def one_up(self):
        self.energy += 1

    def reset(self):
        if self.flashing:
            self.energy = 0

        self.flashing = False

    def __str__(self):
        return terminology.in_green(0) if self.flashing else str(self.energy)

    def __repr__(self):
        return f"*{0}*" if self.flashing else str(f" {self.energy} ")


@aoc.submit(part=1)
@aoc.get_input
@aoc.tests(TESTS_1)
@aoc.parse_text
def part_1(raw: str, ints: list[int], strs: list[str]):
    octos = aoc.Grid.from_str(raw, init=Octopus.from_str)

    steps = 100

    flashes = 0
    for step in range(steps):
        # First, the energy level of each octopus increases by 1
        for octo in octos.values():
            octo.one_up()

        flashed = set()
        while True:
            new = 0
            for coord, octo in octos.items():

                if octo.energy > 9 and coord not in flashed:
                    octo.flash()
                    flashed.add(coord)
                    new += 1
                    flashes += 1

                    for _, neighbor in octos.neighbors(coord).items():
                        neighbor.one_up()

            if not new:
                break

        for octo in octos.values():
            octo.reset()

    return flashes


@aoc.submit(part=2)
@aoc.get_input
@aoc.tests(TESTS_2)
@aoc.parse_text
def part_2(raw: str, ints: list[int], strs: list[str]):
    octos = aoc.Grid.from_str(raw, init=Octopus.from_str)

    steps = 100000

    flashes = 0
    for step in itertools.count():
        # First, the energy level of each octopus increases by 1
        for octo in octos.values():
            octo.one_up()

        flashed = set()
        while True:
            new = 0
            for coord, octo in octos.items():

                if octo.energy > 9 and coord not in flashed:
                    octo.flash()
                    flashed.add(coord)
                    new += 1
                    flashes += 1

                    for _, neighbor in octos.neighbors(coord).items():
                        neighbor.one_up()

            if not new:
                break

        if all(octo.flashing for octo in octos.values()):
            return step + 1

        for octo in octos.values():
            octo.reset()



if __name__ == "__main__":
    print("Part 1:", part_1(__file__))
    print("Part 2:", part_2(__file__))
