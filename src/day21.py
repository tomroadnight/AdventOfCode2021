import typing

from functools import lru_cache
from itertools import count, product

from lib.importer import read_file


@lru_cache(maxsize=None)
def roller(l: typing.Tuple[int, typing.Tuple[int, int]], lines: typing.Tuple[int, typing.Tuple[int, int]], t: int) -> typing.Dict[int, int]:
    curr_l = dict(l)
    wins = {k: 0 for k in map(lambda x: x[0], lines)}
    for roll in product([1,2,3], repeat=3):
        incr = sum(roll)
        new_pos = ((l[t - 1][1][0] + incr - 1) % 10) + 1
        new_score = l[t - 1][1][1] + new_pos
        curr_l[t] = (new_pos, new_score)
        if new_score < 21:
            for k, v in roller(tuple(curr_l.items()), lines, 3 - t).items():
                wins[k] += v
        else:
            wins[t] += 1

    return wins


def part_a() -> int:
    lines = dict((e + 1, (v, 0)) for e, v in enumerate(read_file('day21', line_cb=lambda x: int(x.rsplit(' ', 1)[1]))))

    for _c in count(1, len(lines)*3):
        c = _c
        for player, (pos, score) in lines.items():
            dice_incr = ((c - 1) % 100) + (c % 100) + ((c + 1) % 100) + 3
            new_pos = ((pos + dice_incr - 1) % 10) + 1
            lines[player] = (new_pos, score + new_pos)
            c+=3

            is_win = [k for k, v in lines.items() if v[1] >= 1000]
            if is_win:
                return (c - 1) * lines[3 - is_win[0]][1]


def part_b() -> int:
    lines = tuple((e + 1, (v, 0)) for e, v in enumerate(read_file('day21', line_cb=lambda x: int(x.rsplit(' ', 1)[1]))))
    wins = roller(lines, lines, 1)
    return wins[max(wins, key=wins.get)]


if __name__ == '__main__':
    print((part_a(), part_b()))
