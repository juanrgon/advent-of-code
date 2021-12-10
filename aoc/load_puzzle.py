from .get_puzzle import get_puzzle
from typing import Callable, TypeVar

T = TypeVar("T")



def load_puzzle(fn: Callable[[str], T]) -> Callable[[str], T]:

    def fn_override(script_filename) -> T:
        raw = get_puzzle(script_filename)
        return fn(raw)

    return fn_override

