import aoc_utils as utils


def first_unique(data: str, count):
    for i in range(len(data) - count + 1):
        if len(set(data[i:i + count])) == count:
            return i + count
    return data


class Day06(utils.Day):
    # Used to test code, run by using Day.run_tests(part_test=True)
    def run_part_test(self, data=None):
        data = super().run_part_test(data)
        return data

    # Converts list of strings into more meaningful data if necessary
    # Only really useful if you think there will be common code used twice
    def process_raw_input(self, raw_input=None):
        raw_input = super().process_raw_input(raw_input)
        return raw_input[0]

    def run_part_1(self, data=None):
        return first_unique(data, 4)

    def run_part_2(self, data=None):
        data = super().run_part_2(data)
        return first_unique(data, 14)


if __name__ == '__main__':
    day = Day06()
    day.run_tests(part_test=False)
