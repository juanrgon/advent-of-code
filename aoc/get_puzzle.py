import requests
from .aoc_token import aoc_token
from .script import Script
from datetime import datetime
import pendulum


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

    # Use the folder that the script is in to to determine
    script = Script.from_filename(script_filename)

    # create the puzzle file if it doesn't already exist
    script.puzzle_file.touch(exist_ok=True)

    # If puzzle input file is empty...
    if not script.puzzle_file.read_text():
        puzzle_start = pendulum.datetime(
            int(script.year), 12, int(script.day), 0, 0, 0, tz="US/Eastern"
        )

        if pendulum.now() < puzzle_start:
            raise RuntimeError(f"Too early for {script.year} Day {script.day}")

        # ...download the puzzle if the AOC session token is set in env vars
        if aoc_token():
            response = requests.get(
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

    return script.puzzle_file.read_text().strip()
