import os
from typing import Optional, List


class Day:
    def __init__(self, input_path='input.txt', sample_path='sample.txt', test_path='test.txt'):
        self.test_path = test_path
        self.sample_path = sample_path
        self.input_path = input_path
        self._active_input = input_path

    def get_raw_input(self, input_path=None, strip=True) -> List[str]:
        input_path = self._active_input if input_path is None else input_path
        return get_lines(input_path, strip)

    def process_raw_input(self, raw_input: List[str]):
        return raw_input

    def run_tests(self, part1=True, part2=True, part_test=False, real_input=True, sample_input=True, test_input=True):
        # Uses input arguments to determine which input files to test use for testing
        selected_inputs = {}
        if test_input:
            selected_inputs['Test'] = self.test_path
        if sample_input:
            selected_inputs['Sample'] = self.sample_path
        if real_input:
            selected_inputs['Real'] = self.input_path

        # Removes any empty files from test list
        inputs = {file_type: path for file_type, path in selected_inputs.items() if os.stat(path).st_size != 0}

        if len(inputs) == 0:
            raise ValueError(f'All given input files are empty: {", ".join(selected_inputs)}')

        print(f"Day {self.get_day_str()} - Running: {', '.join(inputs.keys())}")

        original_active_input = self._active_input
        for file_type, path in inputs.items():
            self._active_input = path
            print(f"\nRunning {file_type}\t\t({path}) =========================")
            if part_test:
                print("Part Test:", self.run_part_test(self.process_raw_input(self.get_raw_input())))
            if part1:
                print("Part 1:", self.run_part_1(self.process_raw_input(self.get_raw_input())))
            if part2:
                print("Part 2:", self.run_part_2(self.process_raw_input(self.get_raw_input())))
        self._active_input = original_active_input

    def get_day_str(self):
        return self.__class__.__name__.replace("Day", "")

    def run_part_test(self, data):
        return data

    def run_part_1(self, data):
        return data

    def run_part_2(self, data):
        return data


def get_lines(path='input.txt', strip=True):
    with open(path) as file:
        lines = file.readlines()
        if strip:
            lines = [s.strip() for s in lines]
        return lines


def run_tests(part1_results, part2_results):
    if part1_results is not None:
        print("Part 1:", part1_results)
    if part2_results is not None:
        print("Part 2:", part2_results)
    print("\nDone")


def int_list(input_string: str, sep: Optional[str] = None, ignore_blanks=True) -> List[int]:
    return [int(s) for s in input_string.strip().split(sep) if ignore_blanks or s != ""]
