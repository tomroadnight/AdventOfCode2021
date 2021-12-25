import typing

from statistics import median, pstdev

from lib.importer import read_file


def part_a_b() -> typing.Tuple[int, int]:
    lines = read_file('day7', line_cb=lambda x: list(map(int, x.split(','))))[0]
    mid = round(median(lines))

    _range = range(round(mid - pstdev(lines)), round(mid + pstdev(lines)) + 1)

    return sum((abs(x - mid) for x in lines)), min((sum((abs(x - r) * (abs(x - r) + 1) // 2 for x in lines)) for r in _range))


if __name__ == '__main__':
    print(part_a_b())
