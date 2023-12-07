from __future__ import annotations
import aoc
import math


@aoc.solution(1)
def part_1(
    raw: aoc.String,
    ints: aoc.Integers,
    strs: list[aoc.String],
    paragraphs: list[aoc.Paragraph],
):
    times, record_distances = strs

    times = [int(n) for n in times.split()[1:] if n]
    record_distances = [int(n) for n in record_distances.split()[1:] if n]

    all_ways = []
    for time, record_distance in zip(times, record_distances):
        ways = 0
        for i in range(time):
            speed = i
            time_remaining = time - i
            total_distance = time_remaining * speed
            if total_distance > record_distance:
                ways += 1

        all_ways.append(ways)

    return math.prod(all_ways)


@aoc.solution(2)
def part_2(
    raw: aoc.String,
    ints: aoc.Integers,
    strs: list[aoc.String],
    paragraphs: list[aoc.Paragraph],
):
    times, record_distances = strs

    time = int(''.join(times.split()[1:]))
    record = int(''.join(record_distances.split()[1:]))

    all_ways = []
    ways = 0
    for i in range(time):
        speed = i
        time_remaining = time - i
        total_distance = time_remaining * speed
        if total_distance > record:
            ways += 1

    all_ways.append(ways)

    return math.prod(all_ways)


if __name__ == "__main__":
    print("Part 1:", part_1(__file__))
    print("Part 2:", part_2(__file__))
