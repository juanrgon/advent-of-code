from .aoc_token import aoc_token
from .script import Script
import sys
from pathlib import Path
import yaml
import terminology


def submit_puzzle(*, script_filename: str, part: int, solution):
    script = Script.from_filename(script_filename)
    status_file = Path(__file__).parent.parent / ".status.yaml"

    # check if already completed before submitting
    status = yaml.safe_load(status_file.read_text())
    if status.get(script.year, {}).get(script.day, 0) >= part:
        return

    import requests  # requests is slow to import
    from requests_html import HTML  # request_html is slow to import


    response = requests.post(
        script.submit_url,
        cookies={"session": aoc_token()},
        data={"level": part, "answer": solution},
    )

    try:
        response.raise_for_status()
    except Exception as e:
        raise RuntimeError(
            f"Failed to submit puzzle for {script.year} Day {script.day} Part {part}"
        ) from e

    result = "\n" + HTML(html=response.text).find("article")[0].full_text

    if (
        "You don't seem to be solving the right level.  Did you already complete it?"
        in result
    ):
        return

    if "That's the right answer!" in result:
        result = result.rsplit('.', 2)[0]  # Remove the annoying last sentence about twitter
        print(terminology.in_green(result), '\n')

        # save status to disk
        status.setdefault(script.year, {})
        status[script.year][script.day] = part
        status = status_file.write_text(yaml.safe_dump(status))

        if part == 1:
            print(f"Visit {script.part_2_url} for part 2\n")
            sys.exit(0)
        else:
            script.day += script.day  # gross, but pratical
            print(f"Visit {script.prompt_url} for Day {script.day}\n")

    else:
        print(terminology.in_red(result), '\n')
