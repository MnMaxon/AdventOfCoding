import aoc_utils as utils

ROCK = 1
PAPER = 2
SCISSORS = 3

rps_lists = [
    [ROCK, PAPER, SCISSORS],
    ['A', 'B', 'C'],
    ['X', 'Y', 'Z'],
]

type_map = {}

for rps_list in rps_lists:
    for list_index in range(len(rps_list)):
        type_map[rps_list[list_index]] = list_index + 1

def get_points(them, you):
    win_modifier = ((you - them + 1) % 3) - 1
    winning_points = win_modifier * 3 + 3
    return winning_points + you

def process_input():
    inp = utils.get_lines()
    inp = [s.split() for s in inp]
    return [(type_map[x], type_map[y]) for x, y in inp]

def decode(them, win_condition):
    win_modifier = win_condition - 2
    return (them + win_modifier - 1) % 3 + 1

def part1():
    inp = process_input()
    points = [get_points(them, you) for them, you in inp]
    return sum(points)


def part2():
    inp = process_input()
    decoded = [(them, decode(them, win_condition)) for them, win_condition in inp]
    points = [get_points(them, you) for them, you in decoded]
    return sum(points)


if __name__ == '__main__':
    utils.run_tests(part1(), part2())
