TEST = (
    """
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
""",
    26,
)

TEST2 = (
    """
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
""",
    61229,
)


from functools import singledispatch
import aoc


@aoc.tests([TEST])
@aoc.parse_text
def part_1(raw: str, ints: list[int], strs: list[str]):
    count = 0
    for line in raw.splitlines():
        l, r = line.split(" | ")
        for s in r.split():
            if len(s) == 2:
                count += 1
            if len(s) == 4:
                count += 1
            if len(s) == 3:
                count += 1
            if len(s) == 7:
                count += 1
    return count


@aoc.tests([TEST2])
@aoc.parse_text
def part_2(raw: str, ints: list[int], strs: list[str]):
    total = 0

    for line in raw.splitlines():
        l, r = line.split(" | ")
        signals = ["".join(sorted(s)) for s in l.split()]
        outputs = ["".join(sorted(s)) for s in r.split()]

        nums = {}

        two_three_or_five = []
        zero_six_or_nine = []

        # find 2, 4, 3, and 7
        for signal in signals:
            if len(signal) == 2:
                nums[1] = signal
            elif len(signal) == 4:
                nums[4] = signal
            elif len(signal) == 3:
                nums[7] = signal
            elif len(signal) == 7:
                nums[8] = signal
            elif len(signal) == 5:
                two_three_or_five.append(signal)
            elif len(signal) == 6:
                zero_six_or_nine.append(signal)

        # find 2, 3, and 5
        for signal in two_three_or_five:
            # all of the characters in 1 are in 3
            if set(nums[1]).issubset(signal):
                nums[3] = signal

            # only 2 and 4 combine to make 8
            elif set(signal + nums[4]) == set(nums[8]):
                nums[2] = signal

            else:
                nums[5] = signal

        # find 0, 6, and 9
        for signal in zero_six_or_nine:
            # all of the characters in 4 are in 9
            if set(nums[4]).issubset(signal):
                nums[9] = signal

            # all of the characters in 5 are in 6
            elif set(nums[5]).issubset(signal):
                nums[6] = signal

            else:
                nums[0] = signal

        letters_to_nums = {v: k for k, v in nums.items()}
        total += int(''.join([str(letters_to_nums[o]) for o in outputs]))

    return total




if __name__ == "__main__":
    puzzle = aoc.get_puzzle(__file__)

    part_1.test()
    print("Part 1:", part_1(puzzle))

    part_2.test()
    print("Part 2:", part_2(puzzle))
