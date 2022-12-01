import functools
import operator

class Integers(list[int]):

    @classmethod
    def from_strs(cls, strs: list[str]) -> "Integers":
        return cls([int(x) for x in strs])

    @property
    def sum(self) -> int:
        return sum(self)

    @property
    def max(self) -> int:
        return max(self)

    @property
    def min(self) -> int:
        return min(self)

    @property
    def product(self) -> int:
        return functools.reduce(operator.mul, self)

    @property
    def mean(self) -> float:
        return sum(self) / len(self)

    @property
    def sorted(self) -> "Integers":
        return Integers(sorted(self))

    @property
    def median(self) -> float:
        return self.sorted[len(self) // 2]

    @property
    def mode(self) -> int:
        return max(set(self), key=self.count)

    @property
    def range(self) -> int:
        return self.max - self.min
