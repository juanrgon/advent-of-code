import os.path



def main():
    print("Solution to Part 1: " + _part_1())
    print("Solution to Part 2: " + _part_2())


def _part_1():
    return str(_trees_hit(_trees(), 3))


def _part_2():
    trees = _trees()

    # HACK
    even_row_trees = [t for i, t in enumerate(trees) if i % 2 == 0]

    return str(
        (_trees_hit(trees, 1))
        * (_trees_hit(trees, 3))
        * (_trees_hit(trees, 5))
        * (_trees_hit(trees, 7))
        * (_trees_hit(even_row_trees, 1))
    )


def _trees_hit(trees, travel_per_row):
    position = 0
    trees_hit = 0
    for row in trees[1:]:
        position += travel_per_row
        if row[position % len(row)] == "#":
            trees_hit += 1
    return trees_hit


def _trees():
    with open(os.path.join(os.path.abspath('.'), 'input')) as f:
        return f.read().splitlines()

if __name__ == "__main__":
    main()
