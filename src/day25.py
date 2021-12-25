from itertools import count

from lib.importer import read_file


def part_a() -> int:
    lines = read_file('day25')
    grid = {(x, y): e for y, l in enumerate(lines) for x, e in enumerate(l) if e in ('v', '>')}

    for c in count(1):
        orig_grid = grid.copy()
        for _e in ('>', 'v'):
            n_grid = {}
            for (x, y), e in grid.items():
                if e != _e:
                    n_grid[(x, y)] = e
                else:
                    new_pnt = ((x + 1) % len(lines[0]), y) if e == '>' else (x, (y + 1) % len(lines))
                    n_grid[(x, y) if new_pnt in grid else new_pnt] = e
            grid = n_grid.copy()
        
        if orig_grid == grid:
            return c


if __name__ == '__main__':
    print(part_a())
