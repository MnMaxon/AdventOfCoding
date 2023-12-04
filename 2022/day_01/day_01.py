def get_elves():
    elves = []
    elf = []
    lines = get_lines()
    lines.append('\n')
    for line in get_lines():
        if line == '\n':
            elves.append(elf)
            elf = []
        else:
            elf.append(int(line))
    return elves



def part1():
    elves = get_elves()
    totals = [sum(elf) for elf in elves]
    return max(totals)

def part2():
    elves = get_elves()
    totals = sorted([sum(elf) for elf in elves])
    return sum(totals[-3:])


def get_lines():
    with open('input.txt') as file:
        return file.readlines()


def run_tests():
    p1 = part1()
    if p1 is not None:
        print("Part 1", p1)

    p2 = part2()
    if p2 is not None:
        print("Part 2", p2)

    print("\nDone")


if __name__ == '__main__':
    run_tests()
