from .parse_text import parse_text
from .get_input import get_input
from .tests import tests as run_tests
from .submit import submit as submit_to_aoc
from pathlib import Path
import functools
import toml
from typing import Iterable


def solution(
    part: int, tests: Iterable[tuple[str, int]] | None = None, submit: bool = True
):
    def decorator(fn):
        @functools.wraps(fn)
        def fn_override(aoc_solution_filename: str):
            # parse the input. this function expects the raw input as a string, and then
            # calls the decorated function with the parsed input as arguments.
            f = parse_text(fn)

            # if tests are passed to this decorator, use those, otherwise load the tests
            # from the test file, if it exists:
            tests_to_run = tests
            if tests_to_run is None:
                tests_to_run = tests
                test_file = Path(aoc_solution_filename).parent / "tests.toml"
                if test_file.exists():
                    tests_to_run = load_tests(test_file=test_file, part=part)

            tests_to_run = tests_to_run or []

            # run the tests. this decorator uses the passed in tests to run the decorated
            # function, and then returns the result of the actual input if the tests
            # pass.
            f = run_tests(tests_to_run)(f)

            # get the input from the website/disk. this decorator will load text from the
            # input file (or download it from adventofcode.com if it doesn't exist) and
            # then calls the decorated function with the input's string as an argument.
            f = get_input(f)

            # submit the solution. this final decorator will submit to result from the
            # function to adventofcode.com
            if submit:
                f = submit_to_aoc(part=part)(f)

            return f(aoc_solution_filename)

        return fn_override

    return decorator


def load_tests(test_file: Path, part: int) -> Iterable[tuple[str, int]]:
    return [
        (t["input"], t["solution"])
        for t in toml.loads(test_file.read_text()).get(f"{part}", [])
    ]
