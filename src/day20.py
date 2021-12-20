import typing
from lib.importer import read_file

def part_a_b() -> typing.Tuple[int, int]:
    lines = read_file('day20', line_filter_cb=bool)
    enhancer = lines.pop(0)
    img = set((x, y) for x in range(len(lines[0])) for y in range(len(lines)) if lines[y][x] == '#')

    for i in range(50):
        if i == 2:
            iter_2 = set(img)

        pixel_compute = lambda x, y: '#' == enhancer[int(''.join(['1' if ((curr_x, curr_y) in img) or (i % 2 and enhancer[0] == '#' and (curr_y < -i or curr_y >= len(lines) + i or curr_x < -i or curr_x >= len(lines[0]) + i)) else '0' for curr_y in range(y - 1, y + 2) for curr_x in range(x - 1, x + 2)]), 2)]

        img = set((x, y) for y in range(-i - 1, len(lines) + i + 1) for x in range(-i - 1, len(lines[0]) + i + 1) if pixel_compute(x, y))

    return len(iter_2), len(img)


if __name__ == '__main__':
    print(part_a_b())
