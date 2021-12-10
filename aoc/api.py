"""
API client for adventofcode.com
"""

from __future__ import annotations
import os
import textwrap
from functools import cache
import typing
from typing import Callable, ParamSpec


P = ParamSpec("P")


if typing.TYPE_CHECKING:
    import requests_html


def _raise_for_status(
    fn: Callable[P, requests_html.HTMLResponse]
) -> Callable[P, requests_html.HTMLResponse]:
    def fn_override(*args: P.args, **kwargs: P.kwargs):
        response = fn(*args, **kwargs)
        response.raise_for_status()
        return response

    return fn_override


@_raise_for_status
def get(url: str) -> requests_html.HTMLResponse:
    return _session().get(url)


@_raise_for_status
def post(url: str, data: dict) -> requests_html.HTMLResponse:
    return _session().post(url, data=data)


@cache
def _session() -> requests_html.HTMLSession:
    import requests_html  # this is slow to import

    session = requests_html.HTMLSession()
    session.cookies.set("session", _aoc_token(), domain=".adventofcode.com")
    return session


@cache
def _aoc_token() -> str:
    # Load env vars from local .env file if it exists
    from dotenv import load_dotenv  # this is slow to import

    load_dotenv()

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
