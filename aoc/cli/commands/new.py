import click
import pendulum
import subprocess
import aoc.new_script
import os
import logging
from pathlib import Path


@click.command()
@click.option(
    "-y",
    "--year",
    type=int,
)
@click.option(
    "-d",
    "--day",
    type=int,
)
def new(year: int, day: int):
    """Create new script for AOC"""

    
    year = click.prompt(f"Year", default=_get_year())
    day = click.prompt(f"Day", default=_get_day(year))

    click.prompt("Please enter a valid integer", type=int)

    script_file = aoc.new_script(year=year, day=day)

    print(f"Created script {script_file}!")

    if "EDITOR" in os.environ:
        subprocess.Popen(
            f"$EDITOR {script_file}",
            shell=True,
        )


def _get_year() -> int:
    east = "US/Eastern"

    now = pendulum.now(tz=east)

    if now.month == 12:
        if now.hour == 23:
            # if it's right before 12AM in December, use tomorrow as the default date
            # because it's almost AOC time
            return pendulum.tomorrow(east).year
        elif now.hour == 0:
            # if it's after 12AM in December, use yestrday as the default date because
            # you probably want to do yesteray's date
            return pendulum.today(east).year

    return int(os.environ.get("AOC_YEAR", 0)) or now.year


def _get_day(year: int) -> int:
    year_dir = Path(__file__).parent.parent.parent.parent / str(year)

    if not year_dir.exists():
        return 1
    else:
        return max([int(p.stem) for p in year_dir.iterdir()]) + 1
