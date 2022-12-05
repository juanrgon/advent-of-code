import functools
from textwrap import dedent
from typing import Callable
import attrs

from .ints import ints
from .paragraph import Paragraph
from .integers import Integers
from .string import String


def parse_text(
    fn: Callable[[str, list[int], list[str], list[list[str]]], int | str]
) -> Callable[[str], int | str]:
    @functools.wraps(fn)
    def fn_override(raw: str | int) -> int | str:
        text = dedent(str(raw)).strip()
        return fn(
            raw=raw,
            ints=Integers(ints(text)),
            strs=[String(s) for s in text.splitlines()],
            paragraphs=Paragraph.list_from_str(text),
        )

    return fn_override
