from pprint import pprint

import aoc_utils as utils
import numpy as np

all_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num_map = {num + 1: all_letters[num] for num in range(len(all_letters))}
letter_map = {all_letters[num]: num + 1 for num in range(len(all_letters))}


def str_to_num(s):
    total = 0
    for c in s[::-1]:
        total *= 100
        total += letter_map[c]
    return total


class Day08(utils.Day):
    # Used to test code, run by using Day.run_tests(part_test=True)
    def run_part_test(self, data=None):
        data = super().run_part_test(data)
        return data

    # Converts list of strings into more meaningful data if necessary
    # Only really useful if you think there will be common code used twice
    def process_raw_input(self, raw_input=None):
        raw_input = super().process_raw_input(raw_input)
        instructions = []
        for c in raw_input[0]:
            if c == 'R':
                instructions.append(1)
            else:
                instructions.append(0)
        data = [s.replace("=", ",").replace(" ", "").replace("(", "").replace(")", "").split(",") for s in
                raw_input[2:]]
        data = {from_s: (left, right) for from_s, left, right in data}
        return instructions, data

    def run_part_1(self, data=None):
        instructions, data = super().run_part_1(data)
        instruction_len = len(instructions)
        i = 0
        cur = 'AAA'
        while cur != 'ZZZ':
            cur = data[cur][instructions[i % instruction_len]]
            i += 1
        return i

    def run_part_2(self, data=None):
        min_z = str_to_num('AAZ')
        max_a = str_to_num('ZZA')
        instructions, data = super().run_part_2(data)
        # data = {str_to_num(from_s): [str_to_num(side) for side in to_list] for from_s, to_list in data.items()}
        print(len(data.keys()), len(set([l for l, _ in data.values()])), len(set([r for _, r in data.values()])))
        instruction_len = len(instructions)
        print("instruction_len", instruction_len)
        node_info = {}
        for s in data.keys():
            if not s.endswith('A'):
                continue
            i = 0
            z_list = []
            z_vals = []
            cur = s
            mod_dic = {m: [] for m in range(instruction_len)}
            while cur not in mod_dic[i % instruction_len]:
                ins_index = i % instruction_len
                mod_dic[ins_index].append(cur)
                if cur.endswith('Z'):
                    z_list.append(i)
                    z_vals.append(cur)
                cur = data[cur][instructions[ins_index]]
                i += 1
            print(cur, i, z_list, z_vals)
            node_info[cur] = {"repeats_every": z_list[0], "cur": 0, "z_loc": z_list[0]}
            if z_list[0] == 0:
                print("0 is not expected at", cur)
                return node_info
        i = 0
        pprint(node_info)
        print("Done")
        # Needs dtype=object because the lcm is bigger than the max int for the real data
        return np.lcm.reduce([n["repeats_every"] for n in node_info.values()], dtype=object)


if __name__ == '__main__':
    day = Day08()
    # day.run_tests(part_test=True)
    day.run_tests(part_test=False, part1=False, sample_input=True, test_input=False)
