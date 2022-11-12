import functools
from typing import Callable
from collections.abc import Callable
from typing import TypeVar

import aoc.status
import aoc.api

from .script import Script
import sys
import terminology

T = TypeVar("T")


def submit(part: int):
    def decorator(fn: Callable[[str], T]) -> Callable[[str], T]:
        @functools.wraps(fn)
        def fn_override(script_filename: str) -> T:
            solution = fn(script_filename)
            _submit(script_filename=script_filename, part=part, solution=solution)
            return solution

        return fn_override

    return decorator


def _submit(*, script_filename: str, part: int, solution):
    script = Script.from_filename(script_filename)

    # check if already completed before submitting
    if aoc.status.completed(year=int(script.year), day=int(script.day), part=part):
        return

    response = aoc.api.post(
        script.submit_url,
        data={"level": part, "answer": solution},
    )

    try:
        response.raise_for_status()
    except Exception as e:
        raise RuntimeError(
            f"Failed to submit puzzle for {script.year} Day {script.day} Part {part}"
        ) from e

    result = "\n" + response.html.find("article")[0].full_text

    if (
        "You don't seem to be solving the right level.  Did you already complete it?"
        in result
    ):
        return

    if "That's the right answer!" in result:
        # Remove the annoying last sentence about twitter
        result = result.rsplit(".", 2)[0]
        print(terminology.in_green(result), "\n")

        aoc.status.mark_completed(year=int(script.year), day=int(script.day), part=part)

        if part == 1:
            print(f"Visit {script.part_2_url} for part 2\n")
            sys.exit(0)
        else:
            script.day = str(int(script.day) + 1)  # gross, but practical
            print(f"Visit {script.prompt_url} for Day {script.day}\n")

    else:
        print(terminology.in_red(result), "\n")
