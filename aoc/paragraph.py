class Paragraph(list[str]):

    def ints(self) -> list[int]:
        return [int(x) for x in self]

    def raw(self) -> str:
        return "\n".join(self)

    @classmethod
    def list_from_str(cls, text: str) -> list["Paragraph"]:
        return [cls(b.splitlines()) for b in text.split("\n\n")]
