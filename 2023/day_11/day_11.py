from pprint import pprint

import aoc_utils as utils

def map_points(data, space_dist, i_empties=None, j_empties=None):
    if i_empties is None:
        i_empties = []
    if j_empties is None:
        j_empties = []
    mapping = {}
    i_count = 0
    for i in range(len(data)):
        if i in i_empties:
            i_count+=space_dist
        else:
            i_count+=1
        j_count = 0
        for j in range(len(data[i])):
            if j in j_empties:
                j_count+=space_dist
            else:
                j_count+=1
            if data[i][j] != 0:
                mapping[data[i][j]] = (i_count,j_count)
    return mapping

def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def expand(data):
    for i in reversed(range(len(data))):
        if all([0 == x for x in data[i]]):
            data.insert(i, [0] * len(data[i]))
    for j in reversed(range(len(data[0]))):
        vert = [data[i][j] for i in range(len(data))]
        if all([0 == x for x in vert]):
            for i in range(len(data)):
                data[i].insert(j, 0)
def get_empty(data):
    i_empty = []
    j_empty = []
    for i in range(len(data)):
        if all([0 == x for x in data[i]]):
            i_empty.append(i)
    for j in range(len(data[0])):
        vert = [data[i][j] for i in range(len(data))]
        if all([0 == x for x in vert]):
            j_empty.append(j)
    return i_empty, j_empty


def total_distances(mapping):
    total = 0
    for index, point in mapping.items():
        for other_index, other_point in mapping.items():
            if other_index > index:
                total += dist(point, other_point)
    return total


class Day11(utils.Day):
    # Used to test code, run by using Day.run_tests(part_test=True)
    def run_part_test(self, data=None):
        data = super().run_part_test(data)
        return data

    # Converts list of strings into more meaningful data if necessary
    # Only really useful if you think there will be common code used twice
    def process_raw_input(self, raw_input=None):
        raw_input = super().process_raw_input(raw_input)
        data = []
        cur_num = 1
        for line in raw_input:
            cur_data = []
            for c in line:
                if c == '.':
                    cur_data.append(0)
                else:
                    cur_data.append(cur_num)
                    cur_num +=1
            data.append(cur_data)
        return data

    def run_part_1(self, data=None):
        data = super().run_part_1(data)
        i_empty, j_empty = get_empty(data)
        mapping = map_points(data, 2, i_empty, j_empty)
        total = total_distances(mapping)
        return total

    def run_part_2(self, data=None):
        data = super().run_part_2(data)
        i_empty, j_empty = get_empty(data)
        mapping = map_points(data, 1000000, i_empty, j_empty)
        total = total_distances(mapping)
        return total


if __name__ == '__main__':
    day = Day11()
    day.run_tests(part_test=False)
