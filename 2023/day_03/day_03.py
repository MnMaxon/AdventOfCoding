from typing import Tuple

import aoc_utils as utils
from pprint import pp

symbols = "*+#$%@-/=&"
all_nums = '1234567890'


class Value:
    def __init__(self, val, start: Tuple[int, int]):
        self.val = val
        self.start = start

    def get_surrounding(self, grid):
        grid = grid[max(0, self.start[0] - 1): min(len(grid), self.start[0] + 2)]
        grid = [s[max(0, self.start[1] - 1): min(len(s), self.get_end_j() + 1)] for s in grid]
        return '\n'.join(grid)

    def near_symbol(self, data):
        return any(symbol in self.get_surrounding(data) for symbol in symbols)

    def get_end_j(self):
        return self.start[1] + len(self)

    def __len__(self):
        return len(str(self.val))


def get_values(s: str, start_i=-1):
    vals = []
    for sym in symbols:
        s = s.replace(sym, '.')
    nums = [int(s) for s in s.split('.') if s != '']
    for num in nums:
        if s.find(str(num)) == -1:
            raise ValueError(f"Could not find {num} in {s}")
        vals.append(Value(num, (start_i, s.find(str(num)))))
        s = s.replace(str(num), '.' * len(str(num)), 1)
    return vals


class Day03(utils.Day):

    # Used to test code, run by using Day.run_tests(part_test=True)
    def run_part_test(self, data=None):
        data = super().run_part_test(data)
        return data

    def run_part_1(self, data=None):
        data = super().run_part_1(data)
        print(''.join(set(c for c in ''.join(data) if c not in symbols and c not in all_nums)))

        val_grid = [get_values(data[i], i) for i in range(len(data))]

        all_vals = []
        for val_l in val_grid:
            all_vals.extend(val_l)

        filtered = [v.val for v in all_vals if v.near_symbol(data)]
        return sum(filtered)

    def run_part_2(self, data=None):
        data = super().run_part_2(data, )
        for symbol in symbols.replace("*", ""):
            data = [s.replace(symbol, '.') for s in data]
        val_grid = [get_values(data[i], i) for i in range(len(data))]

        total = 0
        for i in range(len(data)):
            all_vals = []
            # Only checks nearby numbers - greatly improves performance
            for val_l in val_grid[max(0, i - 1):min(len(data), i + 2)]:
                all_vals.extend(val_l)
            for j in range(len(data[0])):
                if data[i][j] != '*':
                    continue
                cur_data = [s.replace("*", '.') for s in data]
                cur_data[i] = cur_data[i][:j] + "*" + cur_data[i][j + 1:]
                gear_vals = [v.val for v in all_vals if v.near_symbol(cur_data)]
                if len(gear_vals) == 2:
                    total += gear_vals[0] * gear_vals[1]

        # TODO Finish part 2 of the task
        return total


if __name__ == '__main__':
    day = Day03()
    day.run_tests(part_test=False)
    # day.run_tests(part_test=False, real_input=False)
