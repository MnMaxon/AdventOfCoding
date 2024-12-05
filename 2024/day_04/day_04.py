import aoc_utils as utils


class Day04(utils.Day):
    # Used to test code, run by using Day.run_tests(part_test=True)
    def run_part_test(self, data=None):
        data = super().run_part_test(data)
        return data

    def run_part_1(self, data=None):
        data = super().run_part_1(data)
        i_max = len(data)
        j_max = len(data[0])
        total = 0
        for i in range(i_max):
            for j in range(j_max):
                for i_mult in [1, 0, -1]:
                    for j_mult in [1, 0, -1]:
                        if i_mult == 0 and j_mult == 0:
                            continue
                        if matches(i, j, i_mult, j_mult, data, "XMAS"):
                            total += 1
        return total

    def run_part_2(self, data=None):
        data = super().run_part_1(data)
        nums = []
        # Converting to numbers, so I can just add them and see if they equal 3 instead of checking for S and M
        for i in range(len(data)):
            cur = []
            for j in range(len(data[0])):
                c = data[i][j]
                if c == "S":
                    cur.append(1)
                elif c == "M":
                    cur.append(2)
                else:
                    cur.append(50)
            nums.append(cur)
        i_max = len(data) - 1
        j_max = len(data[0]) - 1
        total = 0
        for i in range(1, i_max):
            for j in range(1, j_max):
                if data[i][j] == 'A' and nums[i + 1][j + 1] + nums[i - 1][j - 1] == 3 and nums[i - 1][j + 1] + \
                        nums[i + 1][j - 1] == 3:
                    total += 1
        return total


def matches(i, j, i_mult, j_mult, data, word):
    if len(word) == 0:
        return True
    if i < 0 or j < 0 or i >= len(data) or j >= len(data[0]) or data[i][j] != word[0]:
        return False
    return matches(i + i_mult, j + j_mult, i_mult, j_mult, data, word[1:])


if __name__ == '__main__':
    day = Day04()
    day.run_tests(part_test=False)
