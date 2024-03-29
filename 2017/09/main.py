TEST = (
    (r"{}", 1),
    (r"{{{}}}", 6),
    (r"{{},{}}", 5),
    (r"{{{},{},{{}}}}", 16),
    (r"{<a>,<a>,<a>,<a>}", 1),
    (r"{{<ab>},{<ab>},{<ab>},{<ab>}}", 9),
    (r"{{<!!>},{<!!>},{<!!>},{<!!>}}", 9),
    (r"{{<a!>},{<a!>},{<a!>},{<ab>}}", 3),
)


TEST2 = (
    (r"{}", 0),
    (r"{{{}}}", 0),
    (r"{{},{}}", 0),
    (r"{{{},{},{{}}}}", 0),
    (r"{<a>,<a>,<a>,<a>}", 4),
    (r"{{<ab>},{<ab>},{<ab>},{<ab>}}", 8),
    (r"{{<!!>},{<!!>},{<!!>},{<!!>}}", 0),
    (r"{{<a!>},{<a!>},{<a!>},{<ab>}}", 17),
    (r'<{o"i!a,<{i<a>', 10),
)

import re

import aoc
from functools import cache
from pathlib import Path
import string
import subprocess


@aoc.submit(part=1)
@aoc.get_input
@aoc.tests(TEST)
@aoc.parse_text
def part_1(raw: str, ints: list[int], strs: list[str], **kwargs):
    # Handle '!'
    text = re.sub("!.", "", raw)

    # remove all non-bracket characters
    text = text.replace(
        (
            string.ascii_letters.replace("{", "")
            .replace("<", "")
            .replace("}", "")
            .replace(">", "")
        ),
        "",
    )

    text = text.replace(",", '')

    # Handle garbage
    text = re.sub('<[^>]*>', '', text)

    score = 0
    multiplier = 1

    for char in text:
        if char == '{':
            score += multiplier
            multiplier += 1
        elif char == '}':
            multiplier -= 1

    return score


@aoc.submit(part=2)
@aoc.get_input
@aoc.tests(TEST2)
@aoc.parse_text
def part_2(raw: str, ints: list[int], strs: list[str], **kwargs):
    # Handle '!'
    text = re.sub("!.", "", raw)

    # remove all non-bracket characters
    text = text.replace(
        (
            string.ascii_letters.replace("{", "")
            .replace("<", "")
            .replace("}", "")
            .replace(">", "")
        ),
        "",
    )

    # Handle garbage
    return len(text) - len(re.sub('<[^>]*>', '<>', text))



if __name__ == "__main__":
    print("Part 1:", part_1(__file__))
    print("Part 2:", part_2(__file__))
