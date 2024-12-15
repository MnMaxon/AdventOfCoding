import aoc_utils as utils


class DayDayHere(utils.Day):
    # Converts list of strings into more meaningful data if necessary
    def process_raw_input(self, raw_input: list[str]):
        # _TODO Process data from a list of strings into a common data structure used for all parts (or delete this)
        return raw_input

    def run_part_1(self, data):
        # _TODO Finish part 1 of the task
        return data

    def run_part_2(self, data):
        # _TODO Finish part 2 of the task
        return data


if __name__ == '__main__':
    day = DayDayHere()
    day.run_tests(
        sample_input=True,
        real_input=True,
        part1=True,
        part2=True,
        part_test=False,
    )
