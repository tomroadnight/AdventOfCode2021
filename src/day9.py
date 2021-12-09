
import operator, typing
from functools import reduce
from lib.importer import read_file


def part_a_b() -> typing.Tuple[int, int]:
    lines = read_file('day9', line_cb=lambda x: list(map(int, x)))
    
    def adj(i):
        for x, y in ((-1, 0), (0, -1), (1, 0), (0, 1)):
            _x, _y = i[1] + x, i[0] + y
            if not (_x < 0 or _x >= len(lines[0]) or _y < 0 or _y >= len(lines)):
                yield (_y, _x), lines[_y][_x]

    low = reduce(lambda acc, i: acc + [(i, lines[i[0]][i[1]] + 1)] if all((lines[i[0]][i[1]] < z[1] for z in adj(i))) else acc, [(y, x) for x in range(len(lines[0])) for y in range(len(lines))], [])
    low_sum = sum(map(lambda x: x[1], low))

    basin_lengths = list()
    for low_point, low_val in low:
        next_points = list((i for i in adj(low_point) if i[1] >= low_val and i[1] < 9))
        seen = [low_point]
        while next_points:
            point, point_val = next_points.pop(0)
            if point in seen: 
                continue
            seen.append(point)
            next_points.extend(list((i for i in adj(point) if i[1] >= point_val and i[1] < 9)))
        basin_lengths.append(len(seen))

    return low_sum, reduce(operator.mul, sorted(basin_lengths)[-3:], 1)


if __name__ == '__main__':
    print(part_a_b())
