from .parse_text import parse_text
from .get_input import get_input
from .tests import tests as run_tests
from .submit import submit as submit_to_aoc
import functools


def solution(part: int, tests=[], submit=False):
    def decorator(fn):
        @functools.wraps(fn)
        def fn_override(*args, **kwargs):
            f = parse_text(fn)
            f = run_tests(tests)(f)
            f = get_input(f)

            if submit:
                f = submit_to_aoc(part=part)(f)

            return f(*args, **kwargs)

        return fn_override

    return decorator
