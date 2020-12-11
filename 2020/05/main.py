import __main__
import os.path


def main():
    print("Solution to Part 1: " + _part_1())
    print("Solution to Part 2: " + _part_2())


def _part_1():
    highest_seat = float('-inf')
    for seat in _input().split():
        row = int(''.join(['1' if p == 'B' else '0' for p in seat[:-3]]), 2)
        col = int(''.join(['1' if p == 'R' else '0' for p in seat[-3:]]), 2)
        highest_seat = max(highest_seat, row * 8 + col)
    return str(highest_seat)


def _part_2():
    h = float('-inf')
    seats = []
    for seat in _input().split():
        row = int(''.join(['1' if p == 'B' else '0' for p in seat[:-3]]), 2)
        col = int(''.join(['1' if p == 'R' else '0' for p in seat[-3:]]), 2)
        seats.append(row * 8 + col)

    previous = None
    for seat in sorted(seats):
        if previous is None:
            previous = seat
            continue

        if seat == previous + 2:
            return str(seat - 1)
        previous = seat

    return str(h)



def _input():
    with open(os.path.join(os.path.dirname(__main__.__file__),  'input')) as f:
        return f.read()


if __name__ == "__main__":
    main()
