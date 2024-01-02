from pprint import pprint

import aoc_utils as utils


def extrapolate(nums):
    ret = [nums]
    if not all([n == 0 for n in nums]):
        ret.extend(extrapolate([nums[i + 1] - nums[i] for i in range(len(nums) - 1)]))
    return ret


class Day09(utils.Day):
    # Used to test code, run by using Day.run_tests(part_test=True)
    def run_part_test(self, data=None):
        data = super().run_part_test(data)
        return data

    # Converts list of strings into more meaningful data if necessary
    # Only really useful if you think there will be common code used twice
    def process_raw_input(self, raw_input=None):
        raw_input = super().process_raw_input(raw_input)
        data = super().run_part_1(raw_input)
        data = [[int(x) for x in l.split()] for l in data]
        data = [extrapolate(l) for l in data]
        # TODO Process raw data, given strings separated by new lines
        return data

    def run_part_1(self, data=None):
        for extrapolated in data:
            for i in reversed(range(len(extrapolated) - 1)):
                extrapolated[i].append(extrapolated[i][-1] + extrapolated[i + 1][-1])
        return sum([l[0][-1] for l in data])

    def run_part_2(self, data=None):
        data = super().run_part_2(data)
        for extrapolated in data:
            for i in reversed(range(len(extrapolated) - 1)):
                extrapolated[i].insert(0, extrapolated[i][0] - extrapolated[i + 1][0])
        return sum([l[0][0] for l in data])


if __name__ == '__main__':
    day = Day09()
    day.run_tests(part_test=False)
