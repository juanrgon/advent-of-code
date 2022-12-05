from .script import Script
import re
import html
import sys
import terminology
from functools import cache
from typing import Callable, TypeVar
import aoc.status
import aoc.api

T = TypeVar("T")


def get_input(fn: Callable[[str], T]) -> Callable[[str], T]:
    def fn_override(script_filename) -> T:
        raw = _get_input(script_filename)
        return fn(raw)

    return fn_override


@cache
def _get_input(script_filename: str) -> str:
    """
    Return the puzzle input for the given aoc solution script filepath.

    Uses the folder that the script is in to determine which year and day this script
    is for.

    The assumption is that the scripts are organized in this file structure:

    ├── 2020
    │   ├── 01
    │   │   ├── input
    │   │   └── main.py
    │   └── 02
    │       ├── input
    │       └── main.py
    └── 2021
        ├── 01
        │   ├── input
        │   └── main.py
        └── 02
            ├── input
            └── main.py

    If the puzzle input file is empty, the input will be downloaded if the
    ADVENT_OF_CODE_COOKIE environment variable is set.
    """

    # Use the folder that the script is in to to determine which AOC puzzle we're
    # working on
    script = Script.from_filename(script_filename)

    # create the puzzle file if it doesn't already exist
    script.input_file.touch(exist_ok=True)

    _download_prompt(script)

    input, downloaded = _download_input(script)
    if downloaded:
        print(terminology.in_cyan(f"\nSee the prompt at {script.prompt_url}"))
        sys.exit(0)
    return input

def _download_prompt(script):
    # Create prompt file if it doesn't already exist
    script.prompt_file.touch(exist_ok=True)

    if "Part Two" not in script.prompt_file.read_text().strip():
        response = aoc.api.get(script.prompt_url)

        html = "\n\n".join([a.html for a in response.html.find("article")])
        if not html:
            print("Failed to download prompt!")

        print(f"Downloaded prompt to {str(script.prompt_file)}")
        script.prompt_file.write_text(_html_to_markdown(html))


def _download_input(script) -> tuple[str, bool]:
    downloaded = False
    # If puzzle input file is empty...
    if not (script_content := script.input_file.read_text()):
        import pendulum  # pendulum is also slow to import

        puzzle_start = pendulum.datetime(
            int(script.year), 12, int(script.day), 0, 0, 0, tz="US/Eastern"
        )

        if pendulum.now() < puzzle_start:
            raise RuntimeError(f"Too early for {script.year} Day {script.day}")

        # download the input
        response = aoc.api.get(script.puzzle_url)
        response.raise_for_status()
        script.input_file.write_text(response.text)
        print(f"Downloaded input to {str(script.input_file)}")
        downloaded = True

    return script_content, downloaded


def _html_to_markdown(_html):
    _html = re.sub("<p>(?P<text>.*?)</p>", "\n\g<text>\n", _html)
    _html = re.sub("<em>(?P<text>.*?)</em>", "**\g<text>**", _html)
    _html = _html.replace("<ul>", "")
    _html = _html.replace("</ul>", "")
    _html = re.sub("<li>(?P<text>.*?)</li>", "- \g<text>", _html)
    _html = re.sub("<code>(?P<text>.*?)</code>", "`\g<text>`", _html)
    _html = re.sub("<h2.*?>(?P<text>.*?)</h2>", "## \g<text>\n\n", _html)
    _html = re.sub("<span .*?>(?P<text>.*?)</span>", "\g<text>", _html)
    _html = re.sub(
        "<pre><code>(?P<code>.*?)</code></pre>",
        "\n```\n\g<code>```\n",
        _html,
        flags=re.DOTALL,
    )
    _html = html.unescape(_html)
    _html = re.sub("<article .*?>", "", _html)
    _html = re.sub("</article>", "", _html)
    _html = _html.replace("\n\n", "\n").strip()
    return _html
