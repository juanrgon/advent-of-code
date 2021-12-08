from pathlib import Path
import pendulum
import logging

logger = logging.getLogger(__name__)


def new_script(year: str, day: str, overwrite: bool = False) -> Path:
    day = day.zfill(2)

    script_dir = Path(__file__).parent.parent / year / day

    if script_dir.exists() and not overwrite:
        if pendulum.now() > pendulum.datetime(year=int(year), month=12, day=int(day)):
            logger.info("Allow override of solution file, because in the future")
        else:
            raise RuntimeError(f"Script already exists for {year}-{day}!!!")

    script_dir.mkdir(parents=True, exist_ok=True)

    filename = "main.py"

    script = script_dir / filename
    puzzle = script_dir / "input"

    script.touch(exist_ok=True)
    puzzle.touch(exist_ok=True)

    script.write_text(
        (Path(__file__).parent / "templates" / "script" / filename).read_text()
    )

    return script
