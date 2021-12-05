TEST = (
"""
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
""",
    4512,
)

TEST2 = (
"""
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
""",
    1924,
)

from typing import List

import sys
from pathlib import Path
from typing import List
import attr
import terminology

# import local AOC lib
sys.path.append(str(Path(__file__).parent.parent.parent))
import aoc


@attr.define
class BingoCell:
    value: int
    binged: bool


@attr.define
class BingoBoard:
    """Bingo Board is a winner if all in a row, or all in a column"""

    rows: List[List[BingoCell]]

    @classmethod
    def populate(cls, s: str):
        return BingoBoard(
            rows=[
                [BingoCell(value=int(n), binged=False) for n in line.split()]
                for line in s.strip().splitlines()
            ],
        )

    def winner(self) -> bool:
        return any(
            all(c.binged for c in cells)
            for cells in (self.rows + list(self.columns()))
        )

    def columns(self) -> List[List[BingoCell]]:
        cols = []
        for col in range(len(self.rows)):
            cols.append([row[col] for row in self.rows])
        return cols

    def cells(self):
        c = []
        for row in self.rows:
            for cell in row:
                c.append(cell)
        return c

    def binged(self):
        return [c for c in self.cells() if c.binged]

    def unbinged(self):
        return [c for c in self.cells() if not c.binged]

    def bing(self, number):
        for cell in self.cells():
            if cell.value == int(number):
                cell.binged = True

    def display(self):
        for row in self.rows:
            print(
                " ".join(
                    [
                        (
                            terminology.in_green(str(cell.value).zfill(2))
                            if cell.binged
                            else terminology.in_white(str(cell.value).zfill(2))
                        )
                        for cell in row
                    ]
                )
            )
        print()


@aoc.tests([TEST])
@aoc.parse_text
def part_1(raw: str, ints: List[int], strs: List[str]):
    bings = aoc.ints(strs[0])

    boards = [BingoBoard.populate(s) for s in raw.split("\n\n")[1:]]
    for b, bing in enumerate(bings, 1):
        for board in boards:
            board.bing(bing)

            if board.winner():
                return sum(b.value for b in board.unbinged()) * bing

        # if b % 5 == 0:
        #     for board in boards:
        #         board.display()
        #     pass

@aoc.tests([TEST2])
@aoc.parse_text
def part_2(raw: str, ints: List[int], strs: List[str]):
    bings = aoc.ints(strs[0])

    boards = [BingoBoard.populate(s) for s in raw.split("\n\n")[1:]]

    winners: List[int] = []

    for bing in bings:

        for i, board in enumerate(boards, 1):
            board.bing(bing)

            # if i == 2:
            #     print(f"Bing: {bing}")
            #     board.display()

            if i not in winners and board.winner():
                score = sum(b.value for b in board.unbinged()) * bing
                winners.append(i)
                print(f'Board {i} score: {score}')
                print('--------------------')
                board.display()

    return score


if __name__ == "__main__":
    puzzle = aoc.get_puzzle(__file__)

    part_1.test()
    print("Part 1:", part_1(puzzle))

    part_2.test()
    print("Part 2:", part_2(puzzle))
