import typing
from collections import Counter
from functools import reduce
from operator import add
from lib.importer import read_file


def part_a_b() -> typing.Tuple[int, int]:
    days_a = 80
    days_b = 256

    lines = read_file('day6', line_cb=lambda x: list(map(int, x.split(','))))[0]
    fish = Counter(lines)

    age_sprawner = lambda fish, _: Counter({k-1: v for k, v in fish.items() if k}) + (Counter({8: fish.get(0, 0), 6: fish.get(0, 0)}) if fish.get(0) else Counter())

    up_to_day_a = reduce(age_sprawner, range(days_a), fish)

    up_to_day_b = reduce(age_sprawner, range(days_b - days_a), up_to_day_a)

    return sum(up_to_day_a.values()), sum(up_to_day_b.values())


if __name__ == '__main__':
    print(part_a_b())
