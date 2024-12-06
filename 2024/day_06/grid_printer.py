
# This was a cool function - copied the grid from https://adventofcode.com/2024/day/6#part2
def print_grid(data, guard_i=None, guard_j=None, facing=None, wall_i=None, wall_j=None, steps=None, new_line=True):
    for i in range(len(data)):
        row = data[i]
        if guard_i == i:
            row = row[:guard_j] + _get_guard_char(facing) + row[guard_j + 1:]
        if wall_i == i:
            row = row[:wall_j] + 'O' + row[wall_j + 1:]
        if steps:
            for coord, face in steps:
                if coord[0] == i:
                    c = _get_path_char(row[coord[1]], face)
                    row = row[:coord[1]] + c + row[coord[1] + 1:]
        print(row)
    if new_line:
        print()


def _get_guard_char(facing):
    if facing == 0:
        return "^"
    elif facing == 1:
        return ">"
    elif facing == 2:
        return "v"
    elif facing == 3:
        return "<"
    return "X"


def _get_path_char(cur_char, face):
    if cur_char == '|' or cur_char == '-':
        c = '+'
    elif cur_char != '.':
        c = cur_char
    elif face == 0 or face == 2:
        c = "|"
    else:
        c = "-"
    return c