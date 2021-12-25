import typing

from lib.importer import read_file


def freq_ox(col: typing.List[str]) -> str:
    return '0' if (col.count('0') > col.count('1')) else '1'


def freq_co2(col: typing.List[str]) -> str:
    return '0' if (col.count('1') >= col.count('0')) else '1'


def freq_calc(lines: list, freq_fn: typing.Callable) -> list:
    for j in range(len(lines[0])):
        if len(lines) == 1:
            return lines
        freq = freq_fn(''.join(x[j] for x in lines))
        lines = list(filter(lambda x: x[j] == freq, lines))
    return lines


def part_a() -> int:
    lines = read_file('day3', line_cb=list)
    lines = [[l[i] for l in lines] for i in range(len(lines[0]))]
    gamma = ''.join('1' if sum([int(y) for y in x]) > len(x)/2 else '0' for x in lines)
    epsilon = ''.join('1' if x == '0' else '0' for x in gamma)
    return int(gamma, 2) * int(epsilon, 2)


def part_b() -> int:
    lines_oxygen = lines_co2 = read_file('day3')
    return int(freq_calc(lines_oxygen, freq_ox)[0], 2) * int(freq_calc(lines_co2, freq_co2)[0], 2)
    

if __name__ == '__main__':
    print((part_a(), part_b()))
