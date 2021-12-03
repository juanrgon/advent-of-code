import re

def ints(text):
    if callable(text):
        text = text()
    return [int(i) for i in re.findall(r"-?\d+", text)]
