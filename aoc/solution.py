from .parse_text import parse_text
from .get_input import get_input
from .tests import tests as run_tests
from .submit import submit as submit_to_aoc
import functools


def solution(part: int, tests=[], submit=True):
    def decorator(fn):
        @functools.wraps(fn)
        def fn_override(*args, **kwargs):
            # parse the input
            f = parse_text(fn)

            # run the tests
            f = run_tests(tests)(f)

            # get the input from the website/disk
            f = get_input(f)

            # submit the solution
            f = submit_to_aoc(part=part)(f)

            return f(*args, **kwargs)

        return fn_override

    return decorator
