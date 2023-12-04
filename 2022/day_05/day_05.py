import aoc_utils as utils


class Day05(utils.Day):
    # Used to test code, run by using Day.run_tests(part_test=True)
    def run_part_test(self, data=None):
        data = super().run_part_test(data)
        return data
    def get_raw_input(self, input_path=None, strip=True):
        return super().get_raw_input(input_path, strip=False)

    # Converts list of strings into more meaningful data if necessary
    # Only really useful if you think there will be common code used twice
    def process_raw_input(self, raw_input=None):
        raw_input = super().process_raw_input(raw_input)
        process_move = False
        rows = []
        moves = []
        for s in raw_input:
            if s == "\n":
                process_move = True
            elif process_move:
                for rem in ["move","from","to"]:
                    s = s.replace(rem, "")
                nums = s.strip().split()
                moves.append([int(nums[0]),int(nums[1]) - 1,int(nums[2]) - 1])
            else:
                s = s.replace("    ", "[x]").strip()
                for rem in [" ", "[", "]"]:
                    s = s.replace(" ", "").replace(rem, "")
                if s[0] != '1':
                    rows.append(s)
        size = len(rows[-1])

        containers = []
        for container_num in range(size):
            containers.append([s[container_num] for s in rows if container_num < len(s) and s[container_num] != 'x'])
        return containers, moves

    def run_part_1(self, data=None):
        data = super().run_part_1(data)
        containers, moves = data
        print(''.join([container[0] for container in containers]))

        for amount, from_c, to_c in moves:
            for _ in range(amount):
                containers[to_c].insert(0, containers[from_c].pop(0))
        return ''.join([container[0] for container in containers])

    def run_part_2(self, data=None):
        data = super().run_part_2(data)
        containers, moves = data
        print(''.join([container[0] for container in containers]))

        for amount, from_c, to_c in moves:
            for i in range(amount):
                containers[to_c].insert(i, containers[from_c].pop(0))
        # TODO Finish part 2 of the task
        return ''.join([container[0] for container in containers])


if __name__ == '__main__':
    day = Day05()
    day.run_tests(part_test=False)
