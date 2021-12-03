from pathlib import Path
import requests
import __main__
from itertools import permutations, cycle


SESSION = ""

SCRIPT_PATH = Path(__main__.__file__)
SCRIPT_DIR = Path(__main__.__file__).parent

DAY = SCRIPT_DIR.name
YEAR = SCRIPT_DIR.parent.name

file = "input"
# file = "test"
INPUT_PATH = SCRIPT_DIR / file

if not (INPUT_PATH.exists()):
    response = requests.get(
        f"https://adventofcode.com/{YEAR}/day/{DAY}/input",
        cookies={"session": SESSION},
    )
    response.raise_for_status()
    INPUT_PATH.write_text(response.text)

I = INPUT_PATH.read_text().splitlines()
I0 = I[0]

HALT = "HALT"

class Amplifier:
    def __init__(self, program):
        self.phase_setting = phase_setting
        self.position = 0
        self.executor = IntCodeComputer(program)

    def initiate(self, phase_setting):
        self.executor.run(phase_setting)

    def run(self, intake):
        return self.executor.run(intake)

class IntCodeComputer:
    def __init__(self, program):
        self.position = 0
        self.program = program

    def run(self, intake):
        opcode = self._opcode()

        if opcode == "99":
            return "HALT"

        elif opcode == "01":
            a, b = self._load_params(2)
            self._write(3, a + b)
            self._advance(4)
        elif opcode == "02":
            a, b = self._load_params(2)
            self._write(3, a * b)
            self._advance(4)
        elif opcode == "03":
            self._write(1, intake)
            self._advance(2)
        elif opcode == "04":
            self._advance(2)
            return self._load_params(1)[0]
        elif opcode == "05":
            a, b = self._load_params(2)
            self._move_to(b) if a != 0 else self._advance(3)
        elif opcode == "06":
            a, b = self._load_params(2)
            self._move_to(b) if a == 0 else self._advance(3)
        elif opcode == "07":
            a, b, c = self._load_params(3)
            self.write(3, 1 if a < b else 0)
            self._advance(4)
        elif opcode == "08":
            a, b, c = self._load_params(3)
            self.write(3, 1 if a == b else 0)
            self._advance(4)

        return self.run(intake)

    def _advance(self, spaces):
        self.position += spaces

    def _move_to(self, position):
        self.position = position

    def _write(self, rel_addr, value):
        self.program[self.program[self.position + 3]] = value

    def _load_params(self, count):
        modes = reversed(str(self.program[self.position]).zfill(5)[:3])
        params = []

        for i, mode in zip(range(1, count + 1), modes):

            if mode == "0":
                params.append(self.program[self.program[self.position + i]])
            else:
                params.append(self.program[self.position + i])

        return params

    def _opcode(self):
        return str(self.program[self.position]).zfill(2)[-2:]


def _execute(code, position=0, inputs=None, output=None):
    inputs = inputs or []

    instruction = str(code[position]).zfill(5)

    modes, opcode = reversed(instruction[:3]), instruction[-2:]

    if opcode == "99":
        return "HALT", None

    elif opcode == "01":
        a, b = _load_params(code, position, 2, modes)
        code[code[position + 3]] = a + b
        next_position = position + 4
    elif opcode == "02":
        a, b = _load_params(code, position, 2, modes)
        code[code[position + 3]] = a * b
        next_position = position + 4
    elif opcode == "03":
        new_in = inputs[0]
        code[code[position + 1]] = inputs[0]
        inputs = inputs[1:]
        next_position = position + 2
    elif opcode == "04":
        if output:
            raise RuntimeError(output)
        output = _load_params(code, position, 1, modes)[0]
        next_position = position + 2
        return output, next_position
    elif opcode == "05":
        a, b = _load_params(code, position, 2, modes)
        next_position = b if a != 0 else position + 3
    elif opcode == "06":
        a, b = _load_params(code, position, 2, modes)
        next_position = b if a == 0 else position + 3
    elif opcode == "07":
        a, b, c = _load_params(code, position, 3, modes)
        code[code[position + 3]] = 1 if a < b else 0
        next_position = position + 4
    elif opcode == "08":
        a, b, c = _load_params(code, position, 3, modes)
        code[code[position + 3]] = 1 if a == b else 0
        next_position = position + 4

    return _execute(code, next_position, inputs=inputs, output=output)


def _load_params(code, position, count, modes):
    params = []

    for i, mode in zip(range(1, count + 1), modes):

        if mode == "0":
            params.append(code[code[position + i]])
        else:
            params.append(code[position + i])

    return params


max_output = float("-inf")
program = [int(i) for i in I0.split(",")]
for phase_settings in permutations((0, 1, 2, 3, 4)):
    intake = 0
    for phase_setting in phase_settings:
        a = Amplifier(program)
        a.initiate(phase_setting)
        intake = output = a.run(intake)
        print(output)

    max_output = max(max_output, output)
print(max_output)

# max_output = float("-inf")
# for phase_settings in permutations((5, 6, 7, 8, 9)):
#     programs = []
#     positions = []
#     output = 0

#     for i, phase_setting in enumerate(phase_settings):
#         program = [int(i) for i in I0.split(",")]
#         programs.append(program)
#         output, position = _execute(program, inputs=[phase_setting, output])
#         positions.append(position)

#     thruster_output = float("-inf")
#     for i in cycle([0, 1, 2, 3, 4]):
#         output, position = _execute(programs[i], position=positions[i], inputs=[output])
#         positions[i] = position

#         if i == 4:
#             thruster_output = output

#         if output == HALT:
#             break

#     max_output = max(max_output, thruster_output)
# print(max_output)
