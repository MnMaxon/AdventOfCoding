import dataclasses

import aoc_utils
import aoc_utils as utils

dirs = {
    '^': aoc_utils.Coordinate(0, -1),
    'v': aoc_utils.Coordinate(0, 1),
    '<': aoc_utils.Coordinate(-1, 0),
    '>': aoc_utils.Coordinate(1, 0),
}


def score(x, y):
    return x + y * 100


@dataclasses.dataclass
class Grid:
    lines: [str]
    player: aoc_utils.Coordinate
    moves: str
    is_double = False

    def get_char(self, loc):
        return self.lines[loc.y][loc.x]

    def print(self, extra=None, extra_char='X'):
        for i in range(len(self.lines)):
            line = self.lines[i]
            if i == self.player.y:
                line = line[:self.player.x] + '@' + line[self.player.x + 1:]
            if extra is not None and i == extra.y:
                line = line[:extra.x] + extra_char + line[extra.x + 1:]
            print(line)

    def is_box(self, loc):
        return self.lines[loc.y][loc.x] in ['O', '[', ']']

    def get_box(self, loc):
        if not self.is_box(loc):
            return None
        if self.lines[loc.y][loc.x] == ']':
            return [loc + aoc_utils.Coordinate(-1, 0), loc]
        if self.lines[loc.y][loc.x] == '[':
            return [loc, loc + aoc_utils.Coordinate(1, 0)]
        return [loc]

    def get_collisions(self, loc, facing):
        collisions = set()
        locs = self.get_box(loc)
        for box in locs:
            new_loc = box + facing
            if self.is_box(new_loc):
                new_box = self.get_box(new_loc)[0]
                if new_box not in locs:
                    collisions.add(new_box)
            else:
                collisions.add(new_loc)
        return collisions

    def push(self, loc, facing):
        if not self.is_box(loc):
            raise ValueError("Can't push - not a box")
        loc = self.get_box(loc)[0]
        # if facing == dirs['>']:
        #     self.print(loc, '>')  # Debugging
        collisions = self.get_collisions(loc, facing)
        if any(self.get_char(c) == '#' for c in collisions):
            wall = [c for c in collisions if self.get_char(c) == '#'][0]
            # self.print(wall)
            return False
        any_box = False
        for coll in collisions:
            if self.is_box(coll):
                any_box = True
                if not self.push(coll, facing):
                    return False
        if any_box:
            collisions = self.get_collisions(loc, facing)
        if any(self.get_char(c) != '.' for c in collisions):
            raise ValueError("Expected empty space after pushing everything in the way")
        box_locs = self.get_box(loc)
        if facing.x == 1:  # Right
            box_locs = reversed(box_locs)
        for l in box_locs:
            self.swap(l, l + facing)
        return True

    def swap(self, loc1, loc2):
        char1 = self.get_char(loc1)
        char2 = self.get_char(loc2)
        if char1 == char2:
            raise ValueError("Can't swap same character")  # This would be unexpected
        line = self.lines[loc1.y]
        line = line[:loc1.x] + char2 + line[loc1.x + 1:]
        self.lines[loc1.y] = line
        line = self.lines[loc2.y]
        line = line[:loc2.x] + char1 + line[loc2.x + 1:]
        self.lines[loc2.y] = line

    def move(self, direction):
        facing = dirs[direction]
        new_loc = self.player + facing
        new_char = self.get_char(new_loc)
        if new_char == '#':
            return
        elif new_char == '.':
            self.player = new_loc
        elif self.is_box(new_loc):
            orig_lines = [line for line in self.lines]
            if self.push(new_loc, facing):
                self.player = new_loc
            else:
                self.lines = orig_lines

    def calc_score(self):
        total = 0
        for y in range(len(self.lines)):
            line = self.lines[y]
            for x in range(len(line)):
                if line[x] in ['O', '[']:
                    total += score(x, y)
        return total

    def double(self):
        if self.is_double:
            raise Exception("Already doubled")
        self.lines = [line.replace('O', '[]').replace('.', '..').replace('#', '##') for line in self.lines]
        self.player.x *= 2


class Day15(utils.Day):
    def process_raw_input(self, raw_input):
        i = 0
        while raw_input[i] != "":
            i += 1
        grid = raw_input[:i]
        moves = ''.join(raw_input[i:])
        player = None
        for i in range(len(grid)):
            line = grid[i]
            if '@' in line:
                player = aoc_utils.Coordinate(line.index('@'), i)
                grid[i] = line.replace('@', '.')
                break
        return Grid(lines=grid, player=player, moves=moves)

    def run_part_1(self, grid: Grid):
        for move in grid.moves:
            grid.move(move)
        return grid.calc_score()

    def run_part_2(self, grid: Grid):
        grid.double()
        return self.run_part_1(grid)


if __name__ == '__main__':
    day = Day15()
    day.run_tests(
        sample_input=True,
        test_input=True,
        real_input=True,
        part1=True,
        part2=True,
        part_test=False,
    )
