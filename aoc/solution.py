from .parse_text import parse_text
from .get_input import get_input
from .tests import tests as run_tests
from .submit import submit


def solution(part: int, tests=[]):
    def decorator(fn):
        def fn_override(*args, **kwargs):
            f = parse_text(fn)
            f = run_tests(tests)(f)
            f = get_input(f)
            f = submit(part=part)(f)
            return f(*args, **kwargs)

        return fn_override

    return decorator