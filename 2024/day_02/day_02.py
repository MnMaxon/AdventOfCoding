import aoc_utils as utils


class Day02(utils.Day):
    # Used to test code, run by using Day.run_tests(part_test=True)
    def run_part_test(self, data=None):
        data = super().run_part_test(data)
        return data

    # Converts list of strings into more meaningful data if necessary
    # Only really useful if you think there will be common code used twice
    def process_raw_input(self, raw_input=None):
        raw_input = super().process_raw_input(raw_input)
        return [[int(x) for x in line.split()] for line in raw_input]

    def run_part_1(self, data=None):
        data = super().run_part_1(data)
        total = 0
        for l in data:
            if l[0] < l[1]:
                valid =[-1, -2, -3]
            else:
                valid = [1, 2, 3]
            safe = self.is_safe(l, valid)
            if safe:
                total += 1
        return total

    def is_safe(self, numbers, valid, mistakes=1):
        if mistakes == 0:
            return False
        for i in range(len(numbers) - 1):
            if numbers[i] - numbers[i + 1] not in valid:
                numbers = list(numbers)
                numbers2 = list(numbers)
                numbers.pop(i)
                numbers2.pop(i + 1)
                return self.is_safe(numbers, valid, mistakes - 1) or self.is_safe(numbers2, valid, mistakes - 1)
        return True

    def run_part_2(self, data=None):
        data = super().run_part_2(data)
        total = 0
        for l in data:
            if self.is_safe(l, [-1, -2, -3], 2) or self.is_safe(l, [1, 2, 3], 2):
                total += 1
        return total


if __name__ == '__main__':
    day = Day02()
    day.run_tests(part_test=False)
