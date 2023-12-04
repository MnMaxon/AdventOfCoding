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
        data = []
        for line in raw_input:
            elves = line.split(",")
            data.append([[int(section) for section in elf.split('-')] for elf in elves])
        return data

    def run_part_1(self, data=None):
        data = super().run_part_1(data)
        count = 0
        for e1, e2 in data:
            if e1[0] <= e2[0] and e1[1] >= e2[1] or e1[0] >= e2[0] and e1[1] <= e2[1]:
                count += 1
        return count

    def run_part_2(self, data=None):
        data = super().run_part_2(data)
        count = 0
        for e1, e2 in data:
            sort = sorted(e1 + e2)
            if e1[0] in e2 or e1[1] in e2 or not (sort == e1 + e2 or sort == e2 + e1):
                count += 1
        return count


if __name__ == '__main__':
    day = Day04()
    day.run_tests(part_test=False)
