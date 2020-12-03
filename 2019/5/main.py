import os.path


def main():
    print("Solution to Part 1: " + _part_1())
    print("Solution to Part 2: " + _part_2())


def _execute(code, position=0, in_code=1, output=None):
    instruction = str(code[position]).zfill(5)

    modes, opcode = reversed(instruction[:3]), instruction[-2:]

    if opcode == "99":
        return output
    elif opcode == "01":
        a, b = _load_params(code, position, 2, modes)
        code[code[position + 3]] = a + b
        next_position = position + 4
    elif opcode == "02":
        a, b = _load_params(code, position, 2, modes)
        code[code[position + 3]] = a * b
        next_position = position + 4
    elif opcode == "03":
        code[code[position + 1]] = in_code
        next_position = position + 2
    elif opcode == "04":
        if output:
            raise RuntimeError(output)
        output = _load_params(code, position, 1, modes)[0]
        next_position = position + 2
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

    return _execute(code, next_position, in_code=in_code, output=output)


def _input():
    with open(os.path.join(os.path.abspath("."), "input")) as f:
        return [int(n) for n in f.read().strip().split(",")]


def _load_params(code, position, count, modes):
    params = []

    for i, mode in zip(range(1, count + 1), modes):

        if mode == "0":
            params.append(code[code[position + i]])
        else:
            params.append(code[position + i])

    return params


def _part_1():
    return str(_execute(_input(), in_code=1))


def _part_2():
    return str(_execute(_input(), in_code=5))


if __name__ == "__main__":
    main()
