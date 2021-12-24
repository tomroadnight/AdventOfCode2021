import typing
from collections import defaultdict
from functools import reduce
from lib.importer import read_file

def part_a_b() -> typing.Tuple[int, int]:
    lines = read_file('day24', line_cb=lambda x: tuple(map(lambda x: int(x) if x.replace('-', '').isnumeric() else x, x.split())))

    grp_size = len(lines) // len([x for x in lines if x[0] == 'inp'])

    idx_check = lambda l, op, *_ins: op == 'add' and _ins[0] == l and isinstance(_ins[1], int)

    valid_x_idx, valid_y_idx = reduce(lambda acc, i: (acc[0], i) if idx_check('y', *lines[i]) and not acc[1] else (i, acc[1]) if idx_check('x', *lines[i]) and not acc[0] else acc, range(grp_size - 1, 0, -1), (0, 0))

    x_y_sum = lambda i, v: lines[i * grp_size + valid_x_idx][2] + lines[v * grp_size + valid_y_idx][2]

    dependencies = reduce(lambda acc, i: ([i] + acc[0], acc[1]) if lines[i * grp_size + 4][2] == 1 else (acc[0][1:], acc[1] + [(i, acc[0][0], x_y_sum(i, acc[0][0]))]) , range(len(lines) // grp_size), ([], []))[1]

    _max = defaultdict(lambda: 9, {(v if x_y > 0 else i): 9 + (-1 if x_y > 0 else 1) * x_y for i, v, x_y in dependencies})
    _min = defaultdict(lambda: 1, {(i if x_y > 0 else v): 1 + (1 if x_y > 0 else -1) * x_y for i, v, x_y in dependencies})

    return ''.join(str(_max[x]) for x in range(14)), ''.join(str(_min[x]) for x in range(14))


if __name__ == '__main__':
    print(part_a_b())
