import aoc_utils as utils


def multiply_all(data):
    total = 0
    for section in data.split("mul("):
        sections = section.split(")")
        if len(sections) < 2:
            continue
        section = sections[0]
        left_right = section.split(",")
        if len(left_right) != 2:
            continue
        l = left_right[0]
        r = left_right[1]
        if not l.isnumeric() or not r.isnumeric():
            continue
        total += int(l) * int(r)
    return total


class Day03(utils.Day):
    # Used to test code, run by using Day.run_tests(part_test=True)
    def run_part_test(self, data=None):
        data = super().run_part_test(data)
        return data

    # Converts list of strings into more meaningful data if necessary
    # Only really useful if you think there will be common code used twice
    def process_raw_input(self, raw_input=None):
        raw_input = super().process_raw_input(raw_input)
        # TODO Process raw data, given strings separated by new lines
        return raw_input

    def run_part_1(self, data=None):
        data = super().run_part_1(data)
        data = " ".join(data)
        total = multiply_all(data)
        return total

    def run_part_2(self, data=None):
        data = super().run_part_2(data)
        data = " ".join(data)
        sections = data.split("don't()")
        enabled_sections = [sections.pop(0)]
        for section in sections:
            do_split = section.split("do()", 1)
            if len(do_split) != 2:
                continue
            enabled_sections.append(do_split[1])
        return multiply_all(" ".join(enabled_sections))


if __name__ == '__main__':
    print(" 3".isnumeric())
    day = Day03()
    day.run_tests(test_input=True)
