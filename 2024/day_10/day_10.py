import aoc_utils as utils


def find_neighbors(data, i, j, allow_dups=False):
    search_val = data[i][j] + 1
    ret_list = []
    for add_i, add_j in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        new_i = i + add_i
        new_j = j + add_j
        if is_neighbor(data, new_i, new_j, search_val):
            if search_val == 9:
                ret_list.append((new_i, new_j))
            else:
                for neighbor in find_neighbors(data, new_i, new_j, allow_dups=allow_dups):
                    if allow_dups or neighbor not in ret_list:
                        ret_list.append(neighbor)
    return ret_list


def is_neighbor(data, i, new_j, search_val):
    return 0 <= i < len(data) and 0 <= new_j < len(data[0]) and data[i][new_j] == search_val


class Day10(utils.Day):
    # Converts list of strings into more meaningful data if necessary
    # Only really useful if you think there will be common code used twice
    def process_raw_input(self, raw_input):
        return [[-10 if c == '.' else int(c) for c in line] for line in raw_input]

    def run_part_1(self, data=None, allow_dups=False):
        total = 0
        for i in range(len(data)):
            for j in range(len(data[0])):
                if data[i][j] == 0:
                    total += len(find_neighbors(data, i, j, allow_dups=allow_dups))
        return total

    def run_part_2(self, data=None):
        return self.run_part_1(data, allow_dups=True)

if __name__ == '__main__':
    day = Day10()
    day.run_tests(
        sample_input=True,
        real_input=True,
        part1=True,
        part2=True,
        part_test=False,
    )
