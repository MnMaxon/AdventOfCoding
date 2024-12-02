import aoc_utils as utils


class Day01(utils.Day):
    # Used to test code, run by using Day.run_tests(part_test=True)
    def run_part_test(self, data=None):
        data = super().run_part_test(data)
        return data

    # Converts list of strings into more meaningful data if necessary
    # Only really useful if you think there will be common code used twice
    def process_raw_input(self, raw_input=None):
        raw_input = super().process_raw_input(raw_input)
        left_list = []
        right_list = []
        for line in raw_input:
            left, right = [int(x) for x in line.split("   ")]
            left_list.append(left)
            right_list.append(right)
        return sorted(left_list), sorted(right_list)

    def run_part_1(self, data=None):
        data = super().run_part_1(data)
        left_list, right_list = data
        total = 0
        for i in range(len(left_list)):
            total += abs(right_list[i] - left_list[i])
        return total

    def run_part_2(self, data=None):
        data = super().run_part_2(data)
        left_list, right_list = data
        total = 0
        j = 0
        max_j = len(right_list) - 1
        for i in range(len(left_list)):
            add = 0
            while left_list[i] > right_list[j] and j < max_j:
                j += 1
            while left_list[i] == right_list[j + add] and j < max_j:
                add += 1
            total += add * left_list[i]
        return total


if __name__ == '__main__':
    day = Day01()
    day.run_tests(part_test=False)
