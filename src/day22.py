import typing

from functools import lru_cache

from lib.importer import read_file


@lru_cache(maxsize=None)
def intersect(_min: int, _max: int, __min: int, __max: int) -> typing.Tuple[int, int]:
    _min, _max = max(_min, __min), min(_max, __max)
    if _max - _min <= 0:
        return 0, 0
    return _min, _max


def part_a_b() -> typing.Tuple[int, int]:
    lines = read_file('day22', line_cb=lambda x: (x.split()[0] == 'on', tuple(map(lambda y: tuple(map(lambda z: int(''.join([a for a in z if a.isdigit() or a == '-'])), y.split('..'))), x.split('=')[1:]))))

    mini_region, global_region = list(), list()

    for on, ((min_x, max_x), (min_y, max_y), (min_z, max_z)) in lines:
        for region, (min_reg, max_reg) in ((mini_region, (-50, 50)), (global_region, (None, None))):
            if min_reg and max_reg:
                _min_x, _max_x = min(max(min_x, min_reg), max_reg), max(min(max_x, max_reg), min_reg)
                _min_y, _max_y = min(max(min_y, min_reg), max_reg), max(min(max_y, max_reg), min_reg)
                _min_z, _max_z = min(max(min_z, min_reg), max_reg), max(min(max_z, max_reg), min_reg)
                if _min_x == _max_x or _min_y == _max_y or _min_z == _max_z:
                    continue
            else:
                _min_x, _max_x, _min_y, _max_y, _min_z, _max_z = min_x, max_x, min_y, max_y, min_z, max_z

            for region_idx in range(len(region)):
                __min_x, __max_x, __min_y, __max_y, __min_z, __max_z, __on = region[region_idx]
                _x_min, _x_max = intersect(_min_x, _max_x, __min_x, __max_x)
                _y_min, _y_max = intersect(_min_y, _max_y, __min_y, __max_y)
                _z_min, _z_max = intersect(_min_z, _max_z, __min_z, __max_z)
                if _x_min and _x_max and _y_min and _y_max and _z_min and _z_max:
                    region.append((_x_min, _x_max, _y_min, _y_max, _z_min, _z_max, not __on))
            if on:
                region.append((_min_x, _max_x, _min_y, _max_y, _min_z, _max_z, on))

    return tuple((sum([(1 if on else -1) * (max_x - min_x + 1) * (max_y - min_y + 1) * (max_z - min_z + 1) for min_x, max_x, min_y, max_y, min_z, max_z, on in cube]) for cube in (mini_region, global_region)))


if __name__ == '__main__':
    print(part_a_b())
