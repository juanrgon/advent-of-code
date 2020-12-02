from collections import defaultdict


def main():
    print("Part 1 Solution: " + str(_part_1()))
    print("Part 2 Solution: " + str(_part_2()))


def _part_1():
    count = 0
    for n in range(347312, 805915):
        if any(c >= 2 for c in _digit_counts(n).values()) and _all_greater_or_same(n):
            count += 1
    return count


def _part_2():
    count = 0
    for n in range(347312, 805915):
        if any(c == 2 for c in _digit_counts(n).values()) and _all_greater_or_same(n):
            count += 1
    return count

def _digit_counts(n):
    counts = defaultdict(int)
    for d in str(n):
        d = int(d)
        counts[d] += 1
    return counts

def _all_greater_or_same(n):
    previous = -1
    for d in str(n):
        d = int(d)
        if d  < previous:
            return False
        previous = d
    return True

if __name__ == "__main__":
    main()
