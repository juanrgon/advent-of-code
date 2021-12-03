import functools
from textwrap import dedent
from typing import Union, Callable


def parse_text(fn: Callable):
    @functools.wraps(fn)
    def fn_override(raw: str) -> Union[int, str]:
        text = dedent(raw).strip()

        strs = text.splitlines()
        ints = []

        try:
            ints = [int(i) for i in text.splitlines()]
        except:
            pass

        return fn(raw=raw, ints=ints, strs=strs)

    return fn_override
