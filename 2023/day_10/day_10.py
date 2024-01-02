import aoc_utils as utils

offset_map = {
    '|': [(1, 0), (-1, 0)],
    '-': [(0, -1), (0, 1)],
    'L': [(-1, 0), (0, 1)],
    'J': [(-1, 0), (0, -1)],
    '7': [(1, 0), (0, -1)],
    'F': [(1, 0), (0, 1)]
}


class NotConnectedError(ValueError):
    pass


def get_start(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'S':
                return i, j


def get_next_direction(matrix, start, direction):
    direction = (-1 * direction[0], -1 * direction[1])
    val = matrix[start[0]][start[1]]
    if val not in offset_map:
        raise ValueError(f"Invalid Character: {val}")
    possible_paths = offset_map[val].copy()
    possible_paths.remove(direction)
    if len(possible_paths) != 1:
        raise NotConnectedError(f"No value connected to {val} at {start} from {direction}")
    return possible_paths[0]


def add_tup(a, b):
    return a[0] + b[0], a[1] + b[1]

def get_s_offsets(matrix, s_start):
    offsets = []
    for direction in [(0,1),(0,-1),(1,0),(-1,0)]:
        next_start = add_tup(s_start, direction)
        try:
            get_next_direction(matrix, next_start, direction) # Just using for the try catch
            offsets.append(direction)
        except NotConnectedError:
            pass
        except ValueError:
            pass
    if len(offsets) != 2:
        raise ValueError(f"Found {len(offsets)} offsets for S: {offsets}")
    return offsets


def get_path(data):
    s_start = get_start(data)
    path = [s_start]
    direction = get_s_offsets(data, s_start)[0]
    cur = add_tup(s_start, direction)
    while cur != s_start:
        path.append(cur)
        direction = get_next_direction(data, cur, direction)
        cur = add_tup(cur, direction)
    return path


class Day10(utils.Day):

    # Used to test code, run by using Day.run_tests(part_test=True)
    def run_part_test(self, data=None):
        data = super().run_part_test(data)
        return data

    # Converts list of strings into more meaningful data if necessary
    # Only really useful if you think there will be common code used twice
    def process_raw_input(self, raw_input=None):
        raw_input = super().process_raw_input(raw_input)
        # TODO Process raw data, given strings separated by new lines
        return raw_input

    def run_part_1(self, data=None):
        data = super().run_part_1(data)
        path = get_path(data)
        return int(len(path)/2)

    def run_part_2(self, data=None):
        data = super().run_part_2(data)
        path = get_path(data)

        # Update s if it should be a line
        log_data = data.copy()
        s_offsets = get_s_offsets(data, get_start(data))
        print(s_offsets)
        valid_s = None
        for char, offsets in offset_map.items():
            if all([o in offsets for o in s_offsets]):
                print(char, offsets, s_offsets)
                valid_s = char
        print(valid_s)
        data = [line.replace("S", valid_s[0]) for line in data]
        # data = [line.replace("LS7", "L-7").replace("LS-", "L--").replace("-S7", "--7").replace("-S-", "---") for line in data]
        # data = [line.replace("|L", "|-").replace("J|", "-|") for line in data]
        # print("=====")
        # for i, j in path:
        #     print(data[i][j], i, j)
        # print("=====")
        count = 0
        for i in range(len(data)):
            inside = False
            line_start=None
            for j in range(len(data[i])):
                if (i,j) in path:
                    char = data[i][j]
                    # directions = offset_map[char]
                    if char == '|':
                        inside = not inside
                    elif char == '-':
                        pass
                    elif char in ['F', "L"]:
                        line_start = char
                    elif char in ["J", "7"]:
                        if offset_map[line_start][0] != offset_map[char][0]:
                            inside = not inside
                elif inside:
                    # print(data[i][j], i,j)
                    log_data[i] = log_data[i][:j] + 'I' + log_data[i][j+1:]
                    count +=1
                else:
                    log_data[i] = log_data[i][:j] + 'O' + log_data[i][j+1:]
        print('\n'.join(log_data))
        return count


if __name__ == '__main__':
    day = Day10()
    day.run_tests(part_test=False)
