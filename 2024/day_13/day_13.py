import dataclasses

import aoc_utils as utils
from aoc_utils import Coordinate


@dataclasses.dataclass
class Machine:
    a: Coordinate
    b: Coordinate
    prize: Coordinate
    a_cost: int = 3
    b_cost: int = 1

    def get_min_cost(self):
        c1 = self.a.x - self.a.y
        c2 = self.b.x - self.b.y
        c3 = self.prize.x - self.prize.y
        c4 = self.prize.x/self.b.x
        c5 = self.a.x / self.b.x
        i = (c3 - c2 * c4) / (c1 - c2 * c5)
        j = (self.prize.x - self.a.x * i) / self.b.x
        i = round(i, 0)
        j = round(j, 0)
        i = int(i)
        j = int(j)
        if self.a.x * i + self.b.x * j == self.prize.x and self.a.y * i + self.b.y * j == self.prize.y:
            return self.get_cost(i, j)
        return 0

    def get_min_cost_old(self):
        # This is just a system of equations that can be solved, not sure why I thought there could be multiple answers for i and j.
        # They really got me with the 'minimum tokens'
        i = 100
        while i > 0:  # I think <=, doesn't seem like it matters between < and <= here
            goal = self.prize - self.a * i
            if goal % self.b == 0:
                j = goal // self.b
                if j.x == j.y:
                    j = j.x
                    return self.get_cost(i, j)
            i -= 1
        return 0
    def get_cost(self, i, j):
        return self.a_cost * i + self.b_cost * j


def process_line(line):
    if "" == line:
        return None
    line = line.replace(",", "").replace("+", "").replace("=", "").replace("X", "").replace("Y", "").replace("n ", "")
    coords = line.split(" ")
    return Coordinate(int(coords[1]), int(coords[2]))


class Day13(utils.Day):
    # Converts list of strings into more meaningful data if necessary
    # Only really useful if you think there will be common code used twice
    def process_raw_input(self, raw_input):
        a = None
        b = None
        prize = None
        machines = []
        raw_input.append("")
        for i in range(len(raw_input)):
            line = raw_input[i]
            if line == "":
                machines.append(Machine(a, b, prize))
                a = None
                b = None
                prize = None
                continue
            coords = process_line(line)
            if "Button A" in line:
                a = coords
            elif "Button B" in line:
                b = coords
            elif "Prize" in line:
                prize = coords
            else:
                raise ValueError("Invalid line: " + line)
        return machines

    def run_part_1(self, data=None):
        all_min_costs = [machine.get_min_cost() for machine in data]
        all_min_costs_old = [machine.get_min_cost_old() for machine in data]
        for i in range(max(len(all_min_costs), len(all_min_costs_old))):
            s = ""
            if i < len(all_min_costs):
                s += str(all_min_costs[i])
            s += " "
            if i < len(all_min_costs_old):
                s += str()
            # if all_min_costs[i] != all_min_costs_old[i]:
        ans = sum(all_min_costs)
        return ans

    def run_part_2(self, data=None):
        for machine in data:
            machine.prize += 10000000000000
        ans = self.run_part_1(data)
        return ans


if __name__ == '__main__':
    day = Day13()
    day.run_tests(
        sample_input=True,
        real_input=True,
        part1=True,
        part2=True,
        part_test=False,
    )
