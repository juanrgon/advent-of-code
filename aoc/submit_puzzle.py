from .aoc_token import aoc_token
from .script import Script


def submit_puzzle(*, script_filename: str, part: int, solution):
    import requests  # requests is slow to import
    from requests_html import HTML  # request_html is slow to import

    script = Script.from_filename(script_filename)

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

    if "That's the right answer!" in result and part == 1:
        print(f"Visit {script.part_2_url} for part 2")
