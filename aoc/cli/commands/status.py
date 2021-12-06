import click
import requests
import requests_html
import pendulum
from aoc.aoc_token import aoc_token
import yaml
from pathlib import Path
import terminology


FIRST_YEAR = 2015


@click.command()
@click.option(
    "--refresh-from-site", is_flag=True, help="Load the status from the site."
)
def status(refresh_from_site: bool):
    """Load and display the current status for each year of AOC."""

    years = {}

    status_file = Path(__file__).parent.parent.parent.parent / ".status.yaml"

    if refresh_from_site or not status_file.exists():
        today = pendulum.now("US/Eastern")
        most_recent_year = today.year if today.month == 12 else today.year - 1

        for year in range(FIRST_YEAR, most_recent_year + 1):
            years[year] = {}

            response = requests.get(
                f"https://adventofcode.com/{year}", cookies={"session": aoc_token()}
            )

            if response is None:
                import ipdb

                ipdb.set_trace()

            star_count = requests_html.HTML(html=response.text).find(
                ".star-count", first=True
            )
            total_stars = int(star_count.text.strip("*")) if star_count else 0

            for star in range(total_stars):
                day = int(star / 2) + 1
                years[year][day] = star % 2 + 1

        print(f"Loading status from adventofcode.com to {status_file}\n")
        status_file.write_text(yaml.safe_dump(years, default_flow_style=False))

    years = yaml.safe_load(status_file.read_text())

    for year in years:
        print(year)
        print('----')

        if not years[year]:
            print("not yet started")
            print()
            continue


        for day, parts in years[year].items():
            print(f'Day {day}', terminology.in_yellow('*' * parts))

        print()
