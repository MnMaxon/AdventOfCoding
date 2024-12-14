import dataclasses

import aoc_utils as utils
from aoc_utils import Coordinate


@dataclasses.dataclass
class Robot:
    pos: Coordinate
    vel: Coordinate

    def calc_pos(self, time, dims):
        pos = self.pos + self.vel * time
        return pos % dims


def get_quadrant(pos: Coordinate, dims: Coordinate):
    center = dims // 2
    if center.x == pos.x or center.y == pos.y:
        return 0
    if pos.x < center.x:
        if pos.y < center.y:
            return 1
        else:
            return 4
    elif pos.y < center.y:
        return 2
    else:
        return 3


class Day14(utils.Day):
    # Converts list of strings into more meaningful data if necessary
    # Only really useful if you think there will be common code used twice
    def process_raw_input(self, raw_input):
        robots = []
        for line in raw_input:
            line = line.replace("p=", "").replace("v=", "")
            split = line.split(" ")
            robots.append(Robot(Coordinate.from_string(split[0]), Coordinate.from_string(split[1])))
        return robots

    def run_part_1(self, data=None, dims=Coordinate(101,103), time=100):
        # Code to test sample input
        # if True:
        #     dims = Coordinate(11, 7)
        positions = [robot.calc_pos(time, dims) for robot in data]
        quads = [get_quadrant(pos, dims) for pos in positions]
        counts = [quads.count(x) for x in range(1,5)]
        prod = 1
        for count in counts:
            prod *= count
        return prod

    def run_part_2(self, data=None, dims=Coordinate(101,103)):

        i = 0
        # find first time when all robots are in different positions
        while len(set([robot.calc_pos(i, dims) for robot in data])) != len(data):
            i += 1

        # second time is also a christmas tree
        # i += 1
        # while len(set([robot.calc_pos(i, dims) for robot in data])) != len(data) :
        #     i += 1

        # display result
        for y in range(dims.y):
            line = ""
            for x in range(dims.x):
                if Coordinate(x, y) in [robot.calc_pos(i, dims) for robot in data]:
                    line += "#"
                else:
                    line += "."
            print(line)
        return i

if __name__ == '__main__':
    day = Day14()
    day.run_tests(
        sample_input=True,
        real_input=True,
        part1=True,
        part2=True,
        part_test=False,
    )
