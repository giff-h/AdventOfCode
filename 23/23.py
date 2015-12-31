def process_input():
    with open("input.txt") as file:
        data = file.read().splitlines()
    instructions = []
    for line in data:
        instruction = line.split()
        if instruction[0] in ("jio", "jie"):
            instruction[1] = instruction[1][:1]
            instruction[2] = int(instruction[2])
        elif instruction[0] == "jmp":
            instruction[1] = int(instruction[1])
        instructions.append(tuple(instruction))
    return instructions


def evalp1(data):
    register = {'a': 0, 'b': 0}

    i = 0
    while True:
        try:
            instruction = data[i]
        except IndexError:
            return register['b'], None
        if instruction[0] == "inc":
            register[instruction[1]] += 1
            i += 1
        elif instruction[0] == "tpl":
            register[instruction[1]] *= 3
            i += 1
        elif instruction[0] == "hlf":
            if register[instruction[1]] % 2 == 1:
                print("uh oh, odd")
            register[instruction[1]] //= 2
            i += 1
        elif instruction[0] == "jmp":
            i += instruction[1]
        elif instruction[0] == "jio":
            i += instruction[2] if register[instruction[1]] == 1 else 1
        elif instruction[0] == "jie":
            i += instruction[2] if register[instruction[1]] % 2 == 0 else 1


def evalp2(data, part1):
    return evalp1([("inc", "a")] + data)[0]


def main():
    data = process_input()
    part1 = evalp1(data)
    print("Part 1:")
    print(part1[0])
    print("Part 2:")
    print(evalp2(data, part1[1]))

if __name__ == "__main__":
    main()
