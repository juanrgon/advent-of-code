import click
import pendulum
import subprocess
import aoc.new_script
import os
import logging
from pathlib import Path

logger = logging.getLogger(__file__)


def _default_date() -> pendulum.DateTime:
    """
    Default date for new AOC script.

    If it is near midnight in December, use the "current" AOC puzzle as the default.

    Else, we use today's date.

    Allow AOC_YEAR env to override the default date.
    """
    east = "US/Eastern"

    now = pendulum.now(tz=east)

    if now.month == 12:
        if now.hour == 23:
            # if it's right before 12AM in December, use tomorrow as the default date
            # because it's almost AOC time
            return pendulum.tomorrow(east)
        elif now.hour == 0:
            # if it's after 12AM in December, use yestrday as the default date because
            # you probably want to do yesteray's date
            return pendulum.yesterday(east)

    year = int(os.environ["AOC_YEAR"]) or now.year

    year_dir = Path(__file__).parent.parent.parent.parent / str(year)

    if not year_dir.exists():
        day = 1
    else:
        day = max([int(p.stem) for p in year_dir.iterdir()]) + 1

    return pendulum.datetime(int(year), 12, day, 0, 0, 0)



@click.command()
@click.option(
    "-y",
    "--year",
    type=str,
    prompt=True,
    default=lambda: str(_default_date().year),
)
@click.option(
    "-d",
    "--day",
    type=str,
    prompt=True,
    default=lambda: str(_default_date().day),
)
def new(year: str, day: str):
    """Create new script for AOC"""
    script_file = aoc.new_script(year=year, day=day)

    print(f"Created script {script_file}!")

    if "EDITOR" in os.environ:
        subprocess.Popen(
            f"$EDITOR {script_file}",
            shell=True,
        )
