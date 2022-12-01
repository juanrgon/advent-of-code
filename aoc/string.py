class String(str):

    def digits(self) -> list[int]:
        return [int(x) for x in self]
