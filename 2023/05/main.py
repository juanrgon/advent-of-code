from __future__ import annotations
import aoc


@aoc.solution(1)
def part_1(
    raw: aoc.String,
    ints: aoc.Integers,
    strs: list[aoc.String],
    paragraphs: list[aoc.Paragraph],
):
    def get_map(lines):
        maps = []
        for line in paragraph[1:]:
            dest, src, range = [int(n) for n in line.split(" ")]

            def _get_map(dest, src, range):
                def map(n):
                    if n >= src and n < src + range:
                        return dest + (n - src)

                    return n

                return map

            maps.append(_get_map(dest, src, range))

        def _map(dest):
            for map in maps:
                new = map(dest)
                if new != dest:
                    return new

            return dest

        return _map

    maps = []
    for paragraph in paragraphs:
        if paragraph[0].startswith("seeds"):
            seeds = paragraph[0].split(" ")[1:]

        if paragraph[0] == ("seed-to-soil map:"):
            maps.append(get_map(paragraph[1:]))

        if paragraph[0] == ("soil-to-fertilizer map:"):
            maps.append(get_map(paragraph[1:]))

        if paragraph[0] == ("fertilizer-to-water map:"):
            maps.append(get_map(paragraph[1:]))

        if paragraph[0] == ("water-to-light map:"):
            maps.append(get_map(paragraph[1:]))

        if paragraph[0] == ("light-to-temperature map:"):
            maps.append(get_map(paragraph[1:]))

        if paragraph[0] == ("temperature-to-humidity map:"):
            maps.append(get_map(paragraph[1:]))

        if paragraph[0] == ("humidity-to-location map:"):
            maps.append(get_map(paragraph[1:]))

    lowest = None
    for seed in seeds:
        seed = int(seed)
        for map in maps:
            seed = map(seed)

        if lowest is None or seed < lowest:
            lowest = seed

    return lowest


@aoc.solution(2)
def part_2(
    raw: aoc.String,
    ints: aoc.Integers,
    strs: list[aoc.String],
    paragraphs: list[aoc.Paragraph],
):
    def get_map(lines):
        maps = []
        for line in paragraph[1:]:
            src, dest, range = [int(n) for n in line.split(" ")]

            def _get_map(dest, src, range):
                def map(n):
                    if n >= src and n < src + range:
                        return dest + (n - src)

                    return n

                return map

            maps.append(_get_map(dest, src, range))

        def _map(dest):
            for map in maps:
                new = map(dest)
                if new != dest:
                    return new

            return dest

        return _map

    maps = []
    for paragraph in paragraphs:
        if paragraph[0].startswith("seeds"):
            seed_ranges = paragraph[0].split(" ")[1:]
            seeds = []
            for k in range(len(seed_ranges) // 2):
                seeds.append(
                    [
                        int(seed_ranges[k * 2]),
                        int(seed_ranges[k * 2 + 1]) + int(seed_ranges[k * 2]),
                    ]
                )

        if paragraph[0] == ("seed-to-soil map:"):
            maps.append(get_map(paragraph[1:]))

        if paragraph[0] == ("soil-to-fertilizer map:"):
            maps.append(get_map(paragraph[1:]))

        if paragraph[0] == ("fertilizer-to-water map:"):
            maps.append(get_map(paragraph[1:]))

        if paragraph[0] == ("water-to-light map:"):
            maps.append(get_map(paragraph[1:]))

        if paragraph[0] == ("light-to-temperature map:"):
            maps.append(get_map(paragraph[1:]))

        if paragraph[0] == ("temperature-to-humidity map:"):
            maps.append(get_map(paragraph[1:]))

        if paragraph[0] == ("humidity-to-location map:"):
            maps.append(get_map(paragraph[1:]))

            all_locations = []
            for l in paragraph[1:]:
                locations = [int(n) for n in l.split(" ")]
                for i in range(locations[0], locations[0] + locations[2]):
                    all_locations.append(i)
            all_locations.sort()

    for seed in all_locations:
        location = seed
        seed = int(seed)
        for map in reversed(maps):
            seed = map(seed)

        for seed_range in seeds:
            if seed >= seed_range[0] and seed < seed_range[1]:
                return location


if __name__ == "__main__":
    print("Part 1:", part_1(__file__))
    print("Part 2:", part_2(__file__))
