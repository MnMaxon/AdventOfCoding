import aoc_utils as utils

def get_base_points(cards):
    count_d = {}
    for c in cards:
        count_d[c] = count_d.get(c, 0) + 1
    max_count = max(count_d.values())
    if max_count >= 4:  # 5/4 of a kind
        return max_count + 1
    if max_count == 3:  # 3 of a kind / full house
        if 2 in count_d.values():
            return 4
        return 3
    if max_count == 2:  # one/two pair
        value_count = {}
        for v in count_d.values():
            value_count[v] = value_count.get(v, 0) + 1
        return value_count[2]
    return 0  # high card

def get_points_joker(cards):
    # print("==",cards)
    count_d = {}
    for c in cards:
        count_d[c] = count_d.get(c, 0) + 1
    # print(count_d)
    jokers = count_d.get(1, 0)
    count_d[1] = 0
    max_count = max(count_d.values())
    for card,count in count_d.items():
        if count == max_count:
            count_d[card] += jokers
            break
    max_count = max(count_d.values())
    if max_count >= 4:  # 5/4 of a kind
        return max_count + 1
    if max_count == 3:  # 3 of a kind / full house
        if 2 in count_d.values():
            return 4
        return 3
    if max_count == 2:  # one/two pair
        value_count = {}
        for v in count_d.values():
            value_count[v] = value_count.get(v, 0) + 1
        return value_count[2]
    return 0  # high card


class Day07(utils.Day):
    # Used to test code, run by using Day.run_tests(part_test=True)
    def run_part_test(self, data=None):
        data = super().run_part_test(data)
        return data

    # Converts list of strings into more meaningful data if necessary
    # Only really useful if you think there will be common code used twice
    def process_raw_input(self, raw_input=None):
        raw_input = super().process_raw_input(raw_input)
        return [s.split(" ") for s in raw_input]

    def run_part_1(self, data=None):
        data = super().run_part_1(data)
        all_card_s = "23456789TJQKA"
        card_map = {all_card_s[i]: i + 2 for i in range(len(all_card_s))}
        data = [([card_map[c] for c in cards], int(bid)) for cards, bid in data]
        # point_list = [(get_points(cards), bid) for cards, bid in data]
        point_list = [(get_base_points(cards), cards, bid) for cards, bid in data]
        point_list = sorted(point_list)
        total = 0
        for i in range(len(point_list)):
            total += point_list[i][-1] * (i + 1)
        # TODO Finish part 1 of the task
        return total, point_list

    def run_part_2(self, data=None):
        data = super().run_part_2(data)
        all_card_s = "J23456789TQKA"
        card_map = {all_card_s[i]: i + 1 for i in range(len(all_card_s))}
        data = [([card_map[c] for c in cards], int(bid)) for cards, bid in data]
        point_list = [(get_points_joker(cards), cards, bid) for cards, bid in data]
        point_list = sorted(point_list)
        total=0
        for i in range(len(point_list)):
            total += point_list[i][-1] * (i + 1)
        return total, point_list


if __name__ == '__main__':
    day = Day07()
    day.run_tests(part_test=False)
