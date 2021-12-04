from functools import reduce
from math import prod
from lib.importer import read_file


def part_a() -> int:
    lines = read_file('day2', line_cb=lambda x: (x.split(' ')[0], int(x.split(' ')[1])))
    fwd = sum([v for d, v in lines if d == 'forward'])
    up = sum([v if d =='down' else -v for d, v in lines if d in ('up', 'down')])
    return fwd * up


def part_b() -> int:
    lines = read_file('day2', line_cb=lambda x: (x.split(' ')[0], int(x.split(' ')[1])))
    return prod(reduce(lambda acc, v: (acc[0] + v[1], acc[1] + (acc[2] * v[1]), acc[2]) if v[0] == 'forward' else (acc[0], acc[1], acc[2] + (v[1] if v[0] == 'down' else -v[1])), lines, (0, 0, 0))[:2])


if __name__ == '__main__':
    print(part_a())
    print(part_b())
