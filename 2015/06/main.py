from __future__ import annotations

TEST = [
    (
        """
turn on 0,0 through 999,999
toggle 0,0 through 999,0
turn off 499,499 through 500,500
""",
        1_000_000 - 1000 - 4,
    ),
]

TEST2 = [
    (
        """
turn on 0,0 through 0,0
toggle 0,0 through 999,999
""",
        1 + 2_000_000,
    ),
]


from re import sub
import aoc
from collections import defaultdict
import attr


@attr.define
class Light:
    brightness: int = 0

    @classmethod
    def turn_on_1(cls, light: Light):
        light.brightness = max(light.brightness + 1, 1)


    @classmethod
    def turn_off_1(cls, light: Light):
        light.brightness = min(light.brightness - 1, 0)

    @classmethod
    def toggle_1(cls, light: Light):
        light.brightness = 0 if light.brightness else 1

    @classmethod
    def turn_on_2(cls, light: Light):
        light.brightness += 1

    @classmethod
    def turn_off_2(cls, light: Light):
        light.brightness = max(light.brightness - 1, 0)

    @classmethod
    def toggle_2(cls, light: Light):
        light.brightness += 2


@aoc.submit(part=1)
@aoc.get_input
@aoc.tests(TEST)
@aoc.parse_text
def part_1(raw: str, ints: list[int], strs: list[str]):

    grid = aoc.Grid.of(Light, height=1000, width=1000)

    for line in strs:
        line, b = line.split(" through ")
        inst, a = line.rsplit(" ", 1)

        subgrid = grid.subgrid(aoc.ints(a.split(",")), aoc.ints(b.split(",")))

        match inst:
            case "turn on":
                subgrid.for_each(Light.turn_on_1)
            case "turn off":
                subgrid.for_each(Light.turn_off_1)
            case "toggle":
                subgrid.for_each(Light.toggle_1)

    return sum([l.brightness for l in grid.values()])


@aoc.submit(part=2)
@aoc.get_input
@aoc.tests(TEST2)
@aoc.parse_text
def part_2(raw: str, ints: list[int], strs: list[str]):
    grid = aoc.Grid.of(Light, height=1000, width=1000)

    for line in strs:
        line, b = line.split(" through ")
        inst, a = line.rsplit(" ", 1)

        subgrid = grid.subgrid(aoc.ints(a.split(",")), aoc.ints(b.split(",")))

        match inst:
            case "turn on":
                subgrid.for_each(Light.turn_on_2)
            case "turn off":
                subgrid.for_each(Light.turn_off_2)
            case "toggle":
                subgrid.for_each(Light.toggle_2)


    return sum([l.brightness for l in grid.values()])


if __name__ == "__main__":
    print("Part 1:", part_1(__file__))
    print("Part 2:", part_2(__file__))
