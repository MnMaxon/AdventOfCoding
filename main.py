# This is a sample Python script.
from pathlib import Path
import shutil


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def setup_folders(year: int, days=25, base_folder='.', setup_files=False):
    for day in range(days):
        day = str(day + 1)
        while len(day) < len(str(days)):
            day = f"0{day}"
        setup_folder(year, day, base_folder, setup_files)


def setup_folder(year, day, base_folder='.', setup_files=False):
    folder_name = f"day_{day}"
    folder = Path(f'{base_folder}/{year}/{folder_name}')
    folder.mkdir(parents=True, exist_ok=True)
    if setup_files:
        copy_map = {
            'day_sample/test.txt': folder / 'test.txt',
            'day_sample/sample.txt': folder / 'sample.txt',
            'day_sample/input.txt': folder / 'input.txt',
        }
        for src, dst in copy_map.items():
            if not dst.exists():
                shutil.copy(src, dst)

        day_path = folder / f'{folder_name}.py'
        if not day_path.exists():
            shutil.copy('day_sample/day_sample.py', day_path)

            # Replaces ___DAY with the day number - Ex: Day___DAY -> Day01
            with open(day_path, 'r') as f:
                py_data = f.read()
            py_data = py_data.replace('___DAY', str(day))
            with open(day_path, 'w') as f:
                f.write(py_data)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    setup_folders(2024, setup_files=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
