import os.path


def main():
    print("Part 1 Solution: " + str(_part_1()))
    print("Part 2 Solution: " + str(_part_2()))


def _part_1():
    return sum([int(int(m) / 3) - 2 for m in _masses()])


def _part_2():
    return sum([_required_fuel(m) for m in _masses()])


def _required_fuel(mass):
    fuel = max(int(int(mass) / 3) - 2, 0)

    if fuel == 0:
        return fuel

    return fuel + _required_fuel(fuel)


def _masses():
    with open(os.path.join(os.path.abspath("."), "masses")) as f:
        masses = f.read().splitlines()

    return masses


if __name__ == "__main__":
    main()
