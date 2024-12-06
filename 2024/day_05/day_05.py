import aoc_utils as utils


def setup_before_map(rules):
    before_map = {}  # values must be before key
    for left, right in rules:
        before_right = before_map.get(right, [])
        before_right.append(left)
        before_map[right] = before_right
    return before_map


class Day05(utils.Day):
    # Used to test code, run by using Day.run_tests(part_test=True)
    def run_part_test(self, data=None):
        data = super().run_part_test(data)
        return data

    # Converts list of strings into more meaningful data if necessary
    # Only really useful if you think there will be common code used twice
    def process_raw_input(self, raw_input=None):
        rules = []
        updates = []
        reading_rules = True
        for line in raw_input:
            if reading_rules:
                if line == "":
                    reading_rules = False
                    continue
                left, right = line.split("|")
                rules.append((int(left), int(right)))
            else:
                updates.append([int(x) for x in line.split(",")])
        return rules, updates

    def run_part_1(self, data=None):
        rules, updates = super().run_part_1(data)
        total = 0

        for update in updates:
            cur_rules = [rule for rule in rules if rule[0] in update and rule[1] in update]
            before_map = setup_before_map(cur_rules)
            ordered = sorted(update, key=lambda x: len(before_map.get(x, [])))
            if update == ordered:
                total += ordered[int(len(ordered) / 2)]
        return total

    def run_part_2(self, data=None):
        rules, updates = super().run_part_2(data)
        total = 0
        for update in updates:
            cur_rules = [rule for rule in rules if rule[0] in update and rule[1] in update]
            before_map = setup_before_map(cur_rules)
            ordered = sorted(update, key=lambda x: len(before_map.get(x, [])))
            if update != ordered:
                total += ordered[int(len(ordered) / 2)]
        return total


if __name__ == '__main__':
    day = Day05()
    day.run_tests(part_test=False)
