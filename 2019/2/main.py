import os.path


def main():
    print("Part 1 Solution: " + str(_part_1()))
    print("Part 2 Solution: " + str(_part_2()))


def _execute(code, position=0):
    opcode = code[position]

    if opcode == 99:
        return code[0]

    a = code[code[position + 1]]
    b = code[code[position + 2]]
    result_position = code[position + 3]

    if opcode == 1:
        result = a + b
    else:
        result = a * b

    code[result_position] = result

    return _execute(code, position + 4)


def _part_1():
    code = _program()
    code[1] = 12
    code[2] = 2
    return _execute(code)


def _part_2():
    target_output = 19690720
    original_code = _program()

    for noun in range(100):
        for verb in range(100):
            modified_code = original_code.copy()
            modified_code[1] = noun
            modified_code[2] = verb
            if target_output == _execute(modified_code):
                return 100 * noun + verb


def _program():
    with open(os.path.join(os.path.abspath("."), "program")) as f:
        return [int(i) for i in f.read().split(",")]


if __name__ == "__main__":
    main()
