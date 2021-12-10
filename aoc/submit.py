import functools
from typing import Union, Callable
from collections.abc import Callable
from typing import TypeVar
from .submit_puzzle import submit_puzzle


T = TypeVar("T")


def submit(part: int):
    def decorator(fn: Callable[[str], T]) -> Callable[[str], T]:
        @functools.wraps(fn)
        def fn_override(script_filename: str) -> T:
            solution = fn(script_filename)
            submit_puzzle(script_filename=script_filename, part=part, solution=solution)
            return solution

        return fn_override

    return decorator
