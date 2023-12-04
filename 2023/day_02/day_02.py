from typing import Dict

import aoc_utils as utils
from math import prod


class Day02(utils.Day):
    part1_max = {"red": 12, "green": 13, "blue": 14}

    # Used to test code, run by using Day.run_tests(part_test=True)
    def run_part_test(self, data=None):
        data = super().run_part_test(data)
        return data

    # Converts list of strings into more meaningful data if necessary
    # Only really useful if you think there will be common code used twice
    def process_raw_input(self, raw_input=None):
        raw_input = super().process_raw_input(raw_input)
        data = {}
        for s in raw_input:
            game_num, s = s.replace("Game","").split(": ", 1)
            game_num = int(game_num)
            data[game_num] = []
            for bag_s in s.split(';'):
                bag_data: Dict[str,int] = {}
                for block_s in bag_s.split(','):
                    block_num, block_type = block_s.strip().split(' ')
                    bag_data[block_type] = int(block_num)
                data[game_num].append(bag_data)
        return data

    def run_part_1(self, data=None):
        data = super().run_part_1(data)
        total = 0
        for game, bags in data.items():
            possible = True
            for bag in bags:
                for color, amount in self.part1_max.items():
                    if bag.get(color, 0) > amount:
                        possible = False
                        break
            if possible:
                total += game
        return total

    def run_part_2(self, data=None):
        data = super().run_part_2(data)
        total = 0
        for game, bags in data.items():
            game_max = {}
            for bag in bags:
                for color, amount in bag.items():
                    game_max[color] = max(amount, game_max.get(color, 0))
            # print(game, prod(game_max.values()), game_max, bags)
            total += prod(game_max.values())
        return total


if __name__ == '__main__':
    day = Day02()
    day.run_tests(part_test=False)
