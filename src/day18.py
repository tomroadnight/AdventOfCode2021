import json, math, typing
from functools import reduce
from itertools import permutations, count
from lib.importer import read_file


def update_regular(l: typing.Union[int, typing.List[typing.Union[list, int]]], v: int, left_update: bool) -> typing.List[typing.Union[list, int]]:
    if isinstance(l, int):
        return l + v
    if left_update:
        return [update_regular(l[0], v, left_update), l[1]]
    return [l[0], update_regular(l[1], v, left_update)]


def magnitude_sum(l: typing.List[typing.Union[list, int]]) -> typing.List[typing.Union[list, int]]:
    if isinstance(l, int):
        return l
    elif len(l) > 1:
        return 3 * magnitude_sum(l[0]) + 2 * magnitude_sum(l[1])
    elif l:
        return magnitude_sum(l[0])
    return []


def part_a_b() -> typing.Tuple[int, int]:
    lines = read_file('day18', line_cb=json.loads)

    def explode(line: typing.List[typing.Union[list, int]], idx: int) -> typing.Tuple[typing.List[typing.Union[list, int]], typing.Tuple[typing.Optional[int], typing.Optional[int]], bool]:
        if idx >= 4:
            if len(line) == 2 and isinstance(line[0], int) and isinstance(line[1], int):
                return 0, (line[0], line[1]), True

        for i in range(2):
            v = line[i]
            if isinstance(v, list):
                _line, _node, c = explode(v, idx + 1)
                if _node:
                    _l, _r = _node
                if c and i == 0:
                    return [_line, update_regular(line[1], _r, True)] if _r else [_line, line[1]], (_l, None), c
                elif c and i == 1:
                    return [update_regular(line[0], _l, False), _line] if _l else [line[0], _line], (None, _r), c

        return line, None, None


    def split(line: typing.List[typing.Union[list, int]]) -> typing.Tuple[typing.List[typing.Union[list, int]], bool]:
        c = False
        for i in range(len(line)):
            v = line[i]
            if isinstance(v, int) and v >= 10:
                line[i] = [math.floor(v/2), math.ceil(v/2)]
                return line, True
            if isinstance(v, list):
                l, c = split(v)
                if c:
                    line[i] = l
                    return line, True

        return line, None


    def reducer(line: typing.List[typing.Union[list, int]]) -> typing.List[typing.Union[list, int]]:
        for _ in count():
            line, _, change = explode(line, 0)
            if not change:
                line, change = split(line)
                if not change:
                    return line


    line_sum = reduce(lambda acc, line: reducer([acc, line]), lines[1:], lines[0])

    mag_sum = magnitude_sum(line_sum)
    
    max_mag_sum_two = max(magnitude_sum(reducer([x, y])) for x, y in permutations(lines, 2))

    return mag_sum, max_mag_sum_two


if __name__ == '__main__':
    print(part_a_b())
