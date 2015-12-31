from functools import reduce


def qe(group):
    return reduce(lambda x, y: x*y, group, 1)


def permutations(boxes, ngroups): # FIXME VERY BROKEN it found the first by luck, but it doesn't find all true permutations
    target = sum(boxes) // ngroups
    assert sum(boxes) == ngroups * target

    for n in range(len(boxes)):
        groups = [[] for x in range(ngroups)]
        remaining = boxes[:]
        i = n
        group = 0
        while group < len(groups) and sum(groups[group]) < target:
            if group == len(groups) - 1:
                if sum(remaining) == target:
                    groups[group] = remaining[:]
                    remaining = []
                else:
                    break
            if i >= len(remaining):
                break
            a = remaining[i]
            if sum(groups[group]) + a <= target:
                groups[group].append(a)
                del remaining[i]
            else:
                i += 1
            if sum(groups[group]) == target:
                i = 0
                group += 1
        if len(remaining) > 0:
            continue
        yield sorted(groups, key=len)


def process_input():
    with open("input.txt") as file:
        data = file.read().splitlines()
    return [int(i) for i in data]
    # return list(range(1, 6)) + list(range(7, 12))


def evalp1(data, ngroups=3):
    arrangements = []

    for maybe in permutations(list(reversed(sorted(data))), ngroups):
        if maybe not in arrangements:
            arrangements.append(maybe)
    arrangements.sort(key=lambda x: len(x[0]))
    shortest = len(arrangements[0][0])
    quantum = [qe(x[0]) for x in arrangements if len(x[0]) == shortest]

    return min(quantum)


def evalp2(data):
    return evalp1(data, 4)


def main():
    data = process_input()
    part1 = evalp1(data)
    print("Part 1:")
    print(part1)
    print("Part 2:")
    print(evalp2(data))

if __name__ == "__main__":
    main()
