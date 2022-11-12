from pathlib import Path
import yaml
from functools import cache


Status = dict[int, dict[int, int]]


def completed(year: int, day: int, part: int = 2) -> bool:
    return get().get(year, {}).get(day, 0) >= part


def mark_completed(year: int, day: int, part: int):
    years = get()

    years.setdefault(year, {})

    score = years[year].get(day, 0)
    if score < part:
        years[year][day] = part

    _status_file().write_text(yaml.safe_dump(years))


def get() -> Status:
    if not _status_file().exists():
        _status_file().touch()

    return yaml.safe_load(_status_file().read_text()) or {}


def save(status: Status):
    _status_file().write_text(yaml.safe_dump(status, default_flow_style=False))


@cache
def _status_file() -> Path:
    return Path(__file__).parent.parent / ".status.yaml"


class StatusFileMissing(Exception):
    pass
