import os.path
from collections import defaultdict
import re
from itertools import *
from collections import *
from more_itertools import *
from sortedcontainers import *
import sys
from pathlib import Path

YEAR = Path(__file__).parent.parent.name
DAY = Path(__file__).parent.name.lstrip("0")
SESSION = ""


def fst(x):
    return x[0]


def snd(x):
    return x[1]


def ints(text):
    if callable(text):
        text = text()
    return [int(i) for i in re.findall(r"-?\d+", text)]


def min_max(l):
    return min(l), max(l)


def submit(part, answer):
    import requests
    from requests_html import HTML
    response = requests.post(
        f"https://adventofcode.com/{YEAR}/day/{DAY}/answer",
        cookies={"session": SESSION},
        data={"level": part, "answer": answer},
    )
    response.raise_for_status()

    print('\n' + HTML(html=response.text).find('article')[0].full_text)
    if "That's the right answer!" in response.text and part == 1:
        print(f"https://adventofcode.com/{YEAR}/day/{DAY}#part2",)


def main():
    p1 = _part_1()
    p2 = _part_2()
    print("Solution to Part 1: " + str(p1))
    print("Solution to Part 2: " + str(p2))

    if "-1" in sys.argv:
        submit(1, p1)
    elif "-2" in sys.argv:
        submit(2, p2)


def _part_1():
    x = 0
    n = (f())
    for i, d in enumerate(n):
        if d == n[(i + 1) % len(n)]:
            x += int(n[i])
    return x


def _part_2():
    x = 0
    n = (f())
    for i, d in enumerate(n):
        if d == n[int(i + int(len(n)) / 2) % len(n)]:
            x += int(n[i])
    return x



def f():
    if "t" in sys.argv or "-t" in sys.argv and not ('-2' in sys.argv or '-1' in sys.argv):
        name = "test"
    else:
        _download_input()
        name = "input"

    with open(os.path.join(os.path.dirname(__file__), name)) as f:
        return f.read().strip()


def _download_input():
    import requests
    from pathlib import Path

    p = Path(__file__).parent / "input"
    year = Path(__file__).parent.parent.name
    day = Path(__file__).parent.name.lstrip("0")
    if not p.exists():
        response = requests.get(
            f"https://adventofcode.com/{year}/day/{day}/input",
            cookies={"session": SESSION},
        )
        response.raise_for_status()
        p.write_text(response.text)


if __name__ == "__main__":
    main()
