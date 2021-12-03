import attr
from pathlib import Path


@attr.define
class Script:
    """Abstraction of an AOC solution script."""

    day: str
    year: str

    path: Path
    puzzle_file: Path
    submit_url: str
    puzzle_url: str
    part_2_url: str

    @classmethod
    def from_filename(cls, script_filename: str) -> "Script":
        path = Path(script_filename)

        day=path.parent.name.lstrip("0")
        year=path.parent.parent.name

        url = f"https://adventofcode.com/{year}/day/{day}"

        return Script(
            day=day,
            year=year,
            path=path,
            puzzle_file=path.parent / "input",
            puzzle_url=f"{url}/input",
            submit_url=f"{url}/answer",
            part_2_url=f"{url}#part2",
        )
