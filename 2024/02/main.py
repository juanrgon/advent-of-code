import aoc


@aoc.solution(1)
def part_1(
    raw: aoc.String,
    ints: aoc.Integers,
    strs: list[aoc.String],
    paragraphs: list[aoc.Paragraph],
):
    reports = []

    for line in raw.splitlines():
        reports.append(list(map(int, line.split())))

    safe_count = 0

    for report in reports:
        increasing = False
        decreasing = False
        unsafe = False
        for i in range(len(report) - 1):
            diff = report[i] - report[i + 1]

            if diff > 0:
                decreasing = True
            elif diff < 0:
                increasing = True

            if increasing and decreasing:
                unsafe = True
                break

            if not (increasing or decreasing):
                unsafe = True
                break

            if abs(diff) < 1:
                unsafe = True
                break

            if abs(diff) > 3:
                unsafe = True
                break

        if not unsafe:
            safe_count += 1

    return safe_count


@aoc.solution(2)
def part_2(
    raw: aoc.String,
    ints: aoc.Integers,
    strs: list[aoc.String],
    paragraphs: list[aoc.Paragraph],
):
    reports = []
    for line in raw.splitlines():
        reports.append(list(map(int, line.split())))

    def is_safe(numbers):
        if len(numbers) < 2:
            return False

        increasing = False
        decreasing = False

        for i in range(len(numbers) - 1):
            diff = numbers[i] - numbers[i + 1]

            if diff > 0:
                decreasing = True
            elif diff < 0:
                increasing = True

            if increasing and decreasing:
                return False

            if not (increasing or decreasing):
                return False

            if abs(diff) < 1:
                return False

            if abs(diff) > 3:
                return False

        return True

    safe_count = 0

    for report in reports:
        # Check if safe without removing any number
        if is_safe(report):
            safe_count += 1
            continue

        # Try removing each number one at a time
        for i in range(len(report)):
            modified_report = report[:i] + report[i+1:]
            if is_safe(modified_report):
                safe_count += 1
                break

    return safe_count


if __name__ == "__main__":
    print("Part 1:", part_1(__file__))
    print("Part 2:", part_2(__file__))
