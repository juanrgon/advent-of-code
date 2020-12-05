import re
import __main__
import os.path


def main():
    print("Solution to Part 1: " + _part_1())
    print("Solution to Part 2: " + _part_2())


def _part_1():
    passports = _load_passports(_input())

    valid = 0
    for passport in passports:
        is_valid = True
        for field in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]:
            if field not in passport:
                is_valid = False
                break

        if is_valid:
            valid += 1

    return str(valid)


def _part_2():
    passports = _load_passports(_input())

    valid = 0
    for passport in passports:
        is_valid = True
        for field in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]:
            if field not in passport:
                is_valid = False
                break

        if is_valid and (
            (1920 <= int(passport["byr"]) <= 2002)
            and (2010 <= int(passport["iyr"]) <= 2020)
            and (2020 <= int(passport["eyr"]) <= 2030)
            and (passport["hgt"][-2:] in ("in", "cm"))
            and (
                (150 <= int(passport["hgt"][:-2]) <= 193)
                if passport["hgt"][-2:] == "cm"
                else (59 <= int(passport["hgt"][:-2]) <= 76)
            )
            and re.match(r"^#[0-9a-f]{6}$", passport["hcl"])
            and passport["ecl"] in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
            and re.match(r"^[0-9]{9}$", passport["pid"])
        ):
            valid += 1

    return str(valid)


def _load_passports(text):
    passports = []
    for data in _input().split("\n\n"):
       passports.append({d.split(":")[0]: d.split(":")[1] for d in data.split()})
    return passports



def _input():
    with open(os.path.join(os.path.dirname(__main__.__file__),  'input')) as f:
        return f.read()


if __name__ == "__main__":
    main()
