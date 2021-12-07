from .aoc_token import aoc_token
from .script import Script
from datetime import datetime
import requests_html
import pendulum
import re
import html


def get_puzzle(script_filename: str) -> str:
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
    script.puzzle_file.touch(exist_ok=True)

    session = requests_html.HTMLSession()

    # If puzzle input file is empty...
    if not script.puzzle_file.read_text().strip():
        puzzle_start = pendulum.datetime(
            int(script.year), 12, int(script.day), 0, 0, 0, tz="US/Eastern"
        )

        if pendulum.now() < puzzle_start:
            raise RuntimeError(f"Too early for {script.year} Day {script.day}")

        # ...download the puzzle if the AOC session token is set in env vars
        if aoc_token():
            response = session.get(
                script.puzzle_url,
                cookies={"session": aoc_token()},
            )

            try:
                response.raise_for_status()
            except Exception as e:
                raise RuntimeError(f"Failed to download {script.puzzle_url}") from e

            script.puzzle_file.write_text(response.text)

        # ...else abort
        else:
            raise RuntimeError(f"{script.puzzle_file} is empty!")

    # Create prompt file if it doesn't already exist
    script.prompt_file.touch(exist_ok=True)

    prompt_file = script.prompt_file.read_text().strip()

    if "Part Two" not in prompt_file:
        response = session.get(
            script.prompt_url,
            cookies={"session": aoc_token()},
        )

        html = '\n\n'.join([a.html for a in response.html.find("article")])

        if not html:
            print("Failed to download prompt!")

        script.prompt_file.write_text(_html_to_markdown(html))

    return script.puzzle_file.read_text().strip()


def _html_to_markdown(_html):
    _html = re.sub("<p>(?P<text>.*?)</p>", "\n\g<text>\n", _html)

    _html = re.sub("<em>(?P<text>.*?)</em>", "**\g<text>**", _html)

    _html = _html.replace("<ul>", "")
    _html = _html.replace("</ul>", "")
    _html = re.sub("<li>(?P<text>.*?)</li>", "- \g<text>", _html)

    _html = re.sub("<code>(?P<text>.*?)</code>", "`\g<text>`", _html)

    _html = re.sub("<h2.*?>(?P<text>.*?)</h2>", "## \g<text>\n\n", _html)
    _html = re.sub("<span .*?>(?P<text>.*?)</span>", "\g<text>", _html)

    _html = html.unescape(_html)

    _html = re.sub("<article .*?>", "", _html)
    _html = re.sub("</article>", "", _html)

    _html = _html.replace("\n\n", "\n").strip()

    return _html
