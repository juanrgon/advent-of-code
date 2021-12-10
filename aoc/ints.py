import re


def ints(text):
    if callable(text):
        text = text()

    if isinstance(text, list):
        return [int(t) for t in text]

    return [int(i) for i in re.findall(r"-?\d+", text)]
