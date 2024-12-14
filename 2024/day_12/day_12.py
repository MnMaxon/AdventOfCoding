import aoc_utils as utils

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def count_sides(data, i, j, wall_dir_key, banned_dir_list):
    # sides = 0
    # for dir_key in range(len(dirs)):
    #     cur_banned_dirs = banned_dir_list[dir_key]
    #     d = dirs[dir_key]
    #     if d in cur_banned_dirs:
    #         continue
    #     cur_banned_dirs.append((i, j))
    #     new_i, new_j = i + d[0], j + d[1]
    #     char = data[i][j]
    #     if is_different(data, new_i, new_j, char):
    #         sides += 1
    #         left_dir_key = (dir_key + 1) % 4
    #         right_dir_key = (dir_key - 1) % 4
    #         for l_r_key in [left_dir_key, right_dir_key]:
    #             ban_i = i + dirs[l_r_key][0]
    #             ban_j = j + dirs[l_r_key][1]
    #             while not is_different(data, ban_i, ban_j, char) and is_different(data, ban_i +d[0], ban_j + d[1], char):
    #                 cur_banned_dirs.append((ban_i, ban_j))
    #                 ban_i += dirs[l_r_key][0]
    #                 ban_j += dirs[l_r_key][1]
    # return sides
    cur_banned_dirs = banned_dir_list[wall_dir_key]
    origin_key = (i, j)
    if origin_key in cur_banned_dirs:
        return 0
    cur_banned_dirs.append(origin_key)
    char = data[i][j]
    wall_dir = dirs[wall_dir_key]
    if not is_different(data, i + wall_dir[0], j + wall_dir[1], char):
        return 0
    left_dir_key = (wall_dir_key + 1) % 4
    right_dir_key = (wall_dir_key - 1) % 4
    for l_r_key in [left_dir_key, right_dir_key]:
        ban_i = i + dirs[l_r_key][0]
        ban_j = j + dirs[l_r_key][1]
        while not is_different(data, ban_i, ban_j, char) and is_different(data, ban_i + wall_dir[0],
                                                                          ban_j + wall_dir[1], char):
            cur_banned_dirs.append((ban_i, ban_j))
            ban_i += dirs[l_r_key][0]
            ban_j += dirs[l_r_key][1]
    return 1


def print_data(data, banned_dir_list=None):
    if banned_dir_list is None:
        banned_dir_list = []
    walls = {}
    for wall_dir_key in range(len(banned_dir_list)):
        print(wall_dir_key)
        wall_dir = dirs[wall_dir_key]
        for cur_loc in banned_dir_list[wall_dir_key]:
            wall = (cur_loc[0] + wall_dir[0], cur_loc[1] + wall_dir[1])
            walls[wall] = walls.get(wall, 0) + 1
    for i in range(len(data)):
        row = ""
        for j in range(len(data[0])):
            row += str(walls.get((i, j), data[i][j]))
        print(row)
    print()


all_banned = [[], [], [], []]


def count(data, i, j, counted, banned_dirs=None):
    global all_banned
    all_banned = banned_dirs
    coords = (i, j)
    if i < 0 or j < 0 or i >= len(data) or j >= len(data[0]) or coords in counted:
        return 0, 0
    counted.append(coords)
    char = data[i][j]
    area = 1
    perim = 0
    for dir_key in range(len(dirs)):
        d = dirs[dir_key]
        new_i, new_j = i + d[0], j + d[1]
        if is_different(data, new_i, new_j, char):
            if banned_dirs is None:
                perim += 1
            else:
                perim += count_sides(data, i, j, dir_key, banned_dirs)
        else:
            a, p = count(data, new_i, new_j, counted, banned_dirs)
            area += a
            perim += p
    return area, perim


def is_different(data, i, j, char):
    return i < 0 or j < 0 or i >= len(data) or j >= len(data[0]) or data[i][j] != char


class Day12(utils.Day):

    def run_part_1(self, data=None):
        total = 0
        counted = []
        for i in range(len(data)):
            for j in range(len(data[0])):
                area, perim = count(data, i, j, counted)
                total += area * perim
        return total

    def run_part_2(self, data=None):
        # TODO Finish part 2 of the task
        total = 0
        counted = []
        for i in range(len(data)):
            for j in range(len(data[0])):
                area, perim = count(data, i, j, counted, [[], [], [], []])
                # if area != 0:
                    # print(f"A region of {data[i][j]} plants with the price {area} * {perim} = {area * perim}.")
                    # print(all_banned)
                    # print_data(data, all_banned)
                total += area * perim
        return total


if __name__ == '__main__':
    day = Day12()
    day.run_tests(
        sample_input=True,
        real_input=True,
        part1=True,
        part2=True,
        part_test=False,
    )
