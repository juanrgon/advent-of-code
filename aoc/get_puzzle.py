import os
import requests
from requests_html import HTML
from pathlib import Path
from .aoc_token import aoc_token


def get_puzzle(script_path: str) -> str:
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

    # Use the folder that the script is in to to determine
    script = Path(script_path)

    year = script.parent.parent.name
    day = script.parent.name.lstrip("0")

    puzzle_file = script.parent / "input"

    # create the puzzle file if it doesn't already exist
    puzzle_file.touch(exist_ok=True)



    # If puzzle input file is empty...
    if not puzzle_file.read_text():
        # ...download the puzzle if the AOC session token is set in env vars
        if aoc_token():
            puzzle_url = f"https://adventofcode.com/{year}/day/{day}/input"
            response = requests.get(
                puzzle_url,
                cookies={"session": aoc_token()},
            )

            try:
                response.raise_for_status()
            except Exception as e:
                raise RuntimeError(f"Failed to download {puzzle_url}") from e

            puzzle_file.write_text(response.text)
        # ...else abort
        else:
            raise RuntimeError(f"{puzzle_file} is empty!")

    return puzzle_file.read_text().strip()
