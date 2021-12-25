import collections
import typing

from lib.importer import read_file


def bresenham_line_algorithm(x0: int, y0: int, x1: int, y1: int) -> typing.Set[typing.Tuple[int, int]]:
    # Bresnham Line Algorithm - (https://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm)
    line = set()
    dx =  abs(x1 - x0)
    dir_x = 1 if x0 < x1 else -1
    dy = -abs(y1 - y0)
    dir_y = 1 if y0 < y1  else -1
    d = dx + dy
    for z in (range(x0, x1 + dir_x, dir_x) if dx else range(y0, y1 + dir_y, dir_y)):
        line.add((z, y0) if dx else (x0, z))
        if dx and 2*d <= dx:
            d += dy
            y0 += dir_y
        if dy and 2*d >= dy:
            d += dx
            x0 += dir_x
    return line


def part_a_b() -> typing.Tuple[int, int]:
    lines = read_file('day5', line_cb=lambda x: list(map(int, x.replace(' -> ', ',').split(','))))  
    vents = collections.defaultdict(lambda: 0)
    vents_with_diag = collections.defaultdict(lambda: 0)
    for line in lines:
        vent_line = bresenham_line_algorithm(*line)
        for l in vent_line:
            vents_with_diag[l] += 1
        if line[0] == line[2] or line[1] == line[3]:
            for l in vent_line:
                vents[l] += 1
    return len(list(filter(lambda x: x>1, vents.values()))), len(list(filter(lambda x: x>1, vents_with_diag.values())))


if __name__ == '__main__':
    print(part_a_b())
