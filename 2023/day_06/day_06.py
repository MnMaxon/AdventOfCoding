import math

import aoc_utils as utils


# x * (t - x) = -xx + tx
def calc_dist(time, total_time):
    return time * (total_time - time)


# -xx + tx = d
# -xx + tx - d = 0 = axx + bx + c
def quad(total_time, record):
    a = -1
    b = total_time
    c = -1 * record
    return [(-b + sign * math.sqrt(b * b - 4 * a * c)) / (2 * a) for sign in [1, -1]]


def num_list(s):
    ret = []
    for num in s.split(" "):
        try:
            ret.append(int(num))
        except Exception:
            pass
    return ret


class Day06(utils.Day):

    def run_part_1(self, data=None):
        data = super().run_part_1(data)
        data = [num_list(s) for s in data]
        data = [[data[0][i], data[1][i]] for i in range(len(data[0]))]
        times = [[calc_dist(i, time) for i in range(time) if calc_dist(i, time) > record] for time, record in data]
        return math.prod([len(win_times) for win_times in times])

    def run_part_2(self, data=None):
        data = super().run_part_2(data)
        time, distance = [int(s.split(":")[1].replace(" ", "")) for s in data]
        left, right = quad(time, distance)
        left = math.ceil(left)
        right = math.floor(right)
        return min(right, time) - max(left, 0) + 1


if __name__ == '__main__':
    day = Day06()
    day.run_tests(part_test=False)
