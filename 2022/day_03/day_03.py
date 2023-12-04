import aoc_utils as utils

letters = 'abcdefghijklmnopqrstuvwxyz'
letters += letters.upper()
priority_dict = {letters[i]: i + 1 for i in range(len(letters))}
print(priority_dict)

def process_input():
    inp = utils.get_lines()
    return [[priority_dict[c] for c in s] for s in inp]

def part1():
    inp = process_input()
    inp = [(line[:int(len(line)/2)], line[int(len(line)/2):]) for line in inp]
    diffs = [(set(left) & set(right)).pop() for left, right in inp]
    return sum(diffs)


def part2():
    inp = process_input()
    inp = [inp[i*3:i*3+3] for i in range(int(len(inp)/3))]
    diffs = [(set(left) & set(center) & set(right)).pop() for left, center, right in inp]
    return sum(diffs)


if __name__ == '__main__':
    utils.run_tests(part1(), part2())
