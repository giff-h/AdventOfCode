import re


def process_input():
    inp = re.compile("row ([0-9]+), column ([0-9]+)")

    with open("input.txt") as file:
        data = file.read()
    groups = inp.search(data).groups()
    return [int(x) for x in groups]


def evalp1(data):
    row, col = data
    nth = (row + col - 2) * (row + col - 1) // 2 + col
    return (20151125 * pow(252533, nth - 1, 33554393)) % 33554393


def main():
    data = process_input()
    part1 = evalp1(data)
    print("Part 1:")
    print(part1)

if __name__ == "__main__":
    main()
