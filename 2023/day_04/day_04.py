import math

import aoc_utils as utils


class Day04(utils.Day):
    # Used to test code, run by using Day.run_tests(part_test=True)
    def run_part_test(self, data=None):
        data = super().run_part_test(data)
        return data

    # Converts list of strings into more meaningful data if necessary
    # Only really useful if you think there will be common code used twice
    def process_raw_input(self, raw_input=None):
        raw_input = super().process_raw_input(raw_input)
        inp = [s.split(": ")[1].replace("  "," ").strip().split(" | ") for s in raw_input]
        inp = [[[int(num) for num in s1.split(" ")], [int(num) for num in s2.split(" ")]] for s1, s2 in inp]
        return inp

    def run_part_1(self, data=None):
        data = super().run_part_1(data)
        winners = [[winner for winner in winning if winner in ours] for winning, ours in data]
        points = [2**(len(cur)-1) for cur in winners if len(cur) > 0]
        return sum(points)

    def run_part_2(self, data=None):
        data = super().run_part_2(data)
        winners = [[winner for winner in winning if winner in ours] for winning, ours in data]
        win_count = [len(cur) for cur in winners]
        copies = [1 for _ in range(len(data))]
        for i in range(len(data)):
            for j in range(win_count[i]):
                copies[i + j + 1] += copies[i]
        return sum(copies)


if __name__ == '__main__':
    day = Day04()
    day.run_tests(part_test=False)
    # day.run_tests(part_test=False, real_input=False)
