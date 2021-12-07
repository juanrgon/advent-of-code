import functools
from textwrap import dedent
from typing import Union, Callable
from .ints import ints


def parse_text(fn: Callable):

    @functools.wraps(fn)
    def fn_override(raw: str) -> int | str:
        text = dedent(raw).strip()
        return fn(raw=text, ints=ints(text), strs=text.splitlines())

    return fn_override
