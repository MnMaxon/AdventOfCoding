import aoc_utils as utils


class Day___DAY(utils.Day):
    # Used to test code, run by using Day.run_tests(part_test=True)
    def run_part_test(self, data=None):
        data = super().run_part_test(data)
        return data

    # Converts list of strings into more meaningful data if necessary
    # Only really useful if you think there will be common code used twice
    def process_raw_input(self, raw_input):
        # TODO Process raw data, given strings separated by new lines
        return raw_input

    def run_part_1(self, data=None):
        # TODO Finish part 1 of the task
        return data

    def run_part_2(self, data=None):
        # TODO Finish part 2 of the task
        return data


if __name__ == '__main__':
    day = Day___DAY()
    day.run_tests(
        sample_input=True,
        real_input=True,
        part1=True,
        part2=True,
        part_test=False,
    )
