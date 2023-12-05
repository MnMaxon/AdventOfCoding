from typing import Self, List

import aoc_utils as utils
import pprint


class Segment:
    def __init__(self, start, seg_range, map_number=None):
        self.start: int = start
        self.range: int = seg_range
        self.map_number = map_number

    def get_last(self) -> int:
        return self.start + self.range - 1

    def contains(self, point):
        return self.start <= point <= self.get_last()

    def split_all(self, points: List[int]):
        for i in points:
            left, right = self.split(i)
            if right is not None and right.is_valid():
                ret = [left]
                ret.extend(right.split_all(points))
                return ret
        return [self.copy()]

    def split(self, point: int):
        if not (self.start < point < self.get_last() - 1):
            return self.copy(), None
        left_range = point - self.start
        return Segment(self.start, left_range), Segment(point, self.range - left_range)

    def copy(self):
        return Segment(self.start, self.range, self.map_number)

    def __str__(self):
        vals = [self.start, self.range, self.map_number]
        vals = [str(x) for x in vals if x is not None]
        return f"({', '.join(vals)})"

    def is_valid(self):
        return self.start >= 0 and self.range >= 0


def in_range(r, num):
    start, length = r[-2:]
    return start <= num < start + length


def list_categories(maps):
    return list(set('-to-'.join(maps.keys()).split("-to-")))


def get_all_stats(maps, num):
    stats = {cat: None for cat in list_categories(maps)}
    stats['seed'] = num
    while None in stats.values():
        for cat, val in stats.items():
            if val is not None:
                for transform, range_list in maps.items():
                    if transform.startswith(f'{cat}-to'):
                        stats[transform.split('-to-')[1]] = get_mapping(range_list, val)
    return stats


def map_segment(segment, map_list):
    found_mappings = [map_seg for map_seg in map_list if map_seg.contains(segment.start)]
    if len(found_mappings) == 0:
        return segment.copy()
    if len(found_mappings) == 1:
        map_seg = found_mappings[0]
        return Segment(map_seg.map_number + segment.start - map_seg.start, segment.range)
    else:
        raise ValueError(f"Found {len(found_mappings)} valid mappings, there should be 0 or 1")


def get_all_stats_seg(maps, segments):
    stats = {cat: None for cat in list_categories(maps)}
    stats['seed'] = segments
    while None in stats.values():
        for cat, seed_segments in stats.items():
            if seed_segments is None:
                continue

            for transform, map_list in maps.items():
                transform_to = transform.split('-to-')[1]
                if not transform.startswith(f'{cat}-to'):
                    continue
                all_points = get_all_points(map_list)

                cur_segs = []
                for seg in seed_segments:
                    cur_segs.extend(seg.split_all(all_points))

                stats[transform_to] = [map_segment(seg, map_list) for seg in cur_segs]
    return stats


def get_all_points(seg_list):
    all_points = set()
    for map_seg in seg_list:
        all_points.add(map_seg.start)
        all_points.add(map_seg.get_last() + 1)
    all_points = sorted(list(set(all_points)))
    return all_points


def get_mapping_segments(segment_list, segment):
    ret = []
    for map_seg in segment_list:
        inside, outside = segment.intersect(map_seg)
        if inside is not None:
            inside.start = map_seg.map_number + segment.start - map_seg.start
            ret.append(inside)
        ret.extend(outside)
    return ret


def get_mapping(range_list, num):
    valid_ranges = [r for r in range_list if in_range(r, num)]
    if len(valid_ranges) != 1:
        return num
    r = valid_ranges[0]
    return r[0] + num - r[1]


class Day05(utils.Day):
    # Used to test code, run by using Day.run_tests(part_test=True)
    def run_part_test(self, data=None):
        pass

    # Converts list of strings into more meaningful data if necessary
    # Only really useful if you think there will be common code used twice
    def process_raw_input(self, raw_input=None):
        raw_input = super().process_raw_input(raw_input)
        seeds = utils.int_list(raw_input[0].strip("seeds: "))
        maps = {}
        cur_map = ''
        for s in raw_input[2:]:
            if s == '':
                continue
            try:
                int_list = utils.int_list(s)
                maps[cur_map].append(int_list)
            except ValueError:
                cur_map = s.strip(' map:')
                maps[cur_map] = []
        maps = {cat: sorted(range_list, key=lambda x: x[0]) for cat, range_list in maps.items()}
        return seeds, maps

    def run_part_1(self, data=None):
        seeds, maps = super().run_part_1(data)
        return min([get_all_stats(maps, seed)['location'] for seed in seeds])

    def run_part_2(self, data=None):
        seed_ranges_raw, maps = super().run_part_1(data)

        for cat, tuple_list in maps.items():
            maps[cat] = [Segment(t[1], t[2], t[0]) for t in tuple_list]

        seed_segments = []
        for i in range(int(len(seed_ranges_raw) / 2)):
            seed_segments.append(Segment(seed_ranges_raw[i * 2], seed_ranges_raw[i * 2 + 1]))

        stats = get_all_stats_seg(maps, seed_segments)
        return min([s.start for s in stats['location']])


if __name__ == '__main__':
    day = Day05()
    day.run_tests(part_test=False)
