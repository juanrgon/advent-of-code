import os
import textwrap
from functools import lru_cache
from dotenv import load_dotenv

# Load env vars from local .env file if it exists
load_dotenv()

AOC_TOKEN_ENV_VAR_NAME = "ADVENT_OF_CODE_COOKIE"
AOC_TOKEN = os.environ.get(AOC_TOKEN_ENV_VAR_NAME, "")

@lru_cache
def aoc_token() -> str:
    if not AOC_TOKEN:
        import ipdb; ipdb.set_trace()
        print(
            textwrap.dedent(
            f"""
            {AOC_TOKEN_ENV_VAR_NAME} isn't set, so the puzzle input can't be automatically
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

    return AOC_TOKEN
