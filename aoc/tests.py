import functools
import sys
from pathlib import Path
from textwrap import dedent
from typing import Any, Dict, List, Literal, Optional, Union, Iterable
import attr


def tests(cases: Iterable[Union[str, Any]]):

    def decorator(fn):

        def test():
            _test_function(fn, fn.test_cases)

        fn.test_cases = [TestCase(args=[i], kwargs=[], expected=e) for i, e in cases]
        fn.test = test

        return fn

    return decorator

@attr.define
class TestCase:
    args: Optional[List[Any]] = None
    kwargs: Optional[Dict[str, Any]] = None
    expected: Optional[Union[str, int]] = None

def _test_function(fn, test_cases: List[TestCase]):
    for i, test_case in enumerate(test_cases):
        solution = fn(*(test_case.args or []), **(test_case.kwargs or {}))

        expected = test_case.expected

        if expected and solution != expected:
            raise ValueError(
                f"Test Case {i} Failed: Expected '{expected}'. Got {solution}"
            )

