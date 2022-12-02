TEST = [
    (
        """
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
""",
        26397,
    ),
]

TEST2 = [
    (
        """
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
""",
        288957,
    ),
]


import aoc


@aoc.submit(part=1)
@aoc.get_input
@aoc.tests(TEST)
@aoc.parse_text
def part_1(raw: str, ints: list[int], strs: list[str], **kwargs):
    total = 0
    for s in strs:
        total += score(s)[0]
    return total


@aoc.submit(part=2)
@aoc.get_input
@aoc.tests(TEST2)
@aoc.parse_text
def part_2(raw: str, ints: list[int], strs: list[str], **kwargs):
    scores = []

    for s in strs:
        match score(s):
            case 0, opened:
                scores.append(complete(opened))

    return sorted(scores)[int(len(scores) / 2)]


def score(s):
    open = ""

    chars = {
        "}": "{",
        "]": "[",
        ")": "(",
        ">": "<",
    }

    for c in s:
        last_open = open[-1] if open else ""

        if closer := chars.get(c):
            if closer != last_open:
                match c:
                    case ")":
                        return 3, open
                    case "]":
                        return 57, open
                    case "}":
                        return 1197, open
                    case ">":
                        return 25137, open
            else:
                open = open[:-1]
        else:
            open += c

    return 0, open


def complete(s):
    opens = {
        "{": "}",
        "[": "]",
        "(": ")",
        "<": ">",
    }

    score = 0

    for c in reversed(s):
        if closer:= opens.get(c):
            score *= 5
            match closer:
                case ")":
                    score += 1
                case "]":
                    score += 2
                case "}":
                    score += 3
                case ">":
                    score += 4
        else:
            return score

    return score


if __name__ == "__main__":
    print("Part 1:", part_1(__file__))
    print("Part 2:", part_2(__file__))
