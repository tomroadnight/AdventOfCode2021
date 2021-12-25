import typing

from lib.importer import read_file

    
def part_a_b() -> typing.Tuple[int, typing.Set[typing.Tuple[int, int]]]:
    filled = set(read_file('day13', line_cb=lambda x: tuple(map(int, x.split(','))), line_filter_cb=lambda x: bool(x) and x[0][0].isdigit()))
    fold = read_file('day13', line_cb=lambda x: tuple(map(lambda y: int(y) if y.isdigit() else y, x.rsplit(' ', 1)[1].split('='))), line_filter_cb=lambda x: bool(x) and x[0].startswith('fold'))

    for cnt, (d, idx) in enumerate(fold):
        filled = set(((x, y) if (d == 'y' and y < idx) or (d == 'x' and x < idx) else (idx - (x - idx) if d == 'x' else x, idx - (y - idx) if d == 'y' else y) for x, y in filled))
        if cnt == 0: 
            first_fold_count = len(filled)

    return first_fold_count, filled
    

if __name__ == '__main__':
    a, b = part_a_b()
    len_x, len_y = tuple(map(max, zip(*b)))
    print(a)
    print('\n'.join((''.join('#' if (x, y) in b else ' ' for x in range(len_x + 1))) for y in range(len_y + 1)))
