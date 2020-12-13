import os.path
from functools import reduce


def main():
    print("Solution to Part 1: " + str(_part_1()))
    print("Solution to Part 2: " + str(_part_2()))


def _part_1():
    earliest, ids = f().splitlines()
    earliest = int(earliest)

    ids = [int(i) for i in ids.split(",") if i != "x"]

    best_id = None
    best_time = float("inf")
    for i in ids:
        prev = best_time
        best_time = min(int((earliest + i) / i) * i, best_time)
        if best_time != prev:
            best_id = i
    return best_id * (best_time - earliest)


def crt(divisors, remainders):
    # See https://brilliant.org/wiki/chinese-remainder-theorem/
    a = remainders
    n = divisors

    N = reduce(lambda a, b: a * b, n)
    y = [round(N / ni) for ni in n]
    z = [pow(yi, -1, ni) for yi, ni in zip(y, n)]  # pow(yi, -1, ni) only works in 3.8

    return sum([a * y * z for a, y, z in zip(a, y, z)]) % N


def _part_2():
    _, ids = f().splitlines()

    divisors = []
    remainders = []
    for i, num in enumerate(ids.split(",")):
        if num == "x":
            continue
        num = int(num)
        divisors.append(num)
        remainders.append(num - i)

    return crt(divisors, remainders)


def f():
    with open(os.path.join(os.path.dirname(__file__), "input")) as f:
        return f.read().strip()


if __name__ == "__main__":
    main()
