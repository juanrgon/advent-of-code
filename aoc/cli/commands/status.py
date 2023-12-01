import click
import aoc.status
import terminology
import aoc.api


@click.command()
@click.option(
    "--refresh-from-site", is_flag=True, help="Load the status from the site."
)
def status(refresh_from_site: bool):
    """Load and display the current status for each year of AOC."""

    status = aoc.status.get()

    if refresh_from_site or not status:
        status = {}

        response = aoc.api.get("https://adventofcode.com/events")
        response.raise_for_status()

        for event in response.html.find(".eventlist-event"):
            # HTML Parsing
            year = int(event.find("a", first=True).text.strip("[] "))
            star_count = event.find(".star-count", first=True)

            status[year] = {}

            for star in range(int(star_count.text.strip("*")) if star_count else 0):
                day = int(star / 2) + 1
                status[year][day] = star % 2 + 1

        print("Loading status from adventofcode.com to disk\n")
        aoc.status.save(status)

    for year in sorted(status):
        print(year)
        print("----")

        if not status[year]:
            print("not yet started")
            print()
            continue

        for day, parts in status[year].items():
            print(f"Day {str(day).rjust(2)}", terminology.in_yellow("*" * parts))

        print()
