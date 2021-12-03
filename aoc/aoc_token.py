import os
import textwrap
from functools import lru_cache
from dotenv import load_dotenv

# Load env vars from local .env file if it exists
load_dotenv()


@lru_cache
def aoc_token() -> str:
    aoc_token_env_var = "ADVENT_OF_CODE_COOKIE"
    aoc_token_value = os.environ.get(aoc_token_env_var, "")

    if not aoc_token_value:
        print(
            textwrap.dedent(
            f"""
            {aoc_token_env_var} isn't set, so the puzzle input can't be automatically
            downloaded, and puzzle solutions can't be automatically submitted.

            You can get the cookie value by

                - going to https://adventofcode.com/ in chrome,
                - opening developer tools,
                - clicking the Application tab,
                - expanding Cookies on the left
                - clicking 'https://adventofcode.com
                - copying the value for the cookie named 'session

            Add the cookie value to a .env file at the top of your local copy of this repo:

            ```
            # .env file
            ADVENT_OF_CODE_COOKIE=<AOC cookie value>
            ```

            DON'T COMMIT THE .env FILE (it's not dangerous if you do, but it could attract trolls)
            """
            )
        )

    return aoc_token_value
