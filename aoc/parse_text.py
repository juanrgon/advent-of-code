import functools
from textwrap import dedent
from typing import Union, Callable
from .ints import ints


def parse_text(fn: Callable):
    @functools.wraps(fn)
    def fn_override(raw: str) -> Union[int, str]:
        text = dedent(raw).strip()

        strs = text.splitlines()

        return fn(raw=raw, ints=ints(text), strs=strs)

    return fn_override
