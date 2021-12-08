from enum import IntEnum
from lib.importer import read_file


class Segment(IntEnum):
    TOP=1
    TOP_LEFT=2
    TOP_RIGHT=3
    MIDDLE=4
    BOTTOM_LEFT=5
    BOTTOM_RIGHT=6
    BOTTOM=7


def part_a() -> int:
    lines = read_file('day8', line_cb=lambda x: tuple(map(lambda y: y.split(), x.split(' | '))))
    display = read_file('day8_display', line_filter_cb=bool)
    display_chars = {i : ''.join(set(filter(str.isalpha, ''.join(map(lambda x: x[(i%5)*7+(i%5):(i%5)*7+(i%5)+7], display[8*(i//5):8+8*(i//5)]))))) for i in range(10)}
    display_chars_unique_len_map = {len(v): k for k, v in display_chars.items() if k in (1, 4, 7, 8)}

    return sum([True for x in lines for y in x[1] if len(y) in display_chars_unique_len_map.keys()])
    
def part_b() -> int:
    lines = read_file('day8', line_cb=lambda x: tuple(map(lambda y: y.split(), x.split(' | '))))

    part_b_sum = 0
    for i, o in lines:
        digit_map = {x: set(s) for s in i for x, y in ((1, 2), (4, 4), (7, 3), (8, 7)) if len(s) == y}

        len_6 = [set(x) for x in i if len(x) == 6]

        intersections = {}
        intersections[Segment.TOP] = digit_map[7] - digit_map[1]

        bottom_left_corner = list(digit_map[8] - digit_map[4].union(intersections[Segment.TOP]))

        for idx, elem in enumerate(len_6):
            for i in bottom_left_corner:
                if digit_map[4].union(digit_map[1]).union(intersections[Segment.TOP]).union(i) == elem:
                    digit_map[9] = elem
                    len_6.pop(idx)
                    break

        intersections[Segment.BOTTOM_LEFT] = digit_map[8] - digit_map[9]
        intersections[Segment.BOTTOM] = digit_map[9] - digit_map[4] - intersections[Segment.TOP]

        mid_top_left_corner = list(digit_map[4] - digit_map[1])

        for idx, elem in enumerate(len_6):
            for i in mid_top_left_corner:
                if digit_map[7].union(intersections[Segment.BOTTOM_LEFT]).union(intersections[Segment.BOTTOM]).union(i) == elem:
                    digit_map[0] = elem
                    digit_map[6] = len_6[1 - idx]
                    break

        intersections[Segment.MIDDLE] = digit_map[8] - digit_map[0]
        intersections[Segment.TOP_RIGHT] = digit_map[8] - digit_map[6]
        intersections[Segment.TOP_LEFT] = digit_map[0] - digit_map[7] - intersections[Segment.BOTTOM_LEFT] - intersections[Segment.BOTTOM]
        intersections[Segment.BOTTOM_RIGHT] = digit_map[1] - intersections[Segment.TOP_RIGHT]

        digit_map[2] = digit_map[8] - intersections[Segment.TOP_LEFT] - intersections[Segment.BOTTOM_RIGHT]
        digit_map[3] = digit_map[8] - intersections[Segment.BOTTOM_LEFT] - intersections[Segment.TOP_LEFT]
        digit_map[5] = digit_map[8] - intersections[Segment.TOP_RIGHT] - intersections[Segment.BOTTOM_LEFT]
        digit_map_inverse = {frozenset(v): k for k, v in digit_map.items()}

        part_b_sum += int(''.join(str(digit_map_inverse[frozenset(x)]) for x in o))

    return part_b_sum


if __name__ == '__main__':
    print(part_a(), part_b())
