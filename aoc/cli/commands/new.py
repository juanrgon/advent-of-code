import click
import pendulum
from pathlib import Path
import subprocess
import aoc.new_script


@click.command()
@click.option(
    "-y",
    "--year",
    type=str,
    prompt=True,
    default=lambda: str(pendulum.now(tz="US/Eastern").year),
)
@click.option(
    "-d",
    "--day",
    type=str,
    prompt=True,
    default=lambda: str(pendulum.now(tz="US/Eastern").day),
)
def new(year: str, day: str):
    script_file = aoc.new_script(year=year, day=day)

    print(f"Created script {script_file}!")

    subprocess.Popen(
        f"$EDITOR {script_file}",
        shell=True,
    )
