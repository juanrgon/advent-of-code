class String(str):

    def digits(self) -> list[int]:
        return [int(x) for x in self]

    def split(self, sep: str = " ") -> list["String"]:
        return [String(s) for s in super().split(sep)]
