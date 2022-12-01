from .integers import Integers
from .string import String


class Paragraph(list[String]):
    @property
    def ints(self) -> Integers:
        return Integers.from_strs(self)

    @property
    def raw(self) -> str:
        return "\n".join(self)

    @classmethod
    def list_from_str(cls, text: str) -> list["Paragraph"]:
        return [cls([String(s) for s in b.splitlines()]) for b in text.split("\n\n")]
