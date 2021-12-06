import typing
from functools import reduce
from lib.importer import read_file


def part_a_b() -> typing.Tuple[int, int]:
    days_a = 80
    days_b = 256

    lines = read_file('day6', line_cb=lambda x: list(map(int, x.split(','))))[0]
    fish = {k: lines.count(k) for k in set(lines)}

    def age_sprawn(fish: typing.Dict[int, int]) -> typing.Dict[int, int]:
        next_day_fish = {}
        for k, v in fish.items():
            if k == 0:
                next_day_fish[6] = v + next_day_fish.get(6, 0)
                next_day_fish[8] = v
            else:
                next_day_fish[k-1] = v + next_day_fish.get(k-1, 0)
        return next_day_fish

    up_to_day_a = dict(reduce(lambda acc, _: age_sprawn(acc), range(days_a), fish))

    up_to_day_b = dict(reduce(lambda acc, _: age_sprawn(acc), range(days_b - days_a), up_to_day_a))

    return sum(list(up_to_day_a.values())), sum(list(up_to_day_b.values()))


if __name__ == '__main__':
    print(part_a_b())
