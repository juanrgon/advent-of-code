import functools
from collections.abc import Iterable
from typing import (
    Any,
    Callable,
    Iterable,
    ParamSpec,
    TypeVar,
)

import attr

P = ParamSpec("P")
T = TypeVar("T")

F = Callable[P, T]


def tests(cases: Iterable[tuple[str, int]]) -> F:
    def decorator(fn: F) -> F:
        @functools.wraps(fn)
        def fn_override(*args: P.args, **kwargs: P.kwargs):
            fn.test = _test_function(
                fn, [TestCase(args=[i], kwargs=None, expected=e) for i, e in cases]
            )
            return fn(*args, **kwargs)

        return fn_override

    return decorator


@attr.define
class TestCase:
    args: list[Any] | None = None
    kwargs: dict[str, Any] | None = None
    expected: str | int | None = None


def _test_function(fn, test_cases: list[TestCase]):
    for i, test_case in enumerate(test_cases):
        solution = fn(*(test_case.args or []), **(test_case.kwargs or {}))

        expected = test_case.expected

        if expected and solution != expected:
            raise ValueError(
                f"Test Case {i} Failed: Expected '{expected}'. Got {solution}"
            )
