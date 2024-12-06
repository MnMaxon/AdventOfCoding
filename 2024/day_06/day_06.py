import aoc_utils as utils
from grid_printer import print_grid

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def get_steps(data, facing, guard_i, guard_j):
    steps = []
    while 0 <= guard_i < len(data) and 0 <= guard_j < len(data[0]):
        coords = (guard_i, guard_j)
        if data[guard_i][guard_j] == '#':
            guard_i = guard_i - dirs[facing][0]
            guard_j = guard_j - dirs[facing][1]
            facing = (facing + 1) % 4
            continue
        if coords not in steps:
            steps.append(coords)
        guard_i += dirs[facing][0]
        guard_j += dirs[facing][1]
    return steps


def get_starting_coords(data):
    guard_i = -1
    guard_j = -1
    for i in range(len(data)):
        for j in range(len(data[i])):
            c = data[i][j]
            if c == '^':
                guard_i = i
                guard_j = j
                data[i] = data[i].replace('^', '.')
    return guard_i, guard_j


class Day06(utils.Day):
    def run_part_1(self, data):
        facing = 0
        guard_i, guard_j = get_starting_coords(data)
        steps = get_steps(data, facing, guard_i, guard_j)
        return len(steps)

    def run_part_2(self, data):
        facing = 0
        guard_i, guard_j = get_starting_coords(data)
        total = 0

        steps = get_steps(data, facing, guard_i, guard_j)
        steps = steps[1:]

        for step in steps:
            inf, _ = is_infinite(data, guard_i, guard_j, step[0], step[1], facing=0)
            if inf:
                total += 1
        return total


def is_infinite(data, guard_i, guard_j, wall_i, wall_j, facing=0, debug=False):
    steps = set()
    data = [x for x in data]
    data[wall_i] = data[wall_i][:wall_j] + '#' + data[wall_i][wall_j + 1:]
    guard_i -= dirs[facing][0]
    guard_j -= dirs[facing][1]
    # print("\n================\n")
    # print_grid(data, guard_i, guard_j, facing, wall_i, wall_j)
    while 0 <= guard_i < len(data) and 0 <= guard_j < len(data[0]):
        coords = ((guard_i, guard_j), facing)
        if data[guard_i][guard_j] == '#':
            guard_i = guard_i - dirs[facing][0]
            guard_j = guard_j - dirs[facing][1]
            facing = (facing + 1) % 4
            if debug:
                print("HIT WALL:", guard_i, guard_j, "->", guard_i + dirs[facing][0], guard_j + dirs[facing][1])
                print_grid(data, guard_i, guard_j, facing, wall_i, wall_j, steps)
            continue
        if coords in steps:
            return True, steps
        steps.add(coords)
        guard_i += dirs[facing][0]
        guard_j += dirs[facing][1]
    return False, steps


if __name__ == '__main__':
    day = Day06()
    day.run_tests(
        sample_input=True,
        real_input=True,
        part1=True,
        part2=True,
        part_test=False,
    )
