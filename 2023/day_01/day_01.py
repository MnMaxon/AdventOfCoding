num_dic = {str(i): i for i in range(10)}
word_dic = {str(i): i for i in range(10)}
word_dic.update({'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9})
back_word_dic = {s[::-1]: i for s, i in word_dic.items()}


def first_num(s):
    for c in s:
        if c in num_dic:
            return num_dic[c]
    raise ValueError(f'No numbers found in {s}')


def first_num_str(s: str, d=word_dic):
    first_pos = 9999999999
    first_val = None
    for find, cur_val in d.items():
        if find in s:
            cur_pos = s.find(find)
            if cur_pos < first_pos:
                first_pos = cur_pos
                first_val = cur_val
    if first_val is None:
        raise ValueError(f'No numbers found in {s}')
    return first_val


def num_strip(line):
    return first_num(line) * 10 + first_num(reversed(line))


def num_strip_part_2(line):
    return first_num_str(line, word_dic) * 10 + first_num_str(line[::-1], back_word_dic)


def part_1():
    total = 0
    with open('input.txt') as file:
        for line in file.readlines():
            total += num_strip(line)
    return total


def part_2():
    total = 0
    with open('input.txt') as file:
    # with open('sample.txt') as file:
        for line in file.readlines():
            num = num_strip_part_2(line)
            # print(num)
            total += num
    return total


# print(first_num_str("oene2three"))

print("Part 1:", part_1())
print("Part 2:", part_2())
