import re
import __main__
import os.path


class Passport(object):
    def __init__(self, byr, iyr, eyr, hgt, hcl, ecl, pid, cid=None):
        self.byr = byr
        self.iyr = iyr
        self.eyr = eyr
        self.hgt = hgt
        self.hcl = hcl
        self.ecl = ecl
        self.pid = pid

    @classmethod
    def _from_raw_text(cls, text):
        return Passport(**{d.split(":")[0]: d.split(":")[1] for d in text.split()})

    def validate(self):
        self._validate_byr()

    def _validate_byr(self):
        if not 1920 <= int(self.byr) <= 2002:
            raise InvalidByr(f"{self.pid}: {self.byr}")

    def _validate_iyr(self):
        if not 2010 <= int(self.eyr) <= 2020:
            raise InvalidEyr(f"{self.pid}: {self.iyr}")

    def _validate_eyr(self):
        if not 2020 <= int(self.eyr) <= 2030:
            raise InvalidEyr(f"{self.pid}: {self.eyr}")

    def _validate_hgt(self):
        if not 2020 <= int(self.hgt) <= 2030:
            raise InvalidHgt(f"{self.pid}: {self.hgt}")

    def _validate_hcl(self):
        if not (self.hgt[-2:] in ("in", "cm")) or not (
            (150 <= int(self.hgt[:-2]) <= 193)
            if self.hgt[-2:] == "cm"
            else (59 <= int(self.hgt[:-2]) <= 76)
        ):
            raise InvalidHcl(f"{self.pid}: {self.hcl}")

    def _validate_ecl(self):
        if self.ecl not in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"):
            raise InvalidEcl(f"{self.pid}: {self.ecl}")

    def _validate_pid(self):
        if not re.match(r"^[0-9]{9}$", self.pid):
            raise InvalidPid(f"{self.pid}")


class InvalidPassport(Exception):
    pass


class InvalidByr(InvalidPassport):
    pass


class InvalidIyr(InvalidPassport):
    pass


class InvalidEyr(InvalidPassport):
    pass


class InvalidHgt(InvalidPassport):
    pass


class InvalidHcl(InvalidPassport):
    pass


class InvalidEcl(InvalidPassport):
    pass


class InvalidPid(InvalidPassport):
    pass


def main():
    print("Solution to Part 1: " + _part_1())
    print("Solution to Part 2: " + _part_2())


def _part_1():
    raw_passports = _load_passports(_input())

    valid = 0
    for raw_passport in raw_passports:
        try:
            Passport._from_raw_text(raw_passport)
        except TypeError:
            continue
        else:
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
    with open(os.path.join(os.path.dirname(__main__.__file__), "input")) as f:
        return f.read()


if __name__ == "__main__":
    main()
