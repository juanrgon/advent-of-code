import click
import importlib.util
from typing import List
from pathlib import Path
import aoc


@click.command()
@click.argument("local_scriptpath", metavar="SCRIPT")
@click.option(
    "--part",
    "parts",
    default=["1", "2"],
    type=click.Choice(["1", "2"]),
    multiple=True,
    help="A specific part of the puzzle to submit, either 1 or 2. Defaults to submitting both if omitted.",
)
def submit(local_scriptpath: str, parts: List[int]):
    """Submit solution(s) from script to AOC."""

    script = Path(local_scriptpath).absolute()

    # load script. process grabbed from docs in importlib module
    spec = importlib.util.spec_from_file_location(script.stem, str(script))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    for i in parts:
        part = getattr(module, f'part_{i}')

        puzzle = aoc.get_puzzle(script)

        part.test()
        solution = part(puzzle)

        aoc.submit_puzzle(script_filename=script, part=i, solution=solution)
        print("Submitted Part {i}!")
