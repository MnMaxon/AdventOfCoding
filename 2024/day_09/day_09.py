import aoc_utils as utils


class Day09(utils.Day):
    # Used to test code, run by using Day.run_tests(part_test=True)
    def run_part_test(self, data=None):
        data = super().run_part_test(data)
        return data

    # Converts list of strings into more meaningful data if necessary
    # Only really useful if you think there will be common code used twice
    def process_raw_input(self, raw_input):
        return [[int(c) for c in line] for line in raw_input][0]

    def run_part_1(self, data):
        i = 0
        j = len(data) - 1
        total = 0
        position = 0

        while i <= j:
            if j % 2 == 1 or data[j] == 0:
                j -= 1  # Ignore blank spaces
                continue
            if data[i] == 0:
                i += 1
                continue
            if i % 2 == 0:
                file_id = i / 2
                for _ in range(data[i]):
                    total += position * file_id
                    position += 1
                i += 1
                continue
            if i % 2 == 1:
                file_id = j / 2
                diff = min(data[j], data[i])
                for _ in range(diff):
                    total += position * file_id
                    position += 1
                data[i] -= diff
                data[j] -= diff
        return total

    def run_part_2(self, data=None):
        data = [[index, data[index]] for index in range(len(data))]
        j = len(data) - 1
        while j >= 0:
            to_move = data[j]
            if to_move[1] == 0 or to_move[0] % 2 == 1:
                j -= 1
                continue
            found = False
            for i in range(j):
                if data[i][1] == 0 or data[i][0] % 2 == 0 or data[i][1] < to_move[1]:
                    continue
                # debug_line(data)
                found = True
                data[i][1] -= to_move[1]
                data.insert(i, data.pop(j))
                data.insert(j + 1, [99, to_move[1]])
                break
            if found:
                continue
            j -= 1

        # debug_line(data)
        total = 0
        position = 0
        for index, size in data:
            if index % 2 == 1:
                position += size
                continue
            for _ in range(size):
                total += position * (index / 2)
                position += 1
        return total


def debug_line(line):
    s = ""
    for index, size in line:
        for _ in range(size):
            if index % 2 == 0:
                s += str(index / 2)
            else:
                s += "."
    print(s)


if __name__ == '__main__':
    day = Day09()
    day.run_tests(
        sample_input=True,
        real_input=True,
        part1=True,
        part2=True,
        part_test=False,
    )
