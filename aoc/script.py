from __future__ import annotations
import attr
from pathlib import Path
import aoc.paths


@attr.define
class Script:
    """Abstraction of an AOC solution script."""

    day: str
    year: str

    path: Path
    prompt_file: Path
    input_file: Path
    prompt_url: str
    puzzle_url: str
    submit_url: str
    part_2_url: str

    @classmethod
    def from_filename(cls, script_filename: str) -> Script:
        path = Path(script_filename)

        day = path.parent.name.lstrip("0")
        year = path.parent.parent.name

        url = f"https://adventofcode.com/{year}/day/{day}"

        return Script(
            day=day,
            year=year,
            path=path,
            prompt_file=path.parent / "readme.md",
            input_file=path.parent / "input",
            prompt_url=f"{url}",
            puzzle_url=f"{url}/input",
            submit_url=f"{url}/answer",
            part_2_url=f"{url}#part2",
        )

    @classmethod
    def from_year_day(cls, *, year: int | str, day: int | str) -> Script:
        path = aoc.paths.TOP_LEVEL / str(year) / str(day).zfill(2) / "main.py"

        day = path.parent.name.lstrip("0")
        year = path.parent.parent.name

        url = f"https://adventofcode.com/{year}/day/{day}"

        return Script(
            day=day,
            year=year,
            path=path,
            prompt_file=path.parent / "readme.md",
            input_file=path.parent / "input",
            prompt_url=f"{url}",
            puzzle_url=f"{url}/input",
            submit_url=f"{url}/answer",
            part_2_url=f"{url}#part2",
        )
