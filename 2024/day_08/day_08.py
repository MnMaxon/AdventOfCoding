import aoc_utils as utils
import math


def get_antennas_by_freq(data):
    locs = {}
    for i in range(len(data)):
        for j in range(len(data[0])):
            c = data[i][j]
            if c == '.':
                continue
            antennas = locs.get(c, [])
            antennas.append((i, j))
            locs[c] = antennas
    return locs


def in_radar(point, data):
    return 0 <= point[0] < len(data) and 0 <= point[1] < len(data[0])


def append_to_all_antinodes(all_antinodes, antinodes, data):
    antinodes = [antinode for antinode in antinodes if in_radar(antinode, data)]
    for antinode in antinodes:
        if antinode not in all_antinodes:
            all_antinodes.append(antinode)


class Day08(utils.Day):
    # Used to test code, run by using Day.run_tests(part_test=True)
    def run_part_test(self, data=None):
        data = super().run_part_test(data)
        return data

    # Converts list of strings into more meaningful data if necessary
    # Only really useful if you think there will be common code used twice
    def process_raw_input(self, raw_input):
        # TODO Process raw data, given strings separated by new lines
        return raw_input

    def run_part_1(self, data=None):
        all_antinodes = []
        for freq, antennas in get_antennas_by_freq(data).items():
            for antenna_i in range(len(antennas)):
                cur_antenna = antennas[antenna_i]
                for antenna_j in range(antenna_i + 1, len(antennas)):
                    other_antenna = antennas[antenna_j]
                    dist = ((cur_antenna[0] - other_antenna[0]), (cur_antenna[1] - other_antenna[1]))

                    antinodes = [
                        (cur_antenna[0] + dist[0], cur_antenna[1] + dist[1]),
                        (other_antenna[0] - dist[0], other_antenna[1] - dist[1])
                    ]
                    append_to_all_antinodes(all_antinodes, antinodes, data)

        return len(all_antinodes)

    def run_part_2(self, data=None):

        all_antinodes = []
        for freq, antennas in get_antennas_by_freq(data).items():
            for antenna_i in range(len(antennas)):
                cur_antenna = antennas[antenna_i]
                for antenna_j in range(antenna_i + 1, len(antennas)):
                    other_antenna = antennas[antenna_j]
                    dist = ((cur_antenna[0] - other_antenna[0]), (cur_antenna[1] - other_antenna[1]))
                    div = int(math.gcd(abs(dist[0]), abs(dist[1])))
                    dist = (int(dist[0] / div), int(dist[1] / div))
                    antinodes = []
                    for sign in [-1, 1]:
                        i = 0
                        while in_radar((cur_antenna[0] + sign * i * dist[0], cur_antenna[1] + sign * i * dist[1]),
                                       data):
                            antinodes.append((cur_antenna[0] + sign * i * dist[0], cur_antenna[1] + sign * i * dist[1]))
                            i += 1
                    append_to_all_antinodes(all_antinodes, antinodes, data)

        print_l_s = []
        for i in range(len(data)):
            print_l = ''
            for j in range(len(data[0])):
                # if (i, j) in all_antinodes:
                #     print_l += '#'
                #     continue
                if data[i][j] == '.':
                    if (i, j) in all_antinodes:
                        print_l += '#'
                    else:
                        print_l += '.'
                else:
                    print_l += data[i][j]
            # print(print_l)
            print_l_s.append(print_l)

        # for antinode in all_antinodes:
        #     print(antinode, print_l_s[antinode[0]][antinode[1]])

        return len(all_antinodes)


if __name__ == '__main__':
    day = Day08()
    day.run_tests(
        sample_input=True,
        real_input=True,
        part1=True,
        part2=True,
        part_test=False,
    )
