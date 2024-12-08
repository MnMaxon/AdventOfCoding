import aoc_utils as utils


def possible_part_1(total, nums):
    if len(nums) == 0:
        return total == 0
    # make sure total is not a float
    if total < 0 or total % 1 != 0:
        return False
    x = nums[-1]
    if possible_part_1(total - x, nums[:-1]) or possible_part_1(total / x, nums[:-1]):
        return True
    return False


def run_all(nums, total=0):
    if len(nums) == 0:
        return [total]
    mod = nums[0]
    ret = run_all(nums[1:], total + mod)
    ret += run_all(nums[1:], total * mod)
    ret += run_all(nums[1:], int(str(total) + str(mod)))
    return ret


class Day07(utils.Day):

    # Converts list of strings into more meaningful data if necessary
    # Only really useful if you think there will be common code used twice
    def process_raw_input(self, raw_input):
        data = []
        for line in raw_input:
            total, nums = line.split(":")
            nums = [int(x) for x in nums.strip().split(" ")]
            data.append((int(total), nums))
        return data

    def run_part_1(self, data=None):
        ret_total = 0
        for i in range(len(data)):
            total, nums = data[i]
            if possible_part_1(total, nums):
                ret_total += total
        return ret_total

    def run_part_2(self, data=None):
        ret_total = 0
        for i in range(len(data)):
            total, nums = data[i]
            if total in run_all(nums):
                ret_total += total
        return ret_total


if __name__ == '__main__':
    day = Day07()
    day.run_tests(
        sample_input=True,
        real_input=True,
        part1=True,
        part2=True,
        part_test=False,
    )
