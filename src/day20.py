import typing

from lib.importer import read_file


def pixel_compute(x: int, y: int, i: int, img: typing.Set[typing.Tuple[int, int]], enhancer: str, len_x: int, len_y: int) -> bool:
    pixel_region = ['1' if ((curr_x, curr_y) in img) or (i % 2 and enhancer[0] == '#' and (curr_y < -i or curr_y >= len_y + i or curr_x < -i or curr_x >= len_x + i)) else '0' for curr_y in range(y - 1, y + 2) for curr_x in range(x - 1, x + 2)]
    return '#' == enhancer[int(''.join(pixel_region), 2)]


def part_a_b() -> typing.Tuple[int, int]:
    lines = read_file('day20', line_filter_cb=bool)
    enhancer = lines.pop(0)
    len_x, len_y = len(lines[0]), len(lines)

    img = set((x, y) for y, l in enumerate(lines) for x, e in enumerate(l) if e == '#')

    for i in range(50):
        if i == 2:
            iter_2 = set(img)

        img = set((x, y) for y in range(-i - 1, len_y + i + 1) for x in range(-i - 1, len_x + i + 1) if pixel_compute(x, y, i, img, enhancer, len_x, len_y))

    return len(iter_2), len(img)


if __name__ == '__main__':
    print(part_a_b())
