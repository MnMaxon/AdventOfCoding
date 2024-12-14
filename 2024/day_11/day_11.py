import aoc_utils as utils


class Day11(utils.Day):
    total = ""
    answers = {}
    # Used to test code, run by using Day.run_tests(part_test=True)
    def run_part_test(self, data=None):
        data = super().run_part_test(data)
        return data

    def count_stones(self, num, times):
        key = (num, times)
        if key in self.answers:
            return self.answers[key]
        s = str(num)
        if times == 0:
            # self.total += s + " "
            return 1
        times -= 1
        l = len(s)
        if num == 0:
            answer = self.count_stones(1, times)
        elif l % 2 == 0:
            left = int(s[:l // 2])
            right = int(s[l // 2:])
            answer = self.count_stones(left, times) + self.count_stones(right, times)
        else:
            answer = self.count_stones(num * 2024, times)
        self.answers[key] = answer
        return answer

    # Converts list of strings into more meaningful data if necessary
    # Only really useful if you think there will be common code used twice
    def process_raw_input(self, raw_input):
        return [int(x) for x in raw_input[0].split(' ')]

    def run_part_1(self, data=None):
        r =  sum([self.count_stones(x, 25) for x in data])
        # print("total", self.total)
        return r

    def run_part_2(self, data=None):
        return sum([self.count_stones(x, 75) for x in data])


if __name__ == '__main__':
    day = Day11()
    day.run_tests(
        sample_input=True,
        real_input=True,
        part1=True,
        part2=True,
        part_test=False,
    )
